"""bbis_extract.py is a python script for extracting data within executables (e.g. .EXE).
    This script implements a PoC (Proof-of-Concept) system for BBIS (Binary-Based Instruction Substitution)."""

import os
import magic
import argparse

from bbis_hide import get_executable_binary,get_executable_offsets,clear_logs
from opcode_map_db import extraction_opcode_map


def get_arguments_cli():
    """Gets user input from CLI."""
    parser = argparse.ArgumentParser(prog='bbis_extract.py',description='Extract a file hidden with bbis_hide.py within executable.')
    parser.add_argument('-e','--executable',type=str,required=True,help='Path to executable for extraction.')
    parser.add_argument('-o','--output',type=str,required=False,help='Name of output file after extraction.')
    return parser.parse_args()


def get_byte_conversion(bytes):
    return extraction_opcode_map.get(bytes)


def extract_binary_data(buffer,offsets):
    binary_data = ''
    # start = ''
    end = ''
    i = 0
    offset = 0
    used_offsets = []

    while len(end) < 16:
        # Current offset
        offset = offsets[i]
        opcode = f"{buffer[offset]} {buffer[offset+1]}"
        # print(f"Offset:{offset}; opcode:{opcode}")
        if opcode in extraction_opcode_map:
            end += get_byte_conversion(opcode)
            # used_offsets.append(offset)
        # Increase 'i' to next offset in 'offsets'
        i += 1

    # start = int(start,2)
    end = int(end,2)
    # i -= 1
    offset = offsets[i]
    while offset <= end:
        opcode = f"{buffer[offset]} {buffer[offset+1]}"
        # print(f"Offset:{offset}; opcode:{opcode}")
        if opcode in extraction_opcode_map:
            binary_data += get_byte_conversion(opcode)
            # used_offsets.append(offset)

        i += 1
        offset = offsets[i]

    # with open("extraction-offsets.txt","w") as file:
    #     for offset in offsets:
    #         file.write(f"{offset}\n")

    return binary_data


def convert_binary_to_file(binary_data):
    return int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder='big')


def get_file_type(file_binary):
    file_type = magic.from_buffer(file_binary, mime=True).split('/')[1]
    if file_type == 'plain':
        file_type = 'txt'
    return file_type


def write_file(file_binary,file_name,file_type):
    name = f"output-file.{file_type}"
    if file_name:
        name = f"{file_name}.{file_type}"
    with open(name,"wb") as file:
        file.write(file_binary)


if __name__ == '__main__':
    # Get arguments from CLI
    args = get_arguments_cli()
    # Path to executable file
    executable = args.executable
    # Get targeted mnemonics offsets from executable's object data
    offsets_list = get_executable_offsets(executable)
    offsets = [x[0] for x in offsets_list]
    # Get file's binary data
    buffer = get_executable_binary(executable)
    binary_data = extract_binary_data(buffer,offsets)
    # print(f"Extracted binary data:{binary_data}")
    file_binary = convert_binary_to_file(binary_data)
    file_type = get_file_type(file_binary)
    file_name = args.output
    write_file(file_binary,file_name,file_type)
    clear_logs(os.path.basename(executable))