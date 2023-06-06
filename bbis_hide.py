"""bbis_hide.py is a python script for hiding data in executables (e.g. .EXE).
    This script implements a PoC (Proof-of-Concept) system for BBIS (Binary-Based Instruction Substitution)."""

import os
import time
import argparse

from opcode_map_db import target_map, decode_opcode_map_0_to_1, decode_opcode_map_1_to_0

map_dict = \
    {
        0: decode_opcode_map_1_to_0,
        1: decode_opcode_map_0_to_1
    }


def get_arguments_cli():
    """Gets user input from CLI."""
    parser = argparse.ArgumentParser(prog='bbis_hide.py',
                                     description='Python script to decode\extract data within executable file.')
    # parser.add_argument('-a', '--action', type=str, required=True, help='-a or --action [=decode,=extract] (choose whether you want to decode or extract data)')
    parser.add_argument('-d', '--data', type=str, required=True, help='Path to data (file) to hide in executable')
    parser.add_argument('-e', '--executable', type=str, required=True, help='Path to executable to hide file within')
    return parser.parse_args()


def get_file_binary_data(file):
    """Reads file's binary data, converts binary data to binary string.
    :param file: file path
    :return binary: file's binary data in base 2 (binary) as string"""
    with open(file, 'rb') as reader:
        binary = reader.read()
    binary = bin(int.from_bytes(binary, byteorder='big'))[2:]
    return binary


def get_executable_binary(executable):
    """Reads executable and returns binary data as bytearray"""
    return bytearray(open(executable, 'rb').read())


def get_executable_object_data(executable):
    # Get executable name from path
    exe_name = os.path.basename(executable).split('.')[0]
    # Disassemble .EXE file's code section with intel x8086 mnemonics and save output
    os.system(f'objdump -d -M intel {executable} > {exe_name}_dump.txt')
    # Get info about object code - code section's offset,size,virtual address
    os.system(f'objdump -h {executable} > {exe_name}_code_offset.txt')
    # Read object code's disassembly to 'dump'
    dump = open(f'{exe_name}_dump.txt', 'r').readlines()[7:]
    # Read object code's information to 'info'
    info = open(f'{exe_name}_code_offset.txt', 'r').readlines()[5:6]
    # Converting 'info' from list to str
    info = str(info[0])
    virtual_offset = info[28:36]
    code_offset = info[48:56]
    dump = [x.split('\t') for x in dump]
    return (dump, virtual_offset, code_offset)


def organize_mnemonics_list(dump):
    # Iterate through 'dump' and append commands to 'mnemonic_list'
    # Each x is a list and contains [offset,hex value,command(optional)] (sometimes there's NOP or line of zero)
    return [[x[0].replace(' ', ''), x[1].replace(' ', ''), x[2].replace(' ', '')] for x in dump if len(x) == 3]


def get_target_mnemonics(mnemonic_list):
    return [mnemonic_list[i] for i in range(len(mnemonic_list)) if mnemonic_list[i][1] in target_map]


def calculate_offsets(target_list, virtual_offset, code_offset):
    """Calculates for every target mnemonic it's real offset from virtual offset and returns a list"""
    offsets = [(int(hex((int(x[0][:-1], 16) - int(virtual_offset, 16)) + int(code_offset, 16)), 16), x[1]) for x in
               target_list]

    # For debugging purposes
    # with open("offsets-list.txt","w") as file:
    #     for offset in offsets:
    #         file.write(f"{offset}\n")

    return offsets
    # return [(int(hex((int(x[0][:-1], 16) - int(virtual_offset, 16)) + int(code_offset, 16)), 16), x[1]) for x in target_list]


def get_executable_offsets(executable):
    """Get all assembly mnemonics from binary file code section,
        parses them and gets assembly mnemonics that are in the opcode mapping with their offsets"""
    # Get executable's assembly code (dump), virtual offset, and code offset (code section location)
    res = get_executable_object_data(executable)
    dump, virtual_offset, code_offset = res[0], res[1], res[2]
    # Organize mnemonics
    mnemonic_list = organize_mnemonics_list(dump)
    # Get target mnemonics from whole assembly code
    target_list = get_target_mnemonics(mnemonic_list)
    # Return list of tuples (offset,opcode)
    return calculate_offsets(target_list, virtual_offset, code_offset)


def get_opcode_conversion(opcode, param):
    """Converts opcodes based on their value in map and 'param'. If 'param' is 0 and opcode value in map is 1 then
    it will convert it to it's equal opcode that has value of 0 in map."""
    return int(map_dict.get(param).get(opcode).split()[0]), int(map_dict.get(param).get(opcode).split()[1])


def decode_data_within_executable(buffer, binary_data, offsets):
    """Gets buffer and binary input to decode inside buffer
        :param buffer: Buffer for executable file.
        :param binary_data: File's binary representation to decode inside executable (buffer).
        :param offsets: List of offsets for mnemonics in buffer."""
    i = j = 0
    binary = ''

    try:
        while i < len(binary_data):
            # Current bit in binary data
            bit = binary_data[i]
            # Current offset from offset list
            offset = offsets[j]
            # Current opcode (all targeted mnemonics are 2 bytes)
            opcode = f'{buffer[offset]} {buffer[offset + 1]}'
            # print(f"Offset:{offset}; opcode:{opcode}; bit:{bit}; index:{j}")
            if bit == '1':
                # If current bit is 1 check whether current opcode gives value of 0 in map
                if opcode in decode_opcode_map_0_to_1:
                    # Substitute opcode with another one that equals 1 in map
                    buffer[offset], buffer[offset + 1] = get_opcode_conversion(opcode, 1)
                    # print(f"Converted to: {buffer[offset]} {buffer[offset+1]} => 1")
            elif bit == '0':
                # If current bit is 0 check whether current opcode gives value of 1 in map
                if opcode in decode_opcode_map_1_to_0:
                    # Substitute opcode with another one that equals 0 in map
                    buffer[offset], buffer[offset + 1] = get_opcode_conversion(opcode, 0)
                    # print(f"Converted to: {buffer[offset]} {buffer[offset + 1]} =>0")
            i += 1
            j += 1
    except IndexError as e:
        print(e)
        exit()

    if j < len(binary_data):
        print('The code section in this executable is not enough to hide this message.')
        print(f'Still {len(binary_data) - j} bits left to hide.')
        print('Program exits')
        exit()

    return buffer


def write_buffer(buffer, executable):
    """Write buffer back to hard-disk (physical memory) in current directory"""
    with open(f"{executable}", "wb") as file:
        file.write(buffer)


def modify_buffer(buffer, binary_data, offsets_list):
    """Modify buffer (executable file) according to binary input (file).
    :param buffer: executable file to modify.
    :param binary_data: binary string to hide inside executable file.
    :param offsets_list: list containing tuples of offsets and opcodes."""
    # Getting only offsets in list of tuples
    offsets = [int(x[0]) for x in offsets_list]
    # Calculate starting offset to start decoding actual data
    # The first 32-bits are saved to mark the start and end of data
    # start_binary = '0' * (16 - len(bin(offsets[32])[2:])) + bin(offsets[32])[2:]
    try:
        end_binary = '0' * (16 - len(bin(offsets[len(binary_data) + 15])[2:])) + bin(offsets[len(binary_data) + 15])[2:]
    except IndexError:
        print(f"Not enough offsets to decode bits with, need executable with bigger code section")
        print(f"Program exits")
        exit()

    # print(f"Start offset: {int(start_binary,2)}")
    # print(f"End offset: {int(end_binary, 2)}")
    # Concatenate binary end mark with binary data
    full_binary_data = end_binary + binary_data
    # Decode 'full_binary_data' within executable file
    decode_data_within_executable(buffer, full_binary_data, offsets)
    return buffer


def clear_logs(exe_name):
    exe_name = os.path.basename(exe_name).split('.')[0]
    os.system(f'del {exe_name}_code_offset.txt, {exe_name}_dump.txt')


if __name__ == '__main__':
    # Get arguments from CLI
    args = get_arguments_cli()
    # # Action to perform (to hide or extract data)
    # action = args.action
    # Path to file for hiding or extracting
    data = args.data
    # Path to executable file
    executable = args.executable
    # Get targeted mnemonics offsets from executable's object data
    offsets_list = get_executable_offsets(executable)
    # Get file's binary data
    binary_data = get_file_binary_data(data)
    # Load executable's data into buffer
    buffer = get_executable_binary(executable)
    # Modify buffer according to 'binary_data'
    buffer = modify_buffer(buffer, binary_data, offsets_list)
    # Get executable's name from path
    exe_name = os.path.basename(executable)
    # Write modified buffer back to hard-disk (looks exactly like original)
    write_buffer(buffer, exe_name)
    # Delete executable's object data logs
    clear_logs(exe_name)
