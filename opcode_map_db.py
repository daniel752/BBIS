target_map = \
{
    '31c0',  # XOR EAX,EAX
    '33c0',  # XOR EAX,EAX
    '31d8',  # XOR EAX,EBX
    '33c3',  # XOR EAX,EBX
    '31c8',  # XOR EAX,ECX
    '33c1',  # XOR EAX,ECX
    '31d0',  # XOR EAX,EDX
    '33c2',  # XOR EAX,EDX
    '31e0',  # XOR EAX,ESP
    '33c4',  # XOR EAX,ESP
    '31e8',  # XOR EAX,EBP
    '33c5',  # XOR EAX,EBP
    '31f0',  # XOR EAX,ESI
    '33c6',  # XOR EAX,ESI
    '31f8',  # XOR EAX,EDI
    '33c7',  # XOR EAX,EDI
    '31c3',  # XOR EBX,EAX
    '33d8',  # XOR EBX,EAX
    '31db',  # XOR EBX,EBX
    '33db',  # XOR EBX,EBX
    '31cb',  # XOR EBX,ECX
    '33d9',  # XOR EBX,ECX
    '31d3',  # XOR EBX,EDX
    '33da',  # XOR EBX,EDX
    '31e3',  # XOR EBX,ESP
    '33dc',  # XOR EBX,ESP
    '31eb',  # XOR EBX,EBP
    '33dd',  # XOR EBX,EBP
    '31f3',  # XOR EBX,ESI
    '33de',  # XOR EBX,ESI
    '31fb',  # XOR EBX,EDI
    '33df',  # XOR EBX,EDI
    '31c1',  # XOR ECX,EAX
    '33c8',  # XOR ECX,EAX
    '31d9',  # XOR ECX,EBX
    '33cb',  # XOR ECX,EBX
    '31c9',  # XOR ECX,ECX
    '33c9',  # XOR ECX,ECX
    '31d1',  # XOR ECX,EDX
    '33ca',  # XOR ECX,EDX
    '31e1',  # XOR ECX,ESP
    '33cc',  # XOR ECX,ESP
    '31e9',  # XOR ECX,EBP
    '33cd',  # XOR ECX,EBP
    '31f1',  # XOR ECX,ESI
    '33ce',  # XOR ECX,ESI
    '31f9',  # XOR ECX,EDI
    '33cf',  # XOR ECX,EDI
    '31c2',  # XOR EDX,EAX
    '33d0',  # XOR EDX,EAX
    '31da',  # XOR EDX,EBX
    '33d3',  # XOR EDX,EBX
    '31ca',  # XOR EDX,ECX
    '33d1',  # XOR EDX,ECX
    '31d2',  # XOR EDX,EDX
    '33d2',  # XOR EDX,EDX
    '31e2',  # XOR EDX,ESP
    '33d4',  # XOR EDX,ESP
    '31ea',  # XOR EDX,EBP
    '33d5',  # XOR EDX,EBP
    '31f2',  # XOR EDX,ESI
    '33d6',  # XOR EDX,ESI
    '31fa',  # XOR EDX,EDI
    '33d7',  # XOR EDX,EDI
    '31c4',  # XOR ESP,EAX
    '33e0',  # XOR ESP,EAX
    '31dc',  # XOR ESP,EBX
    '33e3',  # XOR ESP,EBX
    '31cc',  # XOR ESP,ECX
    '33e1',  # XOR ESP,ECX
    '31d4',  # XOR ESP,EDX
    '33e2',  # XOR ESP,EDX
    '31e4',  # XOR ESP,ESP
    '33e4',  # XOR ESP,ESP
    '31ec',  # XOR ESP,EBP
    '33e5',  # XOR ESP,EBP
    '31f4',  # XOR ESP,ESI
    '33e6',  # XOR ESP,ESI
    '31fc',  # XOR ESP,EDI
    '33e7',  # XOR ESP,EDI
    '31c5',  # XOR EBP,EAX
    '33e8',  # XOR EBP,EAX
    '31dd',  # XOR EBP,EBX
    '33eb',  # XOR EBP,EBX
    '31cd',  # XOR EBP,ECX
    '33e9',  # XOR EBP,ECX
    '31d5',  # XOR EBP,EDX
    '33ea',  # XOR EBP,EDX
    '31e5',  # XOR EBP,ESP
    '33ec',  # XOR EBP,ESP
    '31ed',  # XOR EBP,EBP
    '33ed',  # XOR EBP,EBP
    '31f5',  # XOR EBP,ESI
    '33ee',  # XOR EBP,ESI
    '31fd',  # XOR EBP,EDI
    '33ef',  # XOR EBP,EDI
    '31c6',  # XOR ESI,EAX
    '33f0',  # XOR ESI,EAX
    '31de',  # XOR ESI,EBX
    '33f3',  # XOR ESI,EBX
    '31ce',  # XOR ESI,ECX
    '33f1',  # XOR ESI,ECX
    '31d6',  # XOR ESI,EDX
    '33f2',  # XOR ESI,EDX
    '31e6',  # XOR ESI,ESP
    '33f4',  # XOR ESI,ESP
    '31ee',  # XOR ESI,EBP
    '33f5',  # XOR ESI,EBP
    '31f6',  # XOR ESI,ESI
    '33f6',  # XOR ESI,ESI
    '31fe',  # XOR ESI,EDI
    '33f7',  # XOR ESI,EDI
    '31c7',  # XOR EDI,EAX
    '33f8',  # XOR EDI,EAX
    '31df',  # XOR EDI,EBX
    '33fb',  # XOR EDI,EBX
    '31cf',  # XOR EDI,ECX
    '33f9',  # XOR EDI,ECX
    '31d7',  # XOR EDI,EDX
    '33fa',  # XOR EDI,EDX
    '31e7',  # XOR EDI,ESP
    '33fc',  # XOR EDI,ESP
    '31ef',  # XOR EDI,EBP
    '33fd',  # XOR EDI,EBP
    '31f7',  # XOR EDI,ESI
    '33fe',  # XOR EDI,ESI
    '31ff',  # XOR EDI,EDI
    '33ff',  # XOR EDI,EDI
    '30e4',  # XOR AH,AH
    '32e4',  # XOR AH,AH
    '30fc',  # XOR AH,BH
    '32e7',  # XOR AH,BH
    '30ec',  # XOR AH,CH
    '32e5',  # XOR AH,CH
    '30f4',  # XOR AH,DH
    '32e6',  # XOR AH,DH
    '30e7',  # XOR BH,AH
    '32fc',  # XOR BH,AH
    '30ff',  # XOR BH,BH
    '32ff',  # XOR BH,BH
    '30ef',  # XOR BH,CH
    '32fd',  # XOR BH,CH
    '30f7',  # XOR BH,DH
    '32fe',  # XOR BH,DH
    '30e5',  # XOR CH,AH
    '32ec',  # XOR CH,AH
    '30fd',  # XOR CH,BH
    '32ef',  # XOR CH,BH
    '30ed',  # XOR CH,CH
    '32ed',  # XOR CH,CH
    '30f5',  # XOR CH,DH
    '32ee',  # XOR CH,DH
    '30e6',  # XOR DH,AH
    '32f4',  # XOR DH,AH
    '30fe',  # XOR DH,BH
    '32f7',  # XOR DH,BH
    '30ee',  # XOR DH,CH
    '32f5',  # XOR DH,CH
    '30f6',  # XOR DH,DH
    '32f6',  # XOR DH,DH
    '30c0',  # XOR AL,AL
    '32c0',  # XOR AL,AL
    '30d8',  # XOR AL,BL
    '32c3',  # XOR AL,BL
    '30c8',  # XOR AL,CL
    '32c1',  # XOR AL,CL
    '30d0',  # XOR AL,DL
    '32c2',  # XOR AL,DL
    '30c3',  # XOR BL,AL
    '32d8',  # XOR BL,AL
    '30db',  # XOR BL,BL
    '32db',  # XOR BL,BL
    '30cb',  # XOR BL,CL
    '32d9',  # XOR BL,CL
    '30d3',  # XOR BL,DL
    '32da',  # XOR BL,DL
    '30c1',  # XOR CL,AL
    '32c8',  # XOR CL,AL
    '30d9',  # XOR CL,BL
    '32cb',  # XOR CL,BL
    '30c9',  # XOR CL,CL
    '32c9',  # XOR CL,CL
    '30d1',  # XOR CL,DL
    '32ca',  # XOR CL,DL
    '30c2',  # XOR DL,AL
    '32d0',  # XOR DL,AL
    '30da',  # XOR DL,BL
    '32d3',  # XOR DL,BL
    '30ca',  # XOR DL,CL
    '32d1',  # XOR DL,CL
    '30d2',  # XOR DL,DL
    '32d2',  # XOR DL,DL
    '89c0',  # MOV EAX,EAX
    '8bc0',  # MOV EAX,EAX
    '89d8',  # MOV EAX,EBX
    '8bc3',  # MOV EAX,EBX
    '89c8',  # MOV EAX,ECX
    '8bc1',  # MOV EAX,ECX
    '89d0',  # MOV EAX,EDX
    '8bc2',  # MOV EAX,EDX
    '89e0',  # MOV EAX,ESP
    '8bc4',  # MOV EAX,ESP
    '89e8',  # MOV EAX,EBP
    '8bc5',  # MOV EAX,EBP
    '89f0',  # MOV EAX,ESI
    '8bc6',  # MOV EAX,ESI
    '89f8',  # MOV EAX,EDI
    '8bc7',  # MOV EAX,EDI
    '89c3',  # MOV EBX,EAX
    '8bd8',  # MOV EBX,EAX
    '89db',  # MOV EBX,EBX
    '8bdb',  # MOV EBX,EBX
    '89cb',  # MOV EBX,ECX
    '8bd9',  # MOV EBX,ECX
    '89d3',  # MOV EBX,EDX
    '8bda',  # MOV EBX,EDX
    '89e3',  # MOV EBX,ESP
    '8bdc',  # MOV EBX,ESP
    '89eb',  # MOV EBX,EBP
    '8bdd',  # MOV EBX,EBP
    '89f3',  # MOV EBX,ESI
    '8bde',  # MOV EBX,ESI
    '89fb',  # MOV EBX,EDI
    '8bdf',  # MOV EBX,EDI
    '89c1',  # MOV ECX,EAX
    '8bc8',  # MOV ECX,EAX
    '89d9',  # MOV ECX,EBX
    '8bcb',  # MOV ECX,EBX
    '89c9',  # MOV ECX,ECX
    '8bc9',  # MOV ECX,ECX
    '89d1',  # MOV ECX,EDX
    '8bca',  # MOV ECX,EDX
    '89e1',  # MOV ECX,ESP
    '8bcc',  # MOV ECX,ESP
    '89e9',  # MOV ECX,EBP
    '8bcd',  # MOV ECX,EBP
    '89f1',  # MOV ECX,ESI
    '8bce',  # MOV ECX,ESI
    '89f9',  # MOV ECX,EDI
    '8bcf',  # MOV ECX,EDI
    '89c2',  # MOV EDX,EAX
    '8bd0',  # MOV EDX,EAX
    '89da',  # MOV EDX,EBX
    '8bd3',  # MOV EDX,EBX
    '89ca',  # MOV EDX,ECX
    '8bd1',  # MOV EDX,ECX
    '89d2',  # MOV EDX,EDX
    '8bd2',  # MOV EDX,EDX
    '89e2',  # MOV EDX,ESP
    '8bd4',  # MOV EDX,ESP
    '89ea',  # MOV EDX,EBP
    '8bd5',  # MOV EDX,EBP
    '89f2',  # MOV EDX,ESI
    '8bd6',  # MOV EDX,ESI
    '89fa',  # MOV EDX,EDI
    '8bd7',  # MOV EDX,EDI
    '89c4',  # MOV ESP,EAX
    '8be0',  # MOV ESP,EAX
    '89dc',  # MOV ESP,EBX
    '8be3',  # MOV ESP,EBX
    '89cc',  # MOV ESP,ECX
    '8be1',  # MOV ESP,ECX
    '89d4',  # MOV ESP,EDX
    '8be2',  # MOV ESP,EDX
    '89e4',  # MOV ESP,ESP
    '8be4',  # MOV ESP,ESP
    '89ec',  # MOV ESP,EBP
    '8be5',  # MOV ESP,EBP
    '89f4',  # MOV ESP,ESI
    '8be6',  # MOV ESP,ESI
    '89fc',  # MOV ESP,EDI
    '8be7',  # MOV ESP,EDI
    '89c5',  # MOV EBP,EAX
    '8be8',  # MOV EBP,EAX
    '89dd',  # MOV EBP,EBX
    '8beb',  # MOV EBP,EBX
    '89cd',  # MOV EBP,ECX
    '8be9',  # MOV EBP,ECX
    '89d5',  # MOV EBP,EDX
    '8bea',  # MOV EBP,EDX
    '89e5',  # MOV EBP,ESP
    '8bec',  # MOV EBP,ESP
    '89ed',  # MOV EBP,EBP
    '8bed',  # MOV EBP,EBP
    '89f5',  # MOV EBP,ESI
    '8bee',  # MOV EBP,ESI
    '89fd',  # MOV EBP,EDI
    '8bef',  # MOV EBP,EDI
    '89c6',  # MOV ESI,EAX
    '8bf0',  # MOV ESI,EAX
    '89de',  # MOV ESI,EBX
    '8bf3',  # MOV ESI,EBX
    '89ce',  # MOV ESI,ECX
    '8bf1',  # MOV ESI,ECX
    '89d6',  # MOV ESI,EDX
    '8bf2',  # MOV ESI,EDX
    '89e6',  # MOV ESI,ESP
    '8bf4',  # MOV ESI,ESP
    '89ee',  # MOV ESI,EBP
    '8bf5',  # MOV ESI,EBP
    '89f6',  # MOV ESI,ESI
    '8bf6',  # MOV ESI,ESI
    '89fe',  # MOV ESI,EDI
    '8bf7',  # MOV ESI,EDI
    '89c7',  # MOV EDI,EAX
    '8bf8',  # MOV EDI,EAX
    '89df',  # MOV EDI,EBX
    '8bfb',  # MOV EDI,EBX
    '89cf',  # MOV EDI,ECX
    '8bf9',  # MOV EDI,ECX
    '89d7',  # MOV EDI,EDX
    '8bfa',  # MOV EDI,EDX
    '89e7',  # MOV EDI,ESP
    '8bfc',  # MOV EDI,ESP
    '89ef',  # MOV EDI,EBP
    '8bfd',  # MOV EDI,EBP
    '89f7',  # MOV EDI,ESI
    '8bfe',  # MOV EDI,ESI
    '89ff',  # MOV EDI,EDI
    '8bff',  # MOV EDI,EDI
    '88e4',  # MOV AH,AH
    '8ae4',  # MOV AH,AH
    '88fc',  # MOV AH,BH
    '8ae7',  # MOV AH,BH
    '88ec',  # MOV AH,CH
    '8ae5',  # MOV AH,CH
    '88f4',  # MOV AH,DH
    '8ae6',  # MOV AH,DH
    '88e7',  # MOV BH,AH
    '8afc',  # MOV BH,AH
    '88ff',  # MOV BH,BH
    '8aff',  # MOV BH,BH
    '88ef',  # MOV BH,CH
    '8afd',  # MOV BH,CH
    '88f7',  # MOV BH,DH
    '8afe',  # MOV BH,DH
    '88e5',  # MOV CH,AH
    '8aec',  # MOV CH,AH
    '88fd',  # MOV CH,BH
    '8aef',  # MOV CH,BH
    '88ed',  # MOV CH,CH
    '8aed',  # MOV CH,CH
    '88f5',  # MOV CH,DH
    '8aee',  # MOV CH,DH
    '88e6',  # MOV DH,AH
    '8af4',  # MOV DH,AH
    '88fe',  # MOV DH,BH
    '8af7',  # MOV DH,BH
    '88ee',  # MOV DH,CH
    '8af5',  # MOV DH,CH
    '88f6',  # MOV DH,DH
    '8af6',  # MOV DH,DH
    '88c0',  # MOV AL,AL
    '8ac0',  # MOV AL,AL
    '88d8',  # MOV AL,BL
    '8ac3',  # MOV AL,BL
    '88c8',  # MOV AL,CL
    '8ac1',  # MOV AL,CL
    '88d0',  # MOV AL,DL
    '8ac2',  # MOV AL,DL
    '88c3',  # MOV BL,AL
    '8ad8',  # MOV BL,AL
    '88db',  # MOV BL,BL
    '8adb',  # MOV BL,BL
    '88cb',  # MOV BL,CL
    '8ad9',  # MOV BL,CL
    '88d3',  # MOV BL,DL
    '8ada',  # MOV BL,DL
    '88c1',  # MOV CL,AL
    '8ac8',  # MOV CL,AL
    '88d9',  # MOV CL,BL
    '8acb',  # MOV CL,BL
    '88c9',  # MOV CL,CL
    '8ac9',  # MOV CL,CL
    '88d1',  # MOV CL,DL
    '8aca',  # MOV CL,DL
    '88c2',  # MOV DL,AL
    '8ad0',  # MOV DL,AL
    '88da',  # MOV DL,BL
    '8ad3',  # MOV DL,BL
    '88ca',  # MOV DL,CL
    '8ad1',  # MOV DL,CL
    '88d2',  # MOV DL,DL
    '8ad2',  # MOV DL,DL
    '01c0',  # ADD EAX,EAX
    '03c0',  # ADD EAX,EAX
    '01d8',  # ADD EAX,EBX
    '03c3',  # ADD EAX,EBX
    '01c8',  # ADD EAX,ECX
    '03c1',  # ADD EAX,ECX
    '01d0',  # ADD EAX,EDX
    '03c2',  # ADD EAX,EDX
    '01e0',  # ADD EAX,ESP
    '03c4',  # ADD EAX,ESP
    '01e8',  # ADD EAX,EBP
    '03c5',  # ADD EAX,EBP
    '01f0',  # ADD EAX,ESI
    '03c6',  # ADD EAX,ESI
    '01f8',  # ADD EAX,EDI
    '03c7',  # ADD EAX,EDI
    '01c3',  # ADD EBX,EAX
    '03d8',  # ADD EBX,EAX
    '01db',  # ADD EBX,EBX
    '03db',  # ADD EBX,EBX
    '01cb',  # ADD EBX,ECX
    '03d9',  # ADD EBX,ECX
    '01d3',  # ADD EBX,EDX
    '03da',  # ADD EBX,EDX
    '01e3',  # ADD EBX,ESP
    '03dc',  # ADD EBX,ESP
    '01eb',  # ADD EBX,EBP
    '03dd',  # ADD EBX,EBP
    '01f3',  # ADD EBX,ESI
    '03de',  # ADD EBX,ESI
    '01fb',  # ADD EBX,EDI
    '03df',  # ADD EBX,EDI
    '01c1',  # ADD ECX,EAX
    '03c8',  # ADD ECX,EAX
    '01d9',  # ADD ECX,EBX
    '03cb',  # ADD ECX,EBX
    '01c9',  # ADD ECX,ECX
    '03c9',  # ADD ECX,ECX
    '01d1',  # ADD ECX,EDX
    '03ca',  # ADD ECX,EDX
    '01e1',  # ADD ECX,ESP
    '03cc',  # ADD ECX,ESP
    '01e9',  # ADD ECX,EBP
    '03cd',  # ADD ECX,EBP
    '01f1',  # ADD ECX,ESI
    '03ce',  # ADD ECX,ESI
    '01f9',  # ADD ECX,EDI
    '03cf',  # ADD ECX,EDI
    '01c2',  # ADD EDX,EAX
    '03d0',  # ADD EDX,EAX
    '01da',  # ADD EDX,EBX
    '03d3',  # ADD EDX,EBX
    '01ca',  # ADD EDX,ECX
    '03d1',  # ADD EDX,ECX
    '01d2',  # ADD EDX,EDX
    '03d2',  # ADD EDX,EDX
    '01e2',  # ADD EDX,ESP
    '03d4',  # ADD EDX,ESP
    '01ea',  # ADD EDX,EBP
    '03d5',  # ADD EDX,EBP
    '01f2',  # ADD EDX,ESI
    '03d6',  # ADD EDX,ESI
    '01fa',  # ADD EDX,EDI
    '03d7',  # ADD EDX,EDI
    '01c4',  # ADD ESP,EAX
    '03e0',  # ADD ESP,EAX
    '01dc',  # ADD ESP,EBX
    '03e3',  # ADD ESP,EBX
    '01cc',  # ADD ESP,ECX
    '03e1',  # ADD ESP,ECX
    '01d4',  # ADD ESP,EDX
    '03e2',  # ADD ESP,EDX
    '01e4',  # ADD ESP,ESP
    '03e4',  # ADD ESP,ESP
    '01ec',  # ADD ESP,EBP
    '03e5',  # ADD ESP,EBP
    '01f4',  # ADD ESP,ESI
    '03e6',  # ADD ESP,ESI
    '01fc',  # ADD ESP,EDI
    '03e7',  # ADD ESP,EDI
    '01c5',  # ADD EBP,EAX
    '03e8',  # ADD EBP,EAX
    '01dd',  # ADD EBP,EBX
    '03eb',  # ADD EBP,EBX
    '01cd',  # ADD EBP,ECX
    '03e9',  # ADD EBP,ECX
    '01d5',  # ADD EBP,EDX
    '03ea',  # ADD EBP,EDX
    '01e5',  # ADD EBP,ESP
    '03ec',  # ADD EBP,ESP
    '01ed',  # ADD EBP,EBP
    '03ed',  # ADD EBP,EBP
    '01f5',  # ADD EBP,ESI
    '03ee',  # ADD EBP,ESI
    '01fd',  # ADD EBP,EDI
    '03ef',  # ADD EBP,EDI
    '01c6',  # ADD ESI,EAX
    '03f0',  # ADD ESI,EAX
    '01de',  # ADD ESI,EBX
    '03f3',  # ADD ESI,EBX
    '01ce',  # ADD ESI,ECX
    '03f1',  # ADD ESI,ECX
    '01d6',  # ADD ESI,EDX
    '03f2',  # ADD ESI,EDX
    '01e6',  # ADD ESI,ESP
    '03f4',  # ADD ESI,ESP
    '01ee',  # ADD ESI,EBP
    '03f5',  # ADD ESI,EBP
    '01f6',  # ADD ESI,ESI
    '03f6',  # ADD ESI,ESI
    '01fe',  # ADD ESI,EDI
    '03f7',  # ADD ESI,EDI
    '01c7',  # ADD EDI,EAX
    '03f8',  # ADD EDI,EAX
    '01df',  # ADD EDI,EBX
    '03fb',  # ADD EDI,EBX
    '01cf',  # ADD EDI,ECX
    '03f9',  # ADD EDI,ECX
    '01d7',  # ADD EDI,EDX
    '03fa',  # ADD EDI,EDX
    '01e7',  # ADD EDI,ESP
    '03fc',  # ADD EDI,ESP
    '01ef',  # ADD EDI,EBP
    '03fd',  # ADD EDI,EBP
    '01f7',  # ADD EDI,ESI
    '03fe',  # ADD EDI,ESI
    '01ff',  # ADD EDI,EDI
    '03ff',  # ADD EDI,EDI
    '00e4',  # ADD AH,AH
    '02e4',  # ADD AH,AH
    '00fc',  # ADD AH,BH
    '02e7',  # ADD AH,BH
    '00ec',  # ADD AH,CH
    '02e5',  # ADD AH,CH
    '00f4',  # ADD AH,DH
    '02e6',  # ADD AH,DH
    '00e7',  # ADD BH,AH
    '02fc',  # ADD BH,AH
    '00ff',  # ADD BH,BH
    '02ff',  # ADD BH,BH
    '00ef',  # ADD BH,CH
    '02fd',  # ADD BH,CH
    '00f7',  # ADD BH,DH
    '02fe',  # ADD BH,DH
    '00e5',  # ADD CH,AH
    '02ec',  # ADD CH,AH
    '00fd',  # ADD CH,BH
    '02ef',  # ADD CH,BH
    '00ed',  # ADD CH,CH
    '02ed',  # ADD CH,CH
    '00f5',  # ADD CH,DH
    '02ee',  # ADD CH,DH
    '00e6',  # ADD DH,AH
    '02f4',  # ADD DH,AH
    '00fe',  # ADD DH,BH
    '02f7',  # ADD DH,BH
    '00ee',  # ADD DH,CH
    '02f5',  # ADD DH,CH
    '00f6',  # ADD DH,DH
    '02f6',  # ADD DH,DH
    '00c0',  # ADD AL,AL
    '02c0',  # ADD AL,AL
    '00d8',  # ADD AL,BL
    '02c3',  # ADD AL,BL
    '00c8',  # ADD AL,CL
    '02c1',  # ADD AL,CL
    '00d0',  # ADD AL,DL
    '02c2',  # ADD AL,DL
    '00c3',  # ADD BL,AL
    '02d8',  # ADD BL,AL
    '00db',  # ADD BL,BL
    '02db',  # ADD BL,BL
    '00cb',  # ADD BL,CL
    '02d9',  # ADD BL,CL
    '00d3',  # ADD BL,DL
    '02da',  # ADD BL,DL
    '00c1',  # ADD CL,AL
    '02c8',  # ADD CL,AL
    '00d9',  # ADD CL,BL
    '02cb',  # ADD CL,BL
    '00c9',  # ADD CL,CL
    '02c9',  # ADD CL,CL
    '00d1',  # ADD CL,DL
    '02ca',  # ADD CL,DL
    '00c2',  # ADD DL,AL
    '02d0',  # ADD DL,AL
    '00da',  # ADD DL,BL
    '02d3',  # ADD DL,BL
    '00ca',  # ADD DL,CL
    '02d1',  # ADD DL,CL
    '00d2',  # ADD DL,DL
    '02d2',  # ADD DL,DL
    '11c0',  # ADC EAX,EAX
    '13c0',  # ADC EAX,EAX
    '11d8',  # ADC EAX,EBX
    '13c3',  # ADC EAX,EBX
    '11c8',  # ADC EAX,ECX
    '13c1',  # ADC EAX,ECX
    '11d0',  # ADC EAX,EDX
    '13c2',  # ADC EAX,EDX
    '11e0',  # ADC EAX,ESP
    '13c4',  # ADC EAX,ESP
    '11e8',  # ADC EAX,EBP
    '13c5',  # ADC EAX,EBP
    '11f0',  # ADC EAX,ESI
    '13c6',  # ADC EAX,ESI
    '11f8',  # ADC EAX,EDI
    '13c7',  # ADC EAX,EDI
    '11c3',  # ADC EBX,EAX
    '13d8',  # ADC EBX,EAX
    '11db',  # ADC EBX,EBX
    '13db',  # ADC EBX,EBX
    '11cb',  # ADC EBX,ECX
    '13d9',  # ADC EBX,ECX
    '11d3',  # ADC EBX,EDX
    '13da',  # ADC EBX,EDX
    '11e3',  # ADC EBX,ESP
    '13dc',  # ADC EBX,ESP
    '11eb',  # ADC EBX,EBP
    '13dd',  # ADC EBX,EBP
    '11f3',  # ADC EBX,ESI
    '13de',  # ADC EBX,ESI
    '11fb',  # ADC EBX,EDI
    '13df',  # ADC EBX,EDI
    '11c1',  # ADC ECX,EAX
    '13c8',  # ADC ECX,EAX
    '11d9',  # ADC ECX,EBX
    '13cb',  # ADC ECX,EBX
    '11c9',  # ADC ECX,ECX
    '13c9',  # ADC ECX,ECX
    '11d1',  # ADC ECX,EDX
    '13ca',  # ADC ECX,EDX
    '11e1',  # ADC ECX,ESP
    '13cc',  # ADC ECX,ESP
    '11e9',  # ADC ECX,EBP
    '13cd',  # ADC ECX,EBP
    '11f1',  # ADC ECX,ESI
    '13ce',  # ADC ECX,ESI
    '11f9',  # ADC ECX,EDI
    '13cf',  # ADC ECX,EDI
    '11c2',  # ADC EDX,EAX
    '13d0',  # ADC EDX,EAX
    '11da',  # ADC EDX,EBX
    '13d3',  # ADC EDX,EBX
    '11ca',  # ADC EDX,ECX
    '13d1',  # ADC EDX,ECX
    '11d2',  # ADC EDX,EDX
    '13d2',  # ADC EDX,EDX
    '11e2',  # ADC EDX,ESP
    '13d4',  # ADC EDX,ESP
    '11ea',  # ADC EDX,EBP
    '13d5',  # ADC EDX,EBP
    '11f2',  # ADC EDX,ESI
    '13d6',  # ADC EDX,ESI
    '11fa',  # ADC EDX,EDI
    '13d7',  # ADC EDX,EDI
    '11c4',  # ADC ESP,EAX
    '13e0',  # ADC ESP,EAX
    '11dc',  # ADC ESP,EBX
    '13e3',  # ADC ESP,EBX
    '11cc',  # ADC ESP,ECX
    '13e1',  # ADC ESP,ECX
    '11d4',  # ADC ESP,EDX
    '13e2',  # ADC ESP,EDX
    '11e4',  # ADC ESP,ESP
    '13e4',  # ADC ESP,ESP
    '11ec',  # ADC ESP,EBP
    '13e5',  # ADC ESP,EBP
    '11f4',  # ADC ESP,ESI
    '13e6',  # ADC ESP,ESI
    '11fc',  # ADC ESP,EDI
    '13e7',  # ADC ESP,EDI
    '11c5',  # ADC EBP,EAX
    '13e8',  # ADC EBP,EAX
    '11dd',  # ADC EBP,EBX
    '13eb',  # ADC EBP,EBX
    '11cd',  # ADC EBP,ECX
    '13e9',  # ADC EBP,ECX
    '11d5',  # ADC EBP,EDX
    '13ea',  # ADC EBP,EDX
    '11e5',  # ADC EBP,ESP
    '13ec',  # ADC EBP,ESP
    '11ed',  # ADC EBP,EBP
    '13ed',  # ADC EBP,EBP
    '11f5',  # ADC EBP,ESI
    '13ee',  # ADC EBP,ESI
    '11fd',  # ADC EBP,EDI
    '13ef',  # ADC EBP,EDI
    '11c6',  # ADC ESI,EAX
    '13f0',  # ADC ESI,EAX
    '11de',  # ADC ESI,EBX
    '13f3',  # ADC ESI,EBX
    '11ce',  # ADC ESI,ECX
    '13f1',  # ADC ESI,ECX
    '11d6',  # ADC ESI,EDX
    '13f2',  # ADC ESI,EDX
    '11e6',  # ADC ESI,ESP
    '13f4',  # ADC ESI,ESP
    '11ee',  # ADC ESI,EBP
    '13f5',  # ADC ESI,EBP
    '11f6',  # ADC ESI,ESI
    '13f6',  # ADC ESI,ESI
    '11fe',  # ADC ESI,EDI
    '13f7',  # ADC ESI,EDI
    '11c7',  # ADC EDI,EAX
    '13f8',  # ADC EDI,EAX
    '11df',  # ADC EDI,EBX
    '13fb',  # ADC EDI,EBX
    '11cf',  # ADC EDI,ECX
    '13f9',  # ADC EDI,ECX
    '11d7',  # ADC EDI,EDX
    '13fa',  # ADC EDI,EDX
    '11e7',  # ADC EDI,ESP
    '13fc',  # ADC EDI,ESP
    '11ef',  # ADC EDI,EBP
    '13fd',  # ADC EDI,EBP
    '11f7',  # ADC EDI,ESI
    '13fe',  # ADC EDI,ESI
    '11ff',  # ADC EDI,EDI
    '13ff',  # ADC EDI,EDI
    '10e4',  # ADC AH,AH
    '12e4',  # ADC AH,AH
    '10fc',  # ADC AH,BH
    '12e7',  # ADC AH,BH
    '10ec',  # ADC AH,CH
    '12e5',  # ADC AH,CH
    '10f4',  # ADC AH,DH
    '12e6',  # ADC AH,DH
    '10e7',  # ADC BH,AH
    '12fc',  # ADC BH,AH
    '10ff',  # ADC BH,BH
    '12ff',  # ADC BH,BH
    '10ef',  # ADC BH,CH
    '12fd',  # ADC BH,CH
    '10f7',  # ADC BH,DH
    '12fe',  # ADC BH,DH
    '10e5',  # ADC CH,AH
    '12ec',  # ADC CH,AH
    '10fd',  # ADC CH,BH
    '12ef',  # ADC CH,BH
    '10ed',  # ADC CH,CH
    '12ed',  # ADC CH,CH
    '10f5',  # ADC CH,DH
    '12ee',  # ADC CH,DH
    '10e6',  # ADC DH,AH
    '12f4',  # ADC DH,AH
    '10fe',  # ADC DH,BH
    '12f7',  # ADC DH,BH
    '10ee',  # ADC DH,CH
    '12f5',  # ADC DH,CH
    '10f6',  # ADC DH,DH
    '12f6',  # ADC DH,DH
    '10c0',  # ADC AL,AL
    '12c0',  # ADC AL,AL
    '10d8',  # ADC AL,BL
    '12c3',  # ADC AL,BL
    '10c8',  # ADC AL,CL
    '12c1',  # ADC AL,CL
    '10d0',  # ADC AL,DL
    '12c2',  # ADC AL,DL
    '10c3',  # ADC BL,AL
    '12d8',  # ADC BL,AL
    '10db',  # ADC BL,BL
    '12db',  # ADC BL,BL
    '10cb',  # ADC BL,CL
    '12d9',  # ADC BL,CL
    '10d3',  # ADC BL,DL
    '12da',  # ADC BL,DL
    '10c1',  # ADC CL,AL
    '12c8',  # ADC CL,AL
    '10d9',  # ADC CL,BL
    '12cb',  # ADC CL,BL
    '10c9',  # ADC CL,CL
    '12c9',  # ADC CL,CL
    '10d1',  # ADC CL,DL
    '12ca',  # ADC CL,DL
    '10c2',  # ADC DL,AL
    '12d0',  # ADC DL,AL
    '10da',  # ADC DL,BL
    '12d3',  # ADC DL,BL
    '10ca',  # ADC DL,CL
    '12d1',  # ADC DL,CL
    '10d2',  # ADC DL,DL
    '12d2',  # ADC DL,DL
    '21c0',  # AND EAX,EAX
    '23c0',  # AND EAX,EAX
    '21d8',  # AND EAX,EBX
    '23c3',  # AND EAX,EBX
    '21c8',  # AND EAX,ECX
    '23c1',  # AND EAX,ECX
    '21d0',  # AND EAX,EDX
    '23c2',  # AND EAX,EDX
    '21e0',  # AND EAX,ESP
    '23c4',  # AND EAX,ESP
    '21e8',  # AND EAX,EBP
    '23c5',  # AND EAX,EBP
    '21f0',  # AND EAX,ESI
    '23c6',  # AND EAX,ESI
    '21f8',  # AND EAX,EDI
    '23c7',  # AND EAX,EDI
    '21c3',  # AND EBX,EAX
    '23d8',  # AND EBX,EAX
    '21db',  # AND EBX,EBX
    '23db',  # AND EBX,EBX
    '21cb',  # AND EBX,ECX
    '23d9',  # AND EBX,ECX
    '21d3',  # AND EBX,EDX
    '23da',  # AND EBX,EDX
    '21e3',  # AND EBX,ESP
    '23dc',  # AND EBX,ESP
    '21eb',  # AND EBX,EBP
    '23dd',  # AND EBX,EBP
    '21f3',  # AND EBX,ESI
    '23de',  # AND EBX,ESI
    '21fb',  # AND EBX,EDI
    '23df',  # AND EBX,EDI
    '21c1',  # AND ECX,EAX
    '23c8',  # AND ECX,EAX
    '21d9',  # AND ECX,EBX
    '23cb',  # AND ECX,EBX
    '21c9',  # AND ECX,ECX
    '23c9',  # AND ECX,ECX
    '21d1',  # AND ECX,EDX
    '23ca',  # AND ECX,EDX
    '21e1',  # AND ECX,ESP
    '23cc',  # AND ECX,ESP
    '21e9',  # AND ECX,EBP
    '23cd',  # AND ECX,EBP
    '21f1',  # AND ECX,ESI
    '23ce',  # AND ECX,ESI
    '21f9',  # AND ECX,EDI
    '23cf',  # AND ECX,EDI
    '21c2',  # AND EDX,EAX
    '23d0',  # AND EDX,EAX
    '21da',  # AND EDX,EBX
    '23d3',  # AND EDX,EBX
    '21ca',  # AND EDX,ECX
    '23d1',  # AND EDX,ECX
    '21d2',  # AND EDX,EDX
    '23d2',  # AND EDX,EDX
    '21e2',  # AND EDX,ESP
    '23d4',  # AND EDX,ESP
    '21ea',  # AND EDX,EBP
    '23d5',  # AND EDX,EBP
    '21f2',  # AND EDX,ESI
    '23d6',  # AND EDX,ESI
    '21fa',  # AND EDX,EDI
    '23d7',  # AND EDX,EDI
    '21c4',  # AND ESP,EAX
    '23e0',  # AND ESP,EAX
    '21dc',  # AND ESP,EBX
    '23e3',  # AND ESP,EBX
    '21cc',  # AND ESP,ECX
    '23e1',  # AND ESP,ECX
    '21d4',  # AND ESP,EDX
    '23e2',  # AND ESP,EDX
    '21e4',  # AND ESP,ESP
    '23e4',  # AND ESP,ESP
    '21ec',  # AND ESP,EBP
    '23e5',  # AND ESP,EBP
    '21f4',  # AND ESP,ESI
    '23e6',  # AND ESP,ESI
    '21fc',  # AND ESP,EDI
    '23e7',  # AND ESP,EDI
    '21c5',  # AND EBP,EAX
    '23e8',  # AND EBP,EAX
    '21dd',  # AND EBP,EBX
    '23eb',  # AND EBP,EBX
    '21cd',  # AND EBP,ECX
    '23e9',  # AND EBP,ECX
    '21d5',  # AND EBP,EDX
    '23ea',  # AND EBP,EDX
    '21e5',  # AND EBP,ESP
    '23ec',  # AND EBP,ESP
    '21ed',  # AND EBP,EBP
    '23ed',  # AND EBP,EBP
    '21f5',  # AND EBP,ESI
    '23ee',  # AND EBP,ESI
    '21fd',  # AND EBP,EDI
    '23ef',  # AND EBP,EDI
    '21c6',  # AND ESI,EAX
    '23f0',  # AND ESI,EAX
    '21de',  # AND ESI,EBX
    '23f3',  # AND ESI,EBX
    '21ce',  # AND ESI,ECX
    '23f1',  # AND ESI,ECX
    '21d6',  # AND ESI,EDX
    '23f2',  # AND ESI,EDX
    '21e6',  # AND ESI,ESP
    '23f4',  # AND ESI,ESP
    '21ee',  # AND ESI,EBP
    '23f5',  # AND ESI,EBP
    '21f6',  # AND ESI,ESI
    '23f6',  # AND ESI,ESI
    '21fe',  # AND ESI,EDI
    '23f7',  # AND ESI,EDI
    '21c7',  # AND EDI,EAX
    '23f8',  # AND EDI,EAX
    '21df',  # AND EDI,EBX
    '23fb',  # AND EDI,EBX
    '21cf',  # AND EDI,ECX
    '23f9',  # AND EDI,ECX
    '21d7',  # AND EDI,EDX
    '23fa',  # AND EDI,EDX
    '21e7',  # AND EDI,ESP
    '23fc',  # AND EDI,ESP
    '21ef',  # AND EDI,EBP
    '23fd',  # AND EDI,EBP
    '21f7',  # AND EDI,ESI
    '23fe',  # AND EDI,ESI
    '21ff',  # AND EDI,EDI
    '23ff',  # AND EDI,EDI
    '20e4',  # AND AH,AH
    '22e4',  # AND AH,AH
    '20fc',  # AND AH,BH
    '22e7',  # AND AH,BH
    '20ec',  # AND AH,CH
    '22e5',  # AND AH,CH
    '20f4',  # AND AH,DH
    '22e6',  # AND AH,DH
    '20e7',  # AND BH,AH
    '22fc',  # AND BH,AH
    '20ff',  # AND BH,BH
    '22ff',  # AND BH,BH
    '20ef',  # AND BH,CH
    '22fd',  # AND BH,CH
    '20f7',  # AND BH,DH
    '22fe',  # AND BH,DH
    '20e5',  # AND CH,AH
    '22ec',  # AND CH,AH
    '20fd',  # AND CH,BH
    '22ef',  # AND CH,BH
    '20ed',  # AND CH,CH
    '22ed',  # AND CH,CH
    '20f5',  # AND CH,DH
    '22ee',  # AND CH,DH
    '20e6',  # AND DH,AH
    '22f4',  # AND DH,AH
    '20fe',  # AND DH,BH
    '22f7',  # AND DH,BH
    '20ee',  # AND DH,CH
    '22f5',  # AND DH,CH
    '20f6',  # AND DH,DH
    '22f6',  # AND DH,DH
    '20c0',  # AND AL,AL
    '22c0',  # AND AL,AL
    '20d8',  # AND AL,BL
    '22c3',  # AND AL,BL
    '20c8',  # AND AL,CL
    '22c1',  # AND AL,CL
    '20d0',  # AND AL,DL
    '22c2',  # AND AL,DL
    '20c3',  # AND BL,AL
    '22d8',  # AND BL,AL
    '20db',  # AND BL,BL
    '22db',  # AND BL,BL
    '20cb',  # AND BL,CL
    '22d9',  # AND BL,CL
    '20d3',  # AND BL,DL
    '22da',  # AND BL,DL
    '20c1',  # AND CL,AL
    '22c8',  # AND CL,AL
    '20d9',  # AND CL,BL
    '22cb',  # AND CL,BL
    '20c9',  # AND CL,CL
    '22c9',  # AND CL,CL
    '20d1',  # AND CL,DL
    '22ca',  # AND CL,DL
    '20c2',  # AND DL,AL
    '22d0',  # AND DL,AL
    '20da',  # AND DL,BL
    '22d3',  # AND DL,BL
    '20ca',  # AND DL,CL
    '22d1',  # AND DL,CL
    '20d2',  # AND DL,DL
    '22d2',  # AND DL,DL
    '09c0',  # OR EAX,EAX
    '0bc0',  # OR EAX,EAX
    '09d8',  # OR EAX,EBX
    '0bc3',  # OR EAX,EBX
    '09c8',  # OR EAX,ECX
    '0bc1',  # OR EAX,ECX
    '09d0',  # OR EAX,EDX
    '0bc2',  # OR EAX,EDX
    '09e0',  # OR EAX,ESP
    '0bc4',  # OR EAX,ESP
    '09e8',  # OR EAX,EBP
    '0bc5',  # OR EAX,EBP
    '09f0',  # OR EAX,ESI
    '0bc6',  # OR EAX,ESI
    '09f8',  # OR EAX,EDI
    '0bc7',  # OR EAX,EDI
    '09c3',  # OR EBX,EAX
    '0bd8',  # OR EBX,EAX
    '09db',  # OR EBX,EBX
    '0bdb',  # OR EBX,EBX
    '09cb',  # OR EBX,ECX
    '0bd9',  # OR EBX,ECX
    '09d3',  # OR EBX,EDX
    '0bda',  # OR EBX,EDX
    '09e3',  # OR EBX,ESP
    '0bdc',  # OR EBX,ESP
    '09eb',  # OR EBX,EBP
    '0bdd',  # OR EBX,EBP
    '09f3',  # OR EBX,ESI
    '0bde',  # OR EBX,ESI
    '09fb',  # OR EBX,EDI
    '0bdf',  # OR EBX,EDI
    '09c1',  # OR ECX,EAX
    '0bc8',  # OR ECX,EAX
    '09d9',  # OR ECX,EBX
    '0bcb',  # OR ECX,EBX
    '09c9',  # OR ECX,ECX
    '0bc9',  # OR ECX,ECX
    '09d1',  # OR ECX,EDX
    '0bca',  # OR ECX,EDX
    '09e1',  # OR ECX,ESP
    '0bcc',  # OR ECX,ESP
    '09e9',  # OR ECX,EBP
    '0bcd',  # OR ECX,EBP
    '09f1',  # OR ECX,ESI
    '0bce',  # OR ECX,ESI
    '09f9',  # OR ECX,EDI
    '0bcf',  # OR ECX,EDI
    '09c2',  # OR EDX,EAX
    '0bd0',  # OR EDX,EAX
    '09da',  # OR EDX,EBX
    '0bd3',  # OR EDX,EBX
    '09ca',  # OR EDX,ECX
    '0bd1',  # OR EDX,ECX
    '09d2',  # OR EDX,EDX
    '0bd2',  # OR EDX,EDX
    '09e2',  # OR EDX,ESP
    '0bd4',  # OR EDX,ESP
    '09ea',  # OR EDX,EBP
    '0bd5',  # OR EDX,EBP
    '09f2',  # OR EDX,ESI
    '0bd6',  # OR EDX,ESI
    '09fa',  # OR EDX,EDI
    '0bd7',  # OR EDX,EDI
    '09c4',  # OR ESP,EAX
    '0be0',  # OR ESP,EAX
    '09dc',  # OR ESP,EBX
    '0be3',  # OR ESP,EBX
    '09cc',  # OR ESP,ECX
    '0be1',  # OR ESP,ECX
    '09d4',  # OR ESP,EDX
    '0be2',  # OR ESP,EDX
    '09e4',  # OR ESP,ESP
    '0be4',  # OR ESP,ESP
    '09ec',  # OR ESP,EBP
    '0be5',  # OR ESP,EBP
    '09f4',  # OR ESP,ESI
    '0be6',  # OR ESP,ESI
    '09fc',  # OR ESP,EDI
    '0be7',  # OR ESP,EDI
    '09c5',  # OR EBP,EAX
    '0be8',  # OR EBP,EAX
    '09dd',  # OR EBP,EBX
    '0beb',  # OR EBP,EBX
    '09cd',  # OR EBP,ECX
    '0be9',  # OR EBP,ECX
    '09d5',  # OR EBP,EDX
    '0bea',  # OR EBP,EDX
    '09e5',  # OR EBP,ESP
    '0bec',  # OR EBP,ESP
    '09ed',  # OR EBP,EBP
    '0bed',  # OR EBP,EBP
    '09f5',  # OR EBP,ESI
    '0bee',  # OR EBP,ESI
    '09fd',  # OR EBP,EDI
    '0bef',  # OR EBP,EDI
    '09c6',  # OR ESI,EAX
    '0bf0',  # OR ESI,EAX
    '09de',  # OR ESI,EBX
    '0bf3',  # OR ESI,EBX
    '09ce',  # OR ESI,ECX
    '0bf1',  # OR ESI,ECX
    '09d6',  # OR ESI,EDX
    '0bf2',  # OR ESI,EDX
    '09e6',  # OR ESI,ESP
    '0bf4',  # OR ESI,ESP
    '09ee',  # OR ESI,EBP
    '0bf5',  # OR ESI,EBP
    '09f6',  # OR ESI,ESI
    '0bf6',  # OR ESI,ESI
    '09fe',  # OR ESI,EDI
    '0bf7',  # OR ESI,EDI
    '09c7',  # OR EDI,EAX
    '0bf8',  # OR EDI,EAX
    '09df',  # OR EDI,EBX
    '0bfb',  # OR EDI,EBX
    '09cf',  # OR EDI,ECX
    '0bf9',  # OR EDI,ECX
    '09d7',  # OR EDI,EDX
    '0bfa',  # OR EDI,EDX
    '09e7',  # OR EDI,ESP
    '0bfc',  # OR EDI,ESP
    '09ef',  # OR EDI,EBP
    '0bfd',  # OR EDI,EBP
    '09f7',  # OR EDI,ESI
    '0bfe',  # OR EDI,ESI
    '09ff',  # OR EDI,EDI
    '0bff',  # OR EDI,EDI
    '08e4',  # OR AH,AH
    '0ae4',  # OR AH,AH
    '08fc',  # OR AH,BH
    '0ae7',  # OR AH,BH
    '08ec',  # OR AH,CH
    '0ae5',  # OR AH,CH
    '08f4',  # OR AH,DH
    '0ae6',  # OR AH,DH
    '08e7',  # OR BH,AH
    '0afc',  # OR BH,AH
    '08ff',  # OR BH,BH
    '0aff',  # OR BH,BH
    '08ef',  # OR BH,CH
    '0afd',  # OR BH,CH
    '08f7',  # OR BH,DH
    '0afe',  # OR BH,DH
    '08e5',  # OR CH,AH
    '0aec',  # OR CH,AH
    '08fd',  # OR CH,BH
    '0aef',  # OR CH,BH
    '08ed',  # OR CH,CH
    '0aed',  # OR CH,CH
    '08f5',  # OR CH,DH
    '0aee',  # OR CH,DH
    '08e6',  # OR DH,AH
    '0af4',  # OR DH,AH
    '08fe',  # OR DH,BH
    '0af7',  # OR DH,BH
    '08ee',  # OR DH,CH
    '0af5',  # OR DH,CH
    '08f6',  # OR DH,DH
    '0af6',  # OR DH,DH
    '08c0',  # OR AL,AL
    '0ac0',  # OR AL,AL
    '08d8',  # OR AL,BL
    '0ac3',  # OR AL,BL
    '08c8',  # OR AL,CL
    '0ac1',  # OR AL,CL
    '08d0',  # OR AL,DL
    '0ac2',  # OR AL,DL
    '08c3',  # OR BL,AL
    '0ad8',  # OR BL,AL
    '08db',  # OR BL,BL
    '0adb',  # OR BL,BL
    '08cb',  # OR BL,CL
    '0ad9',  # OR BL,CL
    '08d3',  # OR BL,DL
    '0ada',  # OR BL,DL
    '08c1',  # OR CL,AL
    '0ac8',  # OR CL,AL
    '08d9',  # OR CL,BL
    '0acb',  # OR CL,BL
    '08c9',  # OR CL,CL
    '0ac9',  # OR CL,CL
    '08d1',  # OR CL,DL
    '0aca',  # OR CL,DL
    '08c2',  # OR DL,AL
    '0ad0',  # OR DL,AL
    '08da',  # OR DL,BL
    '0ad3',  # OR DL,BL
    '08ca',  # OR DL,CL
    '0ad1',  # OR DL,CL
    '08d2',  # OR DL,DL
    '0ad2',  # OR DL,DL
    '19c0',  # SBB EAX,EAX
    '1bc0',  # SBB EAX,EAX
    '19d8',  # SBB EAX,EBX
    '1bc3',  # SBB EAX,EBX
    '19c8',  # SBB EAX,ECX
    '1bc1',  # SBB EAX,ECX
    '19d0',  # SBB EAX,EDX
    '1bc2',  # SBB EAX,EDX
    '19e0',  # SBB EAX,ESP
    '1bc4',  # SBB EAX,ESP
    '19e8',  # SBB EAX,EBP
    '1bc5',  # SBB EAX,EBP
    '19f0',  # SBB EAX,ESI
    '1bc6',  # SBB EAX,ESI
    '19f8',  # SBB EAX,EDI
    '1bc7',  # SBB EAX,EDI
    '19c3',  # SBB EBX,EAX
    '1bd8',  # SBB EBX,EAX
    '19db',  # SBB EBX,EBX
    '1bdb',  # SBB EBX,EBX
    '19cb',  # SBB EBX,ECX
    '1bd9',  # SBB EBX,ECX
    '19d3',  # SBB EBX,EDX
    '1bda',  # SBB EBX,EDX
    '19e3',  # SBB EBX,ESP
    '1bdc',  # SBB EBX,ESP
    '19eb',  # SBB EBX,EBP
    '1bdd',  # SBB EBX,EBP
    '19f3',  # SBB EBX,ESI
    '1bde',  # SBB EBX,ESI
    '19fb',  # SBB EBX,EDI
    '1bdf',  # SBB EBX,EDI
    '19c1',  # SBB ECX,EAX
    '1bc8',  # SBB ECX,EAX
    '19d9',  # SBB ECX,EBX
    '1bcb',  # SBB ECX,EBX
    '19c9',  # SBB ECX,ECX
    '1bc9',  # SBB ECX,ECX
    '19d1',  # SBB ECX,EDX
    '1bca',  # SBB ECX,EDX
    '19e1',  # SBB ECX,ESP
    '1bcc',  # SBB ECX,ESP
    '19e9',  # SBB ECX,EBP
    '1bcd',  # SBB ECX,EBP
    '19f1',  # SBB ECX,ESI
    '1bce',  # SBB ECX,ESI
    '19f9',  # SBB ECX,EDI
    '1bcf',  # SBB ECX,EDI
    '19c2',  # SBB EDX,EAX
    '1bd0',  # SBB EDX,EAX
    '19da',  # SBB EDX,EBX
    '1bd3',  # SBB EDX,EBX
    '19ca',  # SBB EDX,ECX
    '1bd1',  # SBB EDX,ECX
    '19d2',  # SBB EDX,EDX
    '1bd2',  # SBB EDX,EDX
    '19e2',  # SBB EDX,ESP
    '1bd4',  # SBB EDX,ESP
    '19ea',  # SBB EDX,EBP
    '1bd5',  # SBB EDX,EBP
    '19f2',  # SBB EDX,ESI
    '1bd6',  # SBB EDX,ESI
    '19fa',  # SBB EDX,EDI
    '1bd7',  # SBB EDX,EDI
    '19c4',  # SBB ESP,EAX
    '1be0',  # SBB ESP,EAX
    '19dc',  # SBB ESP,EBX
    '1be3',  # SBB ESP,EBX
    '19cc',  # SBB ESP,ECX
    '1be1',  # SBB ESP,ECX
    '19d4',  # SBB ESP,EDX
    '1be2',  # SBB ESP,EDX
    '19e4',  # SBB ESP,ESP
    '1be4',  # SBB ESP,ESP
    '19ec',  # SBB ESP,EBP
    '1be5',  # SBB ESP,EBP
    '19f4',  # SBB ESP,ESI
    '1be6',  # SBB ESP,ESI
    '19fc',  # SBB ESP,EDI
    '1be7',  # SBB ESP,EDI
    '19c5',  # SBB EBP,EAX
    '1be8',  # SBB EBP,EAX
    '19dd',  # SBB EBP,EBX
    '1beb',  # SBB EBP,EBX
    '19cd',  # SBB EBP,ECX
    '1be9',  # SBB EBP,ECX
    '19d5',  # SBB EBP,EDX
    '1bea',  # SBB EBP,EDX
    '19e5',  # SBB EBP,ESP
    '1bec',  # SBB EBP,ESP
    '19ed',  # SBB EBP,EBP
    '1bed',  # SBB EBP,EBP
    '19f5',  # SBB EBP,ESI
    '1bee',  # SBB EBP,ESI
    '19fd',  # SBB EBP,EDI
    '1bef',  # SBB EBP,EDI
    '19c6',  # SBB ESI,EAX
    '1bf0',  # SBB ESI,EAX
    '19de',  # SBB ESI,EBX
    '1bf3',  # SBB ESI,EBX
    '19ce',  # SBB ESI,ECX
    '1bf1',  # SBB ESI,ECX
    '19d6',  # SBB ESI,EDX
    '1bf2',  # SBB ESI,EDX
    '19e6',  # SBB ESI,ESP
    '1bf4',  # SBB ESI,ESP
    '19ee',  # SBB ESI,EBP
    '1bf5',  # SBB ESI,EBP
    '19f6',  # SBB ESI,ESI
    '1bf6',  # SBB ESI,ESI
    '19fe',  # SBB ESI,EDI
    '1bf7',  # SBB ESI,EDI
    '19c7',  # SBB EDI,EAX
    '1bf8',  # SBB EDI,EAX
    '19df',  # SBB EDI,EBX
    '1bfb',  # SBB EDI,EBX
    '19cf',  # SBB EDI,ECX
    '1bf9',  # SBB EDI,ECX
    '19d7',  # SBB EDI,EDX
    '1bfa',  # SBB EDI,EDX
    '19e7',  # SBB EDI,ESP
    '1bfc',  # SBB EDI,ESP
    '19ef',  # SBB EDI,EBP
    '1bfd',  # SBB EDI,EBP
    '19f7',  # SBB EDI,ESI
    '1bfe',  # SBB EDI,ESI
    '19ff',  # SBB EDI,EDI
    '1bff',  # SBB EDI,EDI
    '18e4',  # SBB AH,AH
    '1ae4',  # SBB AH,AH
    '18fc',  # SBB AH,BH
    '1ae7',  # SBB AH,BH
    '18ec',  # SBB AH,CH
    '1ae5',  # SBB AH,CH
    '18f4',  # SBB AH,DH
    '1ae6',  # SBB AH,DH
    '18e7',  # SBB BH,AH
    '1afc',  # SBB BH,AH
    '18ff',  # SBB BH,BH
    '1aff',  # SBB BH,BH
    '18ef',  # SBB BH,CH
    '1afd',  # SBB BH,CH
    '18f7',  # SBB BH,DH
    '1afe',  # SBB BH,DH
    '18e5',  # SBB CH,AH
    '1aec',  # SBB CH,AH
    '18fd',  # SBB CH,BH
    '1aef',  # SBB CH,BH
    '18ed',  # SBB CH,CH
    '1aed',  # SBB CH,CH
    '18f5',  # SBB CH,DH
    '1aee',  # SBB CH,DH
    '18e6',  # SBB DH,AH
    '1af4',  # SBB DH,AH
    '18fe',  # SBB DH,BH
    '1af7',  # SBB DH,BH
    '18ee',  # SBB DH,CH
    '1af5',  # SBB DH,CH
    '18f6',  # SBB DH,DH
    '1af6',  # SBB DH,DH
    '18c0',  # SBB AL,AL
    '1ac0',  # SBB AL,AL
    '18d8',  # SBB AL,BL
    '1ac3',  # SBB AL,BL
    '18c8',  # SBB AL,CL
    '1ac1',  # SBB AL,CL
    '18d0',  # SBB AL,DL
    '1ac2',  # SBB AL,DL
    '18c3',  # SBB BL,AL
    '1ad8',  # SBB BL,AL
    '18db',  # SBB BL,BL
    '1adb',  # SBB BL,BL
    '18cb',  # SBB BL,CL
    '1ad9',  # SBB BL,CL
    '18d3',  # SBB BL,DL
    '1ada',  # SBB BL,DL
    '18c1',  # SBB CL,AL
    '1ac8',  # SBB CL,AL
    '18d9',  # SBB CL,BL
    '1acb',  # SBB CL,BL
    '18c9',  # SBB CL,CL
    '1ac9',  # SBB CL,CL
    '18d1',  # SBB CL,DL
    '1aca',  # SBB CL,DL
    '18c2',  # SBB DL,AL
    '1ad0',  # SBB DL,AL
    '18da',  # SBB DL,BL
    '1ad3',  # SBB DL,BL
    '18ca',  # SBB DL,CL
    '1ad1',  # SBB DL,CL
    '18d2',  # SBB DL,DL
    '1ad2',  # SBB DL,DL
    '29c0',  # SUB EAX,EAX
    '2bc0',  # SUB EAX,EAX
    '29d8',  # SUB EAX,EBX
    '2bc3',  # SUB EAX,EBX
    '29c8',  # SUB EAX,ECX
    '2bc1',  # SUB EAX,ECX
    '29d0',  # SUB EAX,EDX
    '2bc2',  # SUB EAX,EDX
    '29e0',  # SUB EAX,ESP
    '2bc4',  # SUB EAX,ESP
    '29e8',  # SUB EAX,EBP
    '2bc5',  # SUB EAX,EBP
    '29f0',  # SUB EAX,ESI
    '2bc6',  # SUB EAX,ESI
    '29f8',  # SUB EAX,EDI
    '2bc7',  # SUB EAX,EDI
    '29c3',  # SUB EBX,EAX
    '2bd8',  # SUB EBX,EAX
    '29db',  # SUB EBX,EBX
    '2bdb',  # SUB EBX,EBX
    '29cb',  # SUB EBX,ECX
    '2bd9',  # SUB EBX,ECX
    '29d3',  # SUB EBX,EDX
    '2bda',  # SUB EBX,EDX
    '29e3',  # SUB EBX,ESP
    '2bdc',  # SUB EBX,ESP
    '29eb',  # SUB EBX,EBP
    '2bdd',  # SUB EBX,EBP
    '29f3',  # SUB EBX,ESI
    '2bde',  # SUB EBX,ESI
    '29fb',  # SUB EBX,EDI
    '2bdf',  # SUB EBX,EDI
    '29c1',  # SUB ECX,EAX
    '2bc8',  # SUB ECX,EAX
    '29d9',  # SUB ECX,EBX
    '2bcb',  # SUB ECX,EBX
    '29c9',  # SUB ECX,ECX
    '2bc9',  # SUB ECX,ECX
    '29d1',  # SUB ECX,EDX
    '2bca',  # SUB ECX,EDX
    '29e1',  # SUB ECX,ESP
    '2bcc',  # SUB ECX,ESP
    '29e9',  # SUB ECX,EBP
    '2bcd',  # SUB ECX,EBP
    '29f1',  # SUB ECX,ESI
    '2bce',  # SUB ECX,ESI
    '29f9',  # SUB ECX,EDI
    '2bcf',  # SUB ECX,EDI
    '29c2',  # SUB EDX,EAX
    '2bd0',  # SUB EDX,EAX
    '29da',  # SUB EDX,EBX
    '2bd3',  # SUB EDX,EBX
    '29ca',  # SUB EDX,ECX
    '2bd1',  # SUB EDX,ECX
    '29d2',  # SUB EDX,EDX
    '2bd2',  # SUB EDX,EDX
    '29e2',  # SUB EDX,ESP
    '2bd4',  # SUB EDX,ESP
    '29ea',  # SUB EDX,EBP
    '2bd5',  # SUB EDX,EBP
    '29f2',  # SUB EDX,ESI
    '2bd6',  # SUB EDX,ESI
    '29fa',  # SUB EDX,EDI
    '2bd7',  # SUB EDX,EDI
    '29c4',  # SUB ESP,EAX
    '2be0',  # SUB ESP,EAX
    '29dc',  # SUB ESP,EBX
    '2be3',  # SUB ESP,EBX
    '29cc',  # SUB ESP,ECX
    '2be1',  # SUB ESP,ECX
    '29d4',  # SUB ESP,EDX
    '2be2',  # SUB ESP,EDX
    '29e4',  # SUB ESP,ESP
    '2be4',  # SUB ESP,ESP
    '29ec',  # SUB ESP,EBP
    '2be5',  # SUB ESP,EBP
    '29f4',  # SUB ESP,ESI
    '2be6',  # SUB ESP,ESI
    '29fc',  # SUB ESP,EDI
    '2be7',  # SUB ESP,EDI
    '29c5',  # SUB EBP,EAX
    '2be8',  # SUB EBP,EAX
    '29dd',  # SUB EBP,EBX
    '2beb',  # SUB EBP,EBX
    '29cd',  # SUB EBP,ECX
    '2be9',  # SUB EBP,ECX
    '29d5',  # SUB EBP,EDX
    '2bea',  # SUB EBP,EDX
    '29e5',  # SUB EBP,ESP
    '2bec',  # SUB EBP,ESP
    '29ed',  # SUB EBP,EBP
    '2bed',  # SUB EBP,EBP
    '29f5',  # SUB EBP,ESI
    '2bee',  # SUB EBP,ESI
    '29fd',  # SUB EBP,EDI
    '2bef',  # SUB EBP,EDI
    '29c6',  # SUB ESI,EAX
    '2bf0',  # SUB ESI,EAX
    '29de',  # SUB ESI,EBX
    '2bf3',  # SUB ESI,EBX
    '29ce',  # SUB ESI,ECX
    '2bf1',  # SUB ESI,ECX
    '29d6',  # SUB ESI,EDX
    '2bf2',  # SUB ESI,EDX
    '29e6',  # SUB ESI,ESP
    '2bf4',  # SUB ESI,ESP
    '29ee',  # SUB ESI,EBP
    '2bf5',  # SUB ESI,EBP
    '29f6',  # SUB ESI,ESI
    '2bf6',  # SUB ESI,ESI
    '29fe',  # SUB ESI,EDI
    '2bf7',  # SUB ESI,EDI
    '29c7',  # SUB EDI,EAX
    '2bf8',  # SUB EDI,EAX
    '29df',  # SUB EDI,EBX
    '2bfb',  # SUB EDI,EBX
    '29cf',  # SUB EDI,ECX
    '2bf9',  # SUB EDI,ECX
    '29d7',  # SUB EDI,EDX
    '2bfa',  # SUB EDI,EDX
    '29e7',  # SUB EDI,ESP
    '2bfc',  # SUB EDI,ESP
    '29ef',  # SUB EDI,EBP
    '2bfd',  # SUB EDI,EBP
    '29f7',  # SUB EDI,ESI
    '2bfe',  # SUB EDI,ESI
    '29ff',  # SUB EDI,EDI
    '2bff',  # SUB EDI,EDI
    '28e4',  # SUB AH,AH
    '2ae4',  # SUB AH,AH
    '28fc',  # SUB AH,BH
    '2ae7',  # SUB AH,BH
    '28ec',  # SUB AH,CH
    '2ae5',  # SUB AH,CH
    '28f4',  # SUB AH,DH
    '2ae6',  # SUB AH,DH
    '28e7',  # SUB BH,AH
    '2afc',  # SUB BH,AH
    '28ff',  # SUB BH,BH
    '2aff',  # SUB BH,BH
    '28ef',  # SUB BH,CH
    '2afd',  # SUB BH,CH
    '28f7',  # SUB BH,DH
    '2afe',  # SUB BH,DH
    '28e5',  # SUB CH,AH
    '2aec',  # SUB CH,AH
    '28fd',  # SUB CH,BH
    '2aef',  # SUB CH,BH
    '28ed',  # SUB CH,CH
    '2aed',  # SUB CH,CH
    '28f5',  # SUB CH,DH
    '2aee',  # SUB CH,DH
    '28e6',  # SUB DH,AH
    '2af4',  # SUB DH,AH
    '28fe',  # SUB DH,BH
    '2af7',  # SUB DH,BH
    '28ee',  # SUB DH,CH
    '2af5',  # SUB DH,CH
    '28f6',  # SUB DH,DH
    '2af6',  # SUB DH,DH
    '28c0',  # SUB AL,AL
    '2ac0',  # SUB AL,AL
    '28d8',  # SUB AL,BL
    '2ac3',  # SUB AL,BL
    '28c8',  # SUB AL,CL
    '2ac1',  # SUB AL,CL
    '28d0',  # SUB AL,DL
    '2ac2',  # SUB AL,DL
    '28c3',  # SUB BL,AL
    '2ad8',  # SUB BL,AL
    '28db',  # SUB BL,BL
    '2adb',  # SUB BL,BL
    '28cb',  # SUB BL,CL
    '2ad9',  # SUB BL,CL
    '28d3',  # SUB BL,DL
    '2ada',  # SUB BL,DL
    '28c1',  # SUB CL,AL
    '2ac8',  # SUB CL,AL
    '28d9',  # SUB CL,BL
    '2acb',  # SUB CL,BL
    '28c9',  # SUB CL,CL
    '2ac9',  # SUB CL,CL
    '28d1',  # SUB CL,DL
    '2aca',  # SUB CL,DL
    '28c2',  # SUB DL,AL
    '2ad0',  # SUB DL,AL
    '28da',  # SUB DL,BL
    '2ad3',  # SUB DL,BL
    '28ca',  # SUB DL,CL
    '2ad1',  # SUB DL,CL
    '28d2',  # SUB DL,DL
    '2ad2',  # SUB DL,DL
    '39c0',  # CMP EAX,EAX
    '3bc0',  # CMP EAX,EAX
    '39d8',  # CMP EAX,EBX
    '3bc3',  # CMP EAX,EBX
    '39c8',  # CMP EAX,ECX
    '3bc1',  # CMP EAX,ECX
    '39d0',  # CMP EAX,EDX
    '3bc2',  # CMP EAX,EDX
    '39e0',  # CMP EAX,ESP
    '3bc4',  # CMP EAX,ESP
    '39e8',  # CMP EAX,EBP
    '3bc5',  # CMP EAX,EBP
    '39f0',  # CMP EAX,ESI
    '3bc6',  # CMP EAX,ESI
    '39f8',  # CMP EAX,EDI
    '3bc7',  # CMP EAX,EDI
    '39c3',  # CMP EBX,EAX
    '3bd8',  # CMP EBX,EAX
    '39db',  # CMP EBX,EBX
    '3bdb',  # CMP EBX,EBX
    '39cb',  # CMP EBX,ECX
    '3bd9',  # CMP EBX,ECX
    '39d3',  # CMP EBX,EDX
    '3bda',  # CMP EBX,EDX
    '39e3',  # CMP EBX,ESP
    '3bdc',  # CMP EBX,ESP
    '39eb',  # CMP EBX,EBP
    '3bdd',  # CMP EBX,EBP
    '39f3',  # CMP EBX,ESI
    '3bde',  # CMP EBX,ESI
    '39fb',  # CMP EBX,EDI
    '3bdf',  # CMP EBX,EDI
    '39c1',  # CMP ECX,EAX
    '3bc8',  # CMP ECX,EAX
    '39d9',  # CMP ECX,EBX
    '3bcb',  # CMP ECX,EBX
    '39c9',  # CMP ECX,ECX
    '3bc9',  # CMP ECX,ECX
    '39d1',  # CMP ECX,EDX
    '3bca',  # CMP ECX,EDX
    '39e1',  # CMP ECX,ESP
    '3bcc',  # CMP ECX,ESP
    '39e9',  # CMP ECX,EBP
    '3bcd',  # CMP ECX,EBP
    '39f1',  # CMP ECX,ESI
    '3bce',  # CMP ECX,ESI
    '39f9',  # CMP ECX,EDI
    '3bcf',  # CMP ECX,EDI
    '39c2',  # CMP EDX,EAX
    '3bd0',  # CMP EDX,EAX
    '39da',  # CMP EDX,EBX
    '3bd3',  # CMP EDX,EBX
    '39ca',  # CMP EDX,ECX
    '3bd1',  # CMP EDX,ECX
    '39d2',  # CMP EDX,EDX
    '3bd2',  # CMP EDX,EDX
    '39e2',  # CMP EDX,ESP
    '3bd4',  # CMP EDX,ESP
    '39ea',  # CMP EDX,EBP
    '3bd5',  # CMP EDX,EBP
    '39f2',  # CMP EDX,ESI
    '3bd6',  # CMP EDX,ESI
    '39fa',  # CMP EDX,EDI
    '3bd7',  # CMP EDX,EDI
    '39c4',  # CMP ESP,EAX
    '3be0',  # CMP ESP,EAX
    '39dc',  # CMP ESP,EBX
    '3be3',  # CMP ESP,EBX
    '39cc',  # CMP ESP,ECX
    '3be1',  # CMP ESP,ECX
    '39d4',  # CMP ESP,EDX
    '3be2',  # CMP ESP,EDX
    '39e4',  # CMP ESP,ESP
    '3be4',  # CMP ESP,ESP
    '39ec',  # CMP ESP,EBP
    '3be5',  # CMP ESP,EBP
    '39f4',  # CMP ESP,ESI
    '3be6',  # CMP ESP,ESI
    '39fc',  # CMP ESP,EDI
    '3be7',  # CMP ESP,EDI
    '39c5',  # CMP EBP,EAX
    '3be8',  # CMP EBP,EAX
    '39dd',  # CMP EBP,EBX
    '3beb',  # CMP EBP,EBX
    '39cd',  # CMP EBP,ECX
    '3be9',  # CMP EBP,ECX
    '39d5',  # CMP EBP,EDX
    '3bea',  # CMP EBP,EDX
    '39e5',  # CMP EBP,ESP
    '3bec',  # CMP EBP,ESP
    '39ed',  # CMP EBP,EBP
    '3bed',  # CMP EBP,EBP
    '39f5',  # CMP EBP,ESI
    '3bee',  # CMP EBP,ESI
    '39fd',  # CMP EBP,EDI
    '3bef',  # CMP EBP,EDI
    '39c6',  # CMP ESI,EAX
    '3bf0',  # CMP ESI,EAX
    '39de',  # CMP ESI,EBX
    '3bf3',  # CMP ESI,EBX
    '39ce',  # CMP ESI,ECX
    '3bf1',  # CMP ESI,ECX
    '39d6',  # CMP ESI,EDX
    '3bf2',  # CMP ESI,EDX
    '39e6',  # CMP ESI,ESP
    '3bf4',  # CMP ESI,ESP
    '39ee',  # CMP ESI,EBP
    '3bf5',  # CMP ESI,EBP
    '39f6',  # CMP ESI,ESI
    '3bf6',  # CMP ESI,ESI
    '39fe',  # CMP ESI,EDI
    '3bf7',  # CMP ESI,EDI
    '39c7',  # CMP EDI,EAX
    '3bf8',  # CMP EDI,EAX
    '39df',  # CMP EDI,EBX
    '3bfb',  # CMP EDI,EBX
    '39cf',  # CMP EDI,ECX
    '3bf9',  # CMP EDI,ECX
    '39d7',  # CMP EDI,EDX
    '3bfa',  # CMP EDI,EDX
    '39e7',  # CMP EDI,ESP
    '3bfc',  # CMP EDI,ESP
    '39ef',  # CMP EDI,EBP
    '3bfd',  # CMP EDI,EBP
    '39f7',  # CMP EDI,ESI
    '3bfe',  # CMP EDI,ESI
    '39ff',  # CMP EDI,EDI
    '3bff',  # CMP EDI,EDI
    '38e4',  # CMP AH,AH
    '3ae4',  # CMP AH,AH
    '38fc',  # CMP AH,BH
    '3ae7',  # CMP AH,BH
    '38ec',  # CMP AH,CH
    '3ae5',  # CMP AH,CH
    '38f4',  # CMP AH,DH
    '3ae6',  # CMP AH,DH
    '38e7',  # CMP BH,AH
    '3afc',  # CMP BH,AH
    '38ff',  # CMP BH,BH
    '3aff',  # CMP BH,BH
    '38ef',  # CMP BH,CH
    '3afd',  # CMP BH,CH
    '38f7',  # CMP BH,DH
    '3afe',  # CMP BH,DH
    '38e5',  # CMP CH,AH
    '3aec',  # CMP CH,AH
    '38fd',  # CMP CH,BH
    '3aef',  # CMP CH,BH
    '38ed',  # CMP CH,CH
    '3aed',  # CMP CH,CH
    '38f5',  # CMP CH,DH
    '3aee',  # CMP CH,DH
    '38e6',  # CMP DH,AH
    '3af4',  # CMP DH,AH
    '38fe',  # CMP DH,BH
    '3af7',  # CMP DH,BH
    '38ee',  # CMP DH,CH
    '3af5',  # CMP DH,CH
    '38f6',  # CMP DH,DH
    '3af6',  # CMP DH,DH
    '38c0',  # CMP AL,AL
    '3ac0',  # CMP AL,AL
    '38d8',  # CMP AL,BL
    '3ac3',  # CMP AL,BL
    '38c8',  # CMP AL,CL
    '3ac1',  # CMP AL,CL
    '38d0',  # CMP AL,DL
    '3ac2',  # CMP AL,DL
    '38c3',  # CMP BL,AL
    '3ad8',  # CMP BL,AL
    '38db',  # CMP BL,BL
    '3adb',  # CMP BL,BL
    '38cb',  # CMP BL,CL
    '3ad9',  # CMP BL,CL
    '38d3',  # CMP BL,DL
    '3ada',  # CMP BL,DL
    '38c1',  # CMP CL,AL
    '3ac8',  # CMP CL,AL
    '38d9',  # CMP CL,BL
    '3acb',  # CMP CL,BL
    '38c9',  # CMP CL,CL
    '3ac9',  # CMP CL,CL
    '38d1',  # CMP CL,DL
    '3aca',  # CMP CL,DL
    '38c2',  # CMP DL,AL
    '3ad0',  # CMP DL,AL
    '38da',  # CMP DL,BL
    '3ad3',  # CMP DL,BL
    '38ca',  # CMP DL,CL
    '3ad1',  # CMP DL,CL
    '38d2',  # CMP DL,DL
    '3ad2',  # CMP DL,DL
    '85d8',    # TEST EAX,EBX
    '85c3',    # TEST EAX,EBX
    '85c8',    # TEST EAX,ECX
    '85c1',    # TEST EAX,ECX
    '85d0',    # TEST EAX,EDX
    '85c2',    # TEST EAX,EDX
    '85e0',    # TEST EAX,ESP
    '85c4',    # TEST EAX,ESP
    '85e8',    # TEST EAX,EBP
    '85c5',    # TEST EAX,EBP
    '85f0',    # TEST EAX,ESI
    '85c6',    # TEST EAX,ESI
    '85f8',    # TEST EAX,EDI
    '85c7',    # TEST EAX,EDI
    '85cb',    # TEST EBX,ECX
    '85d9',    # TEST EBX,ECX
    '85d3',    # TEST EBX,EDX
    '85da',    # TEST EBX,EDX
    '85e3',    # TEST EBX,ESP
    '85dc',    # TEST EBX,ESP
    '85eb',    # TEST EBX,EBP
    '85dd',    # TEST EBX,EBP
    '85f3',    # TEST EBX,ESI
    '85de',    # TEST EBX,ESI
    '85fb',    # TEST EBX,EDI
    '85df',    # TEST EBX,EDI
    '85d1',    # TEST ECX,EDX
    '85ca',    # TEST ECX,EDX
    '85e1',    # TEST ECX,ESP
    '85cc',    # TEST ECX,ESP
    '85e9',    # TEST ECX,EBP
    '85cd',    # TEST ECX,EBP
    '85f1',    # TEST ECX,ESI
    '85ce',    # TEST ECX,ESI
    '85f9',    # TEST ECX,EDI
    '85cf',    # TEST ECX,EDI
    '85e2',    # TEST EDX,ESP
    '85d4',    # TEST EDX,ESP
    '85ea',    # TEST EDX,EBP
    '85d5',    # TEST EDX,EBP
    '85f2',    # TEST EDX,ESI
    '85d6',    # TEST EDX,ESI
    '85fa',    # TEST EDX,EDI
    '85d7',    # TEST EDX,EDI
    '85ec',    # TEST ESP,EBP
    '85e5',    # TEST ESP,EBP
    '85f4',    # TEST ESP,ESI
    '85e6',    # TEST ESP,ESI
    '85fc',    # TEST ESP,EDI
    '85e7',    # TEST ESP,EDI
    '85f5',    # TEST EBP,ESI
    '85ee',    # TEST EBP,ESI
    '85fd',    # TEST EBP,EDI
    '85ef',    # TEST EBP,EDI
    '85fe',    # TEST ESI,EDI
    '85f7',    # TEST ESI,EDI

}


decode_opcode_map_0_to_1 = \
{
    '49 192': '51 192',  # XOR EAX,EAX => same
    '49 216': '51 195',  # XOR EAX,EBX => same
    '49 200': '51 193',  # XOR EAX,ECX => same
    '49 208': '51 194',  # XOR EAX,EDX => same
    '49 224': '51 196',  # XOR EAX,ESP => same
    '49 232': '51 197',  # XOR EAX,EBP => same
    '49 240': '51 198',  # XOR EAX,ESI => same
    '49 248': '51 199',  # XOR EAX,EDI => same
    '49 195': '51 216',  # XOR EBX,EAX => same
    '49 219': '51 219',  # XOR EBX,EBX => same
    '49 203': '51 217',  # XOR EBX,ECX => same
    '49 211': '51 218',  # XOR EBX,EDX => same
    '49 227': '51 220',  # XOR EBX,ESP => same
    '49 235': '51 221',  # XOR EBX,EBP => same
    '49 243': '51 222',  # XOR EBX,ESI => same
    '49 251': '51 223',  # XOR EBX,EDI => same
    '49 193': '51 200',  # XOR ECX,EAX => same
    '49 217': '51 203',  # XOR ECX,EBX => same
    '49 201': '51 201',  # XOR ECX,ECX => same
    '49 209': '51 202',  # XOR ECX,EDX => same
    '49 225': '51 204',  # XOR ECX,ESP => same
    '49 233': '51 205',  # XOR ECX,EBP => same
    '49 241': '51 206',  # XOR ECX,ESI => same
    '49 249': '51 207',  # XOR ECX,EDI => same
    '49 194': '51 208',  # XOR EDX,EAX => same
    '49 218': '51 211',  # XOR EDX,EBX => same
    '49 202': '51 209',  # XOR EDX,ECX => same
    '49 210': '51 210',  # XOR EDX,EDX => same
    '49 226': '51 212',  # XOR EDX,ESP => same
    '49 234': '51 213',  # XOR EDX,EBP => same
    '49 242': '51 214',  # XOR EDX,ESI => same
    '49 250': '51 215',  # XOR EDX,EDI => same
    '49 196': '51 224',  # XOR ESP,EAX => same
    '49 220': '51 227',  # XOR ESP,EBX => same
    '49 204': '51 225',  # XOR ESP,ECX => same
    '49 212': '51 226',  # XOR ESP,EDX => same
    '49 228': '51 228',  # XOR ESP,ESP => same
    '49 236': '51 229',  # XOR ESP,EBP => same
    '49 244': '51 230',  # XOR ESP,ESI => same
    '49 252': '51 231',  # XOR ESP,EDI => same
    '49 197': '51 232',  # XOR EBP,EAX => same
    '49 221': '51 235',  # XOR EBP,EBX => same
    '49 205': '51 233',  # XOR EBP,ECX => same
    '49 213': '51 234',  # XOR EBP,EDX => same
    '49 229': '51 236',  # XOR EBP,ESP => same
    '49 237': '51 237',  # XOR EBP,EBP => same
    '49 245': '51 238',  # XOR EBP,ESI => same
    '49 253': '51 239',  # XOR EBP,EDI => same
    '49 198': '51 240',  # XOR ESI,EAX => same
    '49 222': '51 243',  # XOR ESI,EBX => same
    '49 206': '51 241',  # XOR ESI,ECX => same
    '49 214': '51 242',  # XOR ESI,EDX => same
    '49 230': '51 244',  # XOR ESI,ESP => same
    '49 238': '51 245',  # XOR ESI,EBP => same
    '49 246': '51 246',  # XOR ESI,ESI => same
    '49 254': '51 247',  # XOR ESI,EDI => same
    '49 199': '51 248',  # XOR EDI,EAX => same
    '49 223': '51 251',  # XOR EDI,EBX => same
    '49 207': '51 249',  # XOR EDI,ECX => same
    '49 215': '51 250',  # XOR EDI,EDX => same
    '49 231': '51 252',  # XOR EDI,ESP => same
    '49 239': '51 253',  # XOR EDI,EBP => same
    '49 247': '51 254',  # XOR EDI,ESI => same
    '49 255': '51 255',  # XOR EDI,EDI => same
    '48 228': '50 228',  # XOR AH,AH => same
    '48 252': '50 231',  # XOR AH,BH => same
    '48 236': '50 229',  # XOR AH,CH => same
    '48 244': '50 230',  # XOR AH,DH => same
    '48 231': '50 252',  # XOR BH,AH => same
    '48 255': '50 255',  # XOR BH,BH => same
    '48 239': '50 253',  # XOR BH,CH => same
    '48 247': '50 254',  # XOR BH,DH => same
    '48 229': '50 236',  # XOR CH,AH => same
    '48 253': '50 239',  # XOR CH,BH => same
    '48 237': '50 237',  # XOR CH,CH => same
    '48 245': '50 238',  # XOR CH,DH => same
    '48 230': '50 244',  # XOR DH,AH => same
    '48 254': '50 247',  # XOR DH,BH => same
    '48 238': '50 245',  # XOR DH,CH => same
    '48 246': '50 246',  # XOR DH,DH => same
    '48 192': '50 192',  # XOR AL,AL => same
    '48 216': '50 195',  # XOR AL,BL => same
    '48 200': '50 193',  # XOR AL,CL => same
    '48 208': '50 194',  # XOR AL,DL => same
    '48 195': '50 216',  # XOR BL,AL => same
    '48 219': '50 219',  # XOR BL,BL => same
    '48 203': '50 217',  # XOR BL,CL => same
    '48 211': '50 218',  # XOR BL,DL => same
    '48 193': '50 200',  # XOR CL,AL => same
    '48 217': '50 203',  # XOR CL,BL => same
    '48 201': '50 201',  # XOR CL,CL => same
    '48 209': '50 202',  # XOR CL,DL => same
    '48 194': '50 208',  # XOR DL,AL => same
    '48 218': '50 211',  # XOR DL,BL => same
    '48 202': '50 209',  # XOR DL,CL => same
    '48 210': '50 210',  # XOR DL,DL => same
    '137 192': '139 192',  # MOV EAX,EAX => same
    '137 216': '139 195',  # MOV EAX,EBX => same
    '137 200': '139 193',  # MOV EAX,ECX => same
    '137 208': '139 194',  # MOV EAX,EDX => same
    '137 224': '139 196',  # MOV EAX,ESP => same
    '137 232': '139 197',  # MOV EAX,EBP => same
    '137 240': '139 198',  # MOV EAX,ESI => same
    '137 248': '139 199',  # MOV EAX,EDI => same
    '137 195': '139 216',  # MOV EBX,EAX => same
    '137 219': '139 219',  # MOV EBX,EBX => same
    '137 203': '139 217',  # MOV EBX,ECX => same
    '137 211': '139 218',  # MOV EBX,EDX => same
    '137 227': '139 220',  # MOV EBX,ESP => same
    '137 235': '139 221',  # MOV EBX,EBP => same
    '137 243': '139 222',  # MOV EBX,ESI => same
    '137 251': '139 223',  # MOV EBX,EDI => same
    '137 193': '139 200',  # MOV ECX,EAX => same
    '137 217': '139 203',  # MOV ECX,EBX => same
    '137 201': '139 201',  # MOV ECX,ECX => same
    '137 209': '139 202',  # MOV ECX,EDX => same
    '137 225': '139 204',  # MOV ECX,ESP => same
    '137 233': '139 205',  # MOV ECX,EBP => same
    '137 241': '139 206',  # MOV ECX,ESI => same
    '137 249': '139 207',  # MOV ECX,EDI => same
    '137 194': '139 208',  # MOV EDX,EAX => same
    '137 218': '139 211',  # MOV EDX,EBX => same
    '137 202': '139 209',  # MOV EDX,ECX => same
    '137 210': '139 210',  # MOV EDX,EDX => same
    '137 226': '139 212',  # MOV EDX,ESP => same
    '137 234': '139 213',  # MOV EDX,EBP => same
    '137 242': '139 214',  # MOV EDX,ESI => same
    '137 250': '139 215',  # MOV EDX,EDI => same
    '137 196': '139 224',  # MOV ESP,EAX => same
    '137 220': '139 227',  # MOV ESP,EBX => same
    '137 204': '139 225',  # MOV ESP,ECX => same
    '137 212': '139 226',  # MOV ESP,EDX => same
    '137 228': '139 228',  # MOV ESP,ESP => same
    '137 236': '139 229',  # MOV ESP,EBP => same
    '137 244': '139 230',  # MOV ESP,ESI => same
    '137 252': '139 231',  # MOV ESP,EDI => same
    '137 197': '139 232',  # MOV EBP,EAX => same
    '137 221': '139 235',  # MOV EBP,EBX => same
    '137 205': '139 233',  # MOV EBP,ECX => same
    '137 213': '139 234',  # MOV EBP,EDX => same
    '137 229': '139 236',  # MOV EBP,ESP => same
    '137 237': '139 237',  # MOV EBP,EBP => same
    '137 245': '139 238',  # MOV EBP,ESI => same
    '137 253': '139 239',  # MOV EBP,EDI => same
    '137 198': '139 240',  # MOV ESI,EAX => same
    '137 222': '139 243',  # MOV ESI,EBX => same
    '137 206': '139 241',  # MOV ESI,ECX => same
    '137 214': '139 242',  # MOV ESI,EDX => same
    '137 230': '139 244',  # MOV ESI,ESP => same
    '137 238': '139 245',  # MOV ESI,EBP => same
    '137 246': '139 246',  # MOV ESI,ESI => same
    '137 254': '139 247',  # MOV ESI,EDI => same
    '137 199': '139 248',  # MOV EDI,EAX => same
    '137 223': '139 251',  # MOV EDI,EBX => same
    '137 207': '139 249',  # MOV EDI,ECX => same
    '137 215': '139 250',  # MOV EDI,EDX => same
    '137 231': '139 252',  # MOV EDI,ESP => same
    '137 239': '139 253',  # MOV EDI,EBP => same
    '137 247': '139 254',  # MOV EDI,ESI => same
    '137 255': '139 255',  # MOV EDI,EDI => same
    '136 228': '138 228',  # MOV AH,AH => same
    '136 252': '138 231',  # MOV AH,BH => same
    '136 236': '138 229',  # MOV AH,CH => same
    '136 244': '138 230',  # MOV AH,DH => same
    '136 231': '138 252',  # MOV BH,AH => same
    '136 255': '138 255',  # MOV BH,BH => same
    '136 239': '138 253',  # MOV BH,CH => same
    '136 247': '138 254',  # MOV BH,DH => same
    '136 229': '138 236',  # MOV CH,AH => same
    '136 253': '138 239',  # MOV CH,BH => same
    '136 237': '138 237',  # MOV CH,CH => same
    '136 245': '138 238',  # MOV CH,DH => same
    '136 230': '138 244',  # MOV DH,AH => same
    '136 254': '138 247',  # MOV DH,BH => same
    '136 238': '138 245',  # MOV DH,CH => same
    '136 246': '138 246',  # MOV DH,DH => same
    '136 192': '138 192',  # MOV AL,AL => same
    '136 216': '138 195',  # MOV AL,BL => same
    '136 200': '138 193',  # MOV AL,CL => same
    '136 208': '138 194',  # MOV AL,DL => same
    '136 195': '138 216',  # MOV BL,AL => same
    '136 219': '138 219',  # MOV BL,BL => same
    '136 203': '138 217',  # MOV BL,CL => same
    '136 211': '138 218',  # MOV BL,DL => same
    '136 193': '138 200',  # MOV CL,AL => same
    '136 217': '138 203',  # MOV CL,BL => same
    '136 201': '138 201',  # MOV CL,CL => same
    '136 209': '138 202',  # MOV CL,DL => same
    '136 194': '138 208',  # MOV DL,AL => same
    '136 218': '138 211',  # MOV DL,BL => same
    '136 202': '138 209',  # MOV DL,CL => same
    '136 210': '138 210',  # MOV DL,DL => same
    '1 192': '3 192',  # ADD EAX,EAX => same
    '1 216': '3 195',  # ADD EAX,EBX => same
    '1 200': '3 193',  # ADD EAX,ECX => same
    '1 208': '3 194',  # ADD EAX,EDX => same
    '1 224': '3 196',  # ADD EAX,ESP => same
    '1 232': '3 197',  # ADD EAX,EBP => same
    '1 240': '3 198',  # ADD EAX,ESI => same
    '1 248': '3 199',  # ADD EAX,EDI => same
    '1 195': '3 216',  # ADD EBX,EAX => same
    '1 219': '3 219',  # ADD EBX,EBX => same
    '1 203': '3 217',  # ADD EBX,ECX => same
    '1 211': '3 218',  # ADD EBX,EDX => same
    '1 227': '3 220',  # ADD EBX,ESP => same
    '1 235': '3 221',  # ADD EBX,EBP => same
    '1 243': '3 222',  # ADD EBX,ESI => same
    '1 251': '3 223',  # ADD EBX,EDI => same
    '1 193': '3 200',  # ADD ECX,EAX => same
    '1 217': '3 203',  # ADD ECX,EBX => same
    '1 201': '3 201',  # ADD ECX,ECX => same
    '1 209': '3 202',  # ADD ECX,EDX => same
    '1 225': '3 204',  # ADD ECX,ESP => same
    '1 233': '3 205',  # ADD ECX,EBP => same
    '1 241': '3 206',  # ADD ECX,ESI => same
    '1 249': '3 207',  # ADD ECX,EDI => same
    '1 194': '3 208',  # ADD EDX,EAX => same
    '1 218': '3 211',  # ADD EDX,EBX => same
    '1 202': '3 209',  # ADD EDX,ECX => same
    '1 210': '3 210',  # ADD EDX,EDX => same
    '1 226': '3 212',  # ADD EDX,ESP => same
    '1 234': '3 213',  # ADD EDX,EBP => same
    '1 242': '3 214',  # ADD EDX,ESI => same
    '1 250': '3 215',  # ADD EDX,EDI => same
    '1 196': '3 224',  # ADD ESP,EAX => same
    '1 220': '3 227',  # ADD ESP,EBX => same
    '1 204': '3 225',  # ADD ESP,ECX => same
    '1 212': '3 226',  # ADD ESP,EDX => same
    '1 228': '3 228',  # ADD ESP,ESP => same
    '1 236': '3 229',  # ADD ESP,EBP => same
    '1 244': '3 230',  # ADD ESP,ESI => same
    '1 252': '3 231',  # ADD ESP,EDI => same
    '1 197': '3 232',  # ADD EBP,EAX => same
    '1 221': '3 235',  # ADD EBP,EBX => same
    '1 205': '3 233',  # ADD EBP,ECX => same
    '1 213': '3 234',  # ADD EBP,EDX => same
    '1 229': '3 236',  # ADD EBP,ESP => same
    '1 237': '3 237',  # ADD EBP,EBP => same
    '1 245': '3 238',  # ADD EBP,ESI => same
    '1 253': '3 239',  # ADD EBP,EDI => same
    '1 198': '3 240',  # ADD ESI,EAX => same
    '1 222': '3 243',  # ADD ESI,EBX => same
    '1 206': '3 241',  # ADD ESI,ECX => same
    '1 214': '3 242',  # ADD ESI,EDX => same
    '1 230': '3 244',  # ADD ESI,ESP => same
    '1 238': '3 245',  # ADD ESI,EBP => same
    '1 246': '3 246',  # ADD ESI,ESI => same
    '1 254': '3 247',  # ADD ESI,EDI => same
    '1 199': '3 248',  # ADD EDI,EAX => same
    '1 223': '3 251',  # ADD EDI,EBX => same
    '1 207': '3 249',  # ADD EDI,ECX => same
    '1 215': '3 250',  # ADD EDI,EDX => same
    '1 231': '3 252',  # ADD EDI,ESP => same
    '1 239': '3 253',  # ADD EDI,EBP => same
    '1 247': '3 254',  # ADD EDI,ESI => same
    '1 255': '3 255',  # ADD EDI,EDI => same
    '0 228': '2 228',  # ADD AH,AH => same
    '0 252': '2 231',  # ADD AH,BH => same
    '0 236': '2 229',  # ADD AH,CH => same
    '0 244': '2 230',  # ADD AH,DH => same
    '0 231': '2 252',  # ADD BH,AH => same
    '0 255': '2 255',  # ADD BH,BH => same
    '0 239': '2 253',  # ADD BH,CH => same
    '0 247': '2 254',  # ADD BH,DH => same
    '0 229': '2 236',  # ADD CH,AH => same
    '0 253': '2 239',  # ADD CH,BH => same
    '0 237': '2 237',  # ADD CH,CH => same
    '0 245': '2 238',  # ADD CH,DH => same
    '0 230': '2 244',  # ADD DH,AH => same
    '0 254': '2 247',  # ADD DH,BH => same
    '0 238': '2 245',  # ADD DH,CH => same
    '0 246': '2 246',  # ADD DH,DH => same
    '0 192': '2 192',  # ADD AL,AL => same
    '0 216': '2 195',  # ADD AL,BL => same
    '0 200': '2 193',  # ADD AL,CL => same
    '0 208': '2 194',  # ADD AL,DL => same
    '0 195': '2 216',  # ADD BL,AL => same
    '0 219': '2 219',  # ADD BL,BL => same
    '0 203': '2 217',  # ADD BL,CL => same
    '0 211': '2 218',  # ADD BL,DL => same
    '0 193': '2 200',  # ADD CL,AL => same
    '0 217': '2 203',  # ADD CL,BL => same
    '0 201': '2 201',  # ADD CL,CL => same
    '0 209': '2 202',  # ADD CL,DL => same
    '0 194': '2 208',  # ADD DL,AL => same
    '0 218': '2 211',  # ADD DL,BL => same
    '0 202': '2 209',  # ADD DL,CL => same
    '0 210': '2 210',  # ADD DL,DL => same
    '17 192': '19 192',  # ADC EAX,EAX => same
    '17 216': '19 195',  # ADC EAX,EBX => same
    '17 200': '19 193',  # ADC EAX,ECX => same
    '17 208': '19 194',  # ADC EAX,EDX => same
    '17 224': '19 196',  # ADC EAX,ESP => same
    '17 232': '19 197',  # ADC EAX,EBP => same
    '17 240': '19 198',  # ADC EAX,ESI => same
    '17 248': '19 199',  # ADC EAX,EDI => same
    '17 195': '19 216',  # ADC EBX,EAX => same
    '17 219': '19 219',  # ADC EBX,EBX => same
    '17 203': '19 217',  # ADC EBX,ECX => same
    '17 211': '19 218',  # ADC EBX,EDX => same
    '17 227': '19 220',  # ADC EBX,ESP => same
    '17 235': '19 221',  # ADC EBX,EBP => same
    '17 243': '19 222',  # ADC EBX,ESI => same
    '17 251': '19 223',  # ADC EBX,EDI => same
    '17 193': '19 200',  # ADC ECX,EAX => same
    '17 217': '19 203',  # ADC ECX,EBX => same
    '17 201': '19 201',  # ADC ECX,ECX => same
    '17 209': '19 202',  # ADC ECX,EDX => same
    '17 225': '19 204',  # ADC ECX,ESP => same
    '17 233': '19 205',  # ADC ECX,EBP => same
    '17 241': '19 206',  # ADC ECX,ESI => same
    '17 249': '19 207',  # ADC ECX,EDI => same
    '17 194': '19 208',  # ADC EDX,EAX => same
    '17 218': '19 211',  # ADC EDX,EBX => same
    '17 202': '19 209',  # ADC EDX,ECX => same
    '17 210': '19 210',  # ADC EDX,EDX => same
    '17 226': '19 212',  # ADC EDX,ESP => same
    '17 234': '19 213',  # ADC EDX,EBP => same
    '17 242': '19 214',  # ADC EDX,ESI => same
    '17 250': '19 215',  # ADC EDX,EDI => same
    '17 196': '19 224',  # ADC ESP,EAX => same
    '17 220': '19 227',  # ADC ESP,EBX => same
    '17 204': '19 225',  # ADC ESP,ECX => same
    '17 212': '19 226',  # ADC ESP,EDX => same
    '17 228': '19 228',  # ADC ESP,ESP => same
    '17 236': '19 229',  # ADC ESP,EBP => same
    '17 244': '19 230',  # ADC ESP,ESI => same
    '17 252': '19 231',  # ADC ESP,EDI => same
    '17 197': '19 232',  # ADC EBP,EAX => same
    '17 221': '19 235',  # ADC EBP,EBX => same
    '17 205': '19 233',  # ADC EBP,ECX => same
    '17 213': '19 234',  # ADC EBP,EDX => same
    '17 229': '19 236',  # ADC EBP,ESP => same
    '17 237': '19 237',  # ADC EBP,EBP => same
    '17 245': '19 238',  # ADC EBP,ESI => same
    '17 253': '19 239',  # ADC EBP,EDI => same
    '17 198': '19 240',  # ADC ESI,EAX => same
    '17 222': '19 243',  # ADC ESI,EBX => same
    '17 206': '19 241',  # ADC ESI,ECX => same
    '17 214': '19 242',  # ADC ESI,EDX => same
    '17 230': '19 244',  # ADC ESI,ESP => same
    '17 238': '19 245',  # ADC ESI,EBP => same
    '17 246': '19 246',  # ADC ESI,ESI => same
    '17 254': '19 247',  # ADC ESI,EDI => same
    '17 199': '19 248',  # ADC EDI,EAX => same
    '17 223': '19 251',  # ADC EDI,EBX => same
    '17 207': '19 249',  # ADC EDI,ECX => same
    '17 215': '19 250',  # ADC EDI,EDX => same
    '17 231': '19 252',  # ADC EDI,ESP => same
    '17 239': '19 253',  # ADC EDI,EBP => same
    '17 247': '19 254',  # ADC EDI,ESI => same
    '17 255': '19 255',  # ADC EDI,EDI => same
    '16 228': '18 228',  # ADC AH,AH => same
    '16 252': '18 231',  # ADC AH,BH => same
    '16 236': '18 229',  # ADC AH,CH => same
    '16 244': '18 230',  # ADC AH,DH => same
    '16 231': '18 252',  # ADC BH,AH => same
    '16 255': '18 255',  # ADC BH,BH => same
    '16 239': '18 253',  # ADC BH,CH => same
    '16 247': '18 254',  # ADC BH,DH => same
    '16 229': '18 236',  # ADC CH,AH => same
    '16 253': '18 239',  # ADC CH,BH => same
    '16 237': '18 237',  # ADC CH,CH => same
    '16 245': '18 238',  # ADC CH,DH => same
    '16 230': '18 244',  # ADC DH,AH => same
    '16 254': '18 247',  # ADC DH,BH => same
    '16 238': '18 245',  # ADC DH,CH => same
    '16 246': '18 246',  # ADC DH,DH => same
    '16 192': '18 192',  # ADC AL,AL => same
    '16 216': '18 195',  # ADC AL,BL => same
    '16 200': '18 193',  # ADC AL,CL => same
    '16 208': '18 194',  # ADC AL,DL => same
    '16 195': '18 216',  # ADC BL,AL => same
    '16 219': '18 219',  # ADC BL,BL => same
    '16 203': '18 217',  # ADC BL,CL => same
    '16 211': '18 218',  # ADC BL,DL => same
    '16 193': '18 200',  # ADC CL,AL => same
    '16 217': '18 203',  # ADC CL,BL => same
    '16 201': '18 201',  # ADC CL,CL => same
    '16 209': '18 202',  # ADC CL,DL => same
    '16 194': '18 208',  # ADC DL,AL => same
    '16 218': '18 211',  # ADC DL,BL => same
    '16 202': '18 209',  # ADC DL,CL => same
    '16 210': '18 210',  # ADC DL,DL => same
    '33 192': '35 192',  # AND EAX,EAX => same
    '33 216': '35 195',  # AND EAX,EBX => same
    '33 200': '35 193',  # AND EAX,ECX => same
    '33 208': '35 194',  # AND EAX,EDX => same
    '33 224': '35 196',  # AND EAX,ESP => same
    '33 232': '35 197',  # AND EAX,EBP => same
    '33 240': '35 198',  # AND EAX,ESI => same
    '33 248': '35 199',  # AND EAX,EDI => same
    '33 195': '35 216',  # AND EBX,EAX => same
    '33 219': '35 219',  # AND EBX,EBX => same
    '33 203': '35 217',  # AND EBX,ECX => same
    '33 211': '35 218',  # AND EBX,EDX => same
    '33 227': '35 220',  # AND EBX,ESP => same
    '33 235': '35 221',  # AND EBX,EBP => same
    '33 243': '35 222',  # AND EBX,ESI => same
    '33 251': '35 223',  # AND EBX,EDI => same
    '33 193': '35 200',  # AND ECX,EAX => same
    '33 217': '35 203',  # AND ECX,EBX => same
    '33 201': '35 201',  # AND ECX,ECX => same
    '33 209': '35 202',  # AND ECX,EDX => same
    '33 225': '35 204',  # AND ECX,ESP => same
    '33 233': '35 205',  # AND ECX,EBP => same
    '33 241': '35 206',  # AND ECX,ESI => same
    '33 249': '35 207',  # AND ECX,EDI => same
    '33 194': '35 208',  # AND EDX,EAX => same
    '33 218': '35 211',  # AND EDX,EBX => same
    '33 202': '35 209',  # AND EDX,ECX => same
    '33 210': '35 210',  # AND EDX,EDX => same
    '33 226': '35 212',  # AND EDX,ESP => same
    '33 234': '35 213',  # AND EDX,EBP => same
    '33 242': '35 214',  # AND EDX,ESI => same
    '33 250': '35 215',  # AND EDX,EDI => same
    '33 196': '35 224',  # AND ESP,EAX => same
    '33 220': '35 227',  # AND ESP,EBX => same
    '33 204': '35 225',  # AND ESP,ECX => same
    '33 212': '35 226',  # AND ESP,EDX => same
    '33 228': '35 228',  # AND ESP,ESP => same
    '33 236': '35 229',  # AND ESP,EBP => same
    '33 244': '35 230',  # AND ESP,ESI => same
    '33 252': '35 231',  # AND ESP,EDI => same
    '33 197': '35 232',  # AND EBP,EAX => same
    '33 221': '35 235',  # AND EBP,EBX => same
    '33 205': '35 233',  # AND EBP,ECX => same
    '33 213': '35 234',  # AND EBP,EDX => same
    '33 229': '35 236',  # AND EBP,ESP => same
    '33 237': '35 237',  # AND EBP,EBP => same
    '33 245': '35 238',  # AND EBP,ESI => same
    '33 253': '35 239',  # AND EBP,EDI => same
    '33 198': '35 240',  # AND ESI,EAX => same
    '33 222': '35 243',  # AND ESI,EBX => same
    '33 206': '35 241',  # AND ESI,ECX => same
    '33 214': '35 242',  # AND ESI,EDX => same
    '33 230': '35 244',  # AND ESI,ESP => same
    '33 238': '35 245',  # AND ESI,EBP => same
    '33 246': '35 246',  # AND ESI,ESI => same
    '33 254': '35 247',  # AND ESI,EDI => same
    '33 199': '35 248',  # AND EDI,EAX => same
    '33 223': '35 251',  # AND EDI,EBX => same
    '33 207': '35 249',  # AND EDI,ECX => same
    '33 215': '35 250',  # AND EDI,EDX => same
    '33 231': '35 252',  # AND EDI,ESP => same
    '33 239': '35 253',  # AND EDI,EBP => same
    '33 247': '35 254',  # AND EDI,ESI => same
    '33 255': '35 255',  # AND EDI,EDI => same
    '32 228': '34 228',  # AND AH,AH => same
    '32 252': '34 231',  # AND AH,BH => same
    '32 236': '34 229',  # AND AH,CH => same
    '32 244': '34 230',  # AND AH,DH => same
    '32 231': '34 252',  # AND BH,AH => same
    '32 255': '34 255',  # AND BH,BH => same
    '32 239': '34 253',  # AND BH,CH => same
    '32 247': '34 254',  # AND BH,DH => same
    '32 229': '34 236',  # AND CH,AH => same
    '32 253': '34 239',  # AND CH,BH => same
    '32 237': '34 237',  # AND CH,CH => same
    '32 245': '34 238',  # AND CH,DH => same
    '32 230': '34 244',  # AND DH,AH => same
    '32 254': '34 247',  # AND DH,BH => same
    '32 238': '34 245',  # AND DH,CH => same
    '32 246': '34 246',  # AND DH,DH => same
    '32 192': '34 192',  # AND AL,AL => same
    '32 216': '34 195',  # AND AL,BL => same
    '32 200': '34 193',  # AND AL,CL => same
    '32 208': '34 194',  # AND AL,DL => same
    '32 195': '34 216',  # AND BL,AL => same
    '32 219': '34 219',  # AND BL,BL => same
    '32 203': '34 217',  # AND BL,CL => same
    '32 211': '34 218',  # AND BL,DL => same
    '32 193': '34 200',  # AND CL,AL => same
    '32 217': '34 203',  # AND CL,BL => same
    '32 201': '34 201',  # AND CL,CL => same
    '32 209': '34 202',  # AND CL,DL => same
    '32 194': '34 208',  # AND DL,AL => same
    '32 218': '34 211',  # AND DL,BL => same
    '32 202': '34 209',  # AND DL,CL => same
    '32 210': '34 210',  # AND DL,DL => same
    '9 192': '11 192',  # OR EAX,EAX => same
    '9 216': '11 195',  # OR EAX,EBX => same
    '9 200': '11 193',  # OR EAX,ECX => same
    '9 208': '11 194',  # OR EAX,EDX => same
    '9 224': '11 196',  # OR EAX,ESP => same
    '9 232': '11 197',  # OR EAX,EBP => same
    '9 240': '11 198',  # OR EAX,ESI => same
    '9 248': '11 199',  # OR EAX,EDI => same
    '9 195': '11 216',  # OR EBX,EAX => same
    '9 219': '11 219',  # OR EBX,EBX => same
    '9 203': '11 217',  # OR EBX,ECX => same
    '9 211': '11 218',  # OR EBX,EDX => same
    '9 227': '11 220',  # OR EBX,ESP => same
    '9 235': '11 221',  # OR EBX,EBP => same
    '9 243': '11 222',  # OR EBX,ESI => same
    '9 251': '11 223',  # OR EBX,EDI => same
    '9 193': '11 200',  # OR ECX,EAX => same
    '9 217': '11 203',  # OR ECX,EBX => same
    '9 201': '11 201',  # OR ECX,ECX => same
    '9 209': '11 202',  # OR ECX,EDX => same
    '9 225': '11 204',  # OR ECX,ESP => same
    '9 233': '11 205',  # OR ECX,EBP => same
    '9 241': '11 206',  # OR ECX,ESI => same
    '9 249': '11 207',  # OR ECX,EDI => same
    '9 194': '11 208',  # OR EDX,EAX => same
    '9 218': '11 211',  # OR EDX,EBX => same
    '9 202': '11 209',  # OR EDX,ECX => same
    '9 210': '11 210',  # OR EDX,EDX => same
    '9 226': '11 212',  # OR EDX,ESP => same
    '9 234': '11 213',  # OR EDX,EBP => same
    '9 242': '11 214',  # OR EDX,ESI => same
    '9 250': '11 215',  # OR EDX,EDI => same
    '9 196': '11 224',  # OR ESP,EAX => same
    '9 220': '11 227',  # OR ESP,EBX => same
    '9 204': '11 225',  # OR ESP,ECX => same
    '9 212': '11 226',  # OR ESP,EDX => same
    '9 228': '11 228',  # OR ESP,ESP => same
    '9 236': '11 229',  # OR ESP,EBP => same
    '9 244': '11 230',  # OR ESP,ESI => same
    '9 252': '11 231',  # OR ESP,EDI => same
    '9 197': '11 232',  # OR EBP,EAX => same
    '9 221': '11 235',  # OR EBP,EBX => same
    '9 205': '11 233',  # OR EBP,ECX => same
    '9 213': '11 234',  # OR EBP,EDX => same
    '9 229': '11 236',  # OR EBP,ESP => same
    '9 237': '11 237',  # OR EBP,EBP => same
    '9 245': '11 238',  # OR EBP,ESI => same
    '9 253': '11 239',  # OR EBP,EDI => same
    '9 198': '11 240',  # OR ESI,EAX => same
    '9 222': '11 243',  # OR ESI,EBX => same
    '9 206': '11 241',  # OR ESI,ECX => same
    '9 214': '11 242',  # OR ESI,EDX => same
    '9 230': '11 244',  # OR ESI,ESP => same
    '9 238': '11 245',  # OR ESI,EBP => same
    '9 246': '11 246',  # OR ESI,ESI => same
    '9 254': '11 247',  # OR ESI,EDI => same
    '9 199': '11 248',  # OR EDI,EAX => same
    '9 223': '11 251',  # OR EDI,EBX => same
    '9 207': '11 249',  # OR EDI,ECX => same
    '9 215': '11 250',  # OR EDI,EDX => same
    '9 231': '11 252',  # OR EDI,ESP => same
    '9 239': '11 253',  # OR EDI,EBP => same
    '9 247': '11 254',  # OR EDI,ESI => same
    '9 255': '11 255',  # OR EDI,EDI => same
    '8 228': '10 228',  # OR AH,AH => same
    '8 252': '10 231',  # OR AH,BH => same
    '8 236': '10 229',  # OR AH,CH => same
    '8 244': '10 230',  # OR AH,DH => same
    '8 231': '10 252',  # OR BH,AH => same
    '8 255': '10 255',  # OR BH,BH => same
    '8 239': '10 253',  # OR BH,CH => same
    '8 247': '10 254',  # OR BH,DH => same
    '8 229': '10 236',  # OR CH,AH => same
    '8 253': '10 239',  # OR CH,BH => same
    '8 237': '10 237',  # OR CH,CH => same
    '8 245': '10 238',  # OR CH,DH => same
    '8 230': '10 244',  # OR DH,AH => same
    '8 254': '10 247',  # OR DH,BH => same
    '8 238': '10 245',  # OR DH,CH => same
    '8 246': '10 246',  # OR DH,DH => same
    '8 192': '10 192',  # OR AL,AL => same
    '8 216': '10 195',  # OR AL,BL => same
    '8 200': '10 193',  # OR AL,CL => same
    '8 208': '10 194',  # OR AL,DL => same
    '8 195': '10 216',  # OR BL,AL => same
    '8 219': '10 219',  # OR BL,BL => same
    '8 203': '10 217',  # OR BL,CL => same
    '8 211': '10 218',  # OR BL,DL => same
    '8 193': '10 200',  # OR CL,AL => same
    '8 217': '10 203',  # OR CL,BL => same
    '8 201': '10 201',  # OR CL,CL => same
    '8 209': '10 202',  # OR CL,DL => same
    '8 194': '10 208',  # OR DL,AL => same
    '8 218': '10 211',  # OR DL,BL => same
    '8 202': '10 209',  # OR DL,CL => same
    '8 210': '10 210',  # OR DL,DL => same
    '25 192': '27 192',  # SBB EAX,EAX => same
    '25 216': '27 195',  # SBB EAX,EBX => same
    '25 200': '27 193',  # SBB EAX,ECX => same
    '25 208': '27 194',  # SBB EAX,EDX => same
    '25 224': '27 196',  # SBB EAX,ESP => same
    '25 232': '27 197',  # SBB EAX,EBP => same
    '25 240': '27 198',  # SBB EAX,ESI => same
    '25 248': '27 199',  # SBB EAX,EDI => same
    '25 195': '27 216',  # SBB EBX,EAX => same
    '25 219': '27 219',  # SBB EBX,EBX => same
    '25 203': '27 217',  # SBB EBX,ECX => same
    '25 211': '27 218',  # SBB EBX,EDX => same
    '25 227': '27 220',  # SBB EBX,ESP => same
    '25 235': '27 221',  # SBB EBX,EBP => same
    '25 243': '27 222',  # SBB EBX,ESI => same
    '25 251': '27 223',  # SBB EBX,EDI => same
    '25 193': '27 200',  # SBB ECX,EAX => same
    '25 217': '27 203',  # SBB ECX,EBX => same
    '25 201': '27 201',  # SBB ECX,ECX => same
    '25 209': '27 202',  # SBB ECX,EDX => same
    '25 225': '27 204',  # SBB ECX,ESP => same
    '25 233': '27 205',  # SBB ECX,EBP => same
    '25 241': '27 206',  # SBB ECX,ESI => same
    '25 249': '27 207',  # SBB ECX,EDI => same
    '25 194': '27 208',  # SBB EDX,EAX => same
    '25 218': '27 211',  # SBB EDX,EBX => same
    '25 202': '27 209',  # SBB EDX,ECX => same
    '25 210': '27 210',  # SBB EDX,EDX => same
    '25 226': '27 212',  # SBB EDX,ESP => same
    '25 234': '27 213',  # SBB EDX,EBP => same
    '25 242': '27 214',  # SBB EDX,ESI => same
    '25 250': '27 215',  # SBB EDX,EDI => same
    '25 196': '27 224',  # SBB ESP,EAX => same
    '25 220': '27 227',  # SBB ESP,EBX => same
    '25 204': '27 225',  # SBB ESP,ECX => same
    '25 212': '27 226',  # SBB ESP,EDX => same
    '25 228': '27 228',  # SBB ESP,ESP => same
    '25 236': '27 229',  # SBB ESP,EBP => same
    '25 244': '27 230',  # SBB ESP,ESI => same
    '25 252': '27 231',  # SBB ESP,EDI => same
    '25 197': '27 232',  # SBB EBP,EAX => same
    '25 221': '27 235',  # SBB EBP,EBX => same
    '25 205': '27 233',  # SBB EBP,ECX => same
    '25 213': '27 234',  # SBB EBP,EDX => same
    '25 229': '27 236',  # SBB EBP,ESP => same
    '25 237': '27 237',  # SBB EBP,EBP => same
    '25 245': '27 238',  # SBB EBP,ESI => same
    '25 253': '27 239',  # SBB EBP,EDI => same
    '25 198': '27 240',  # SBB ESI,EAX => same
    '25 222': '27 243',  # SBB ESI,EBX => same
    '25 206': '27 241',  # SBB ESI,ECX => same
    '25 214': '27 242',  # SBB ESI,EDX => same
    '25 230': '27 244',  # SBB ESI,ESP => same
    '25 238': '27 245',  # SBB ESI,EBP => same
    '25 246': '27 246',  # SBB ESI,ESI => same
    '25 254': '27 247',  # SBB ESI,EDI => same
    '25 199': '27 248',  # SBB EDI,EAX => same
    '25 223': '27 251',  # SBB EDI,EBX => same
    '25 207': '27 249',  # SBB EDI,ECX => same
    '25 215': '27 250',  # SBB EDI,EDX => same
    '25 231': '27 252',  # SBB EDI,ESP => same
    '25 239': '27 253',  # SBB EDI,EBP => same
    '25 247': '27 254',  # SBB EDI,ESI => same
    '25 255': '27 255',  # SBB EDI,EDI => same
    '24 228': '26 228',  # SBB AH,AH => same
    '24 252': '26 231',  # SBB AH,BH => same
    '24 236': '26 229',  # SBB AH,CH => same
    '24 244': '26 230',  # SBB AH,DH => same
    '24 231': '26 252',  # SBB BH,AH => same
    '24 255': '26 255',  # SBB BH,BH => same
    '24 239': '26 253',  # SBB BH,CH => same
    '24 247': '26 254',  # SBB BH,DH => same
    '24 229': '26 236',  # SBB CH,AH => same
    '24 253': '26 239',  # SBB CH,BH => same
    '24 237': '26 237',  # SBB CH,CH => same
    '24 245': '26 238',  # SBB CH,DH => same
    '24 230': '26 244',  # SBB DH,AH => same
    '24 254': '26 247',  # SBB DH,BH => same
    '24 238': '26 245',  # SBB DH,CH => same
    '24 246': '26 246',  # SBB DH,DH => same
    '24 192': '26 192',  # SBB AL,AL => same
    '24 216': '26 195',  # SBB AL,BL => same
    '24 200': '26 193',  # SBB AL,CL => same
    '24 208': '26 194',  # SBB AL,DL => same
    '24 195': '26 216',  # SBB BL,AL => same
    '24 219': '26 219',  # SBB BL,BL => same
    '24 203': '26 217',  # SBB BL,CL => same
    '24 211': '26 218',  # SBB BL,DL => same
    '24 193': '26 200',  # SBB CL,AL => same
    '24 217': '26 203',  # SBB CL,BL => same
    '24 201': '26 201',  # SBB CL,CL => same
    '24 209': '26 202',  # SBB CL,DL => same
    '24 194': '26 208',  # SBB DL,AL => same
    '24 218': '26 211',  # SBB DL,BL => same
    '24 202': '26 209',  # SBB DL,CL => same
    '24 210': '26 210',  # SBB DL,DL => same
    '41 192': '43 192',  # SUB EAX,EAX => same
    '41 216': '43 195',  # SUB EAX,EBX => same
    '41 200': '43 193',  # SUB EAX,ECX => same
    '41 208': '43 194',  # SUB EAX,EDX => same
    '41 224': '43 196',  # SUB EAX,ESP => same
    '41 232': '43 197',  # SUB EAX,EBP => same
    '41 240': '43 198',  # SUB EAX,ESI => same
    '41 248': '43 199',  # SUB EAX,EDI => same
    '41 195': '43 216',  # SUB EBX,EAX => same
    '41 219': '43 219',  # SUB EBX,EBX => same
    '41 203': '43 217',  # SUB EBX,ECX => same
    '41 211': '43 218',  # SUB EBX,EDX => same
    '41 227': '43 220',  # SUB EBX,ESP => same
    '41 235': '43 221',  # SUB EBX,EBP => same
    '41 243': '43 222',  # SUB EBX,ESI => same
    '41 251': '43 223',  # SUB EBX,EDI => same
    '41 193': '43 200',  # SUB ECX,EAX => same
    '41 217': '43 203',  # SUB ECX,EBX => same
    '41 201': '43 201',  # SUB ECX,ECX => same
    '41 209': '43 202',  # SUB ECX,EDX => same
    '41 225': '43 204',  # SUB ECX,ESP => same
    '41 233': '43 205',  # SUB ECX,EBP => same
    '41 241': '43 206',  # SUB ECX,ESI => same
    '41 249': '43 207',  # SUB ECX,EDI => same
    '41 194': '43 208',  # SUB EDX,EAX => same
    '41 218': '43 211',  # SUB EDX,EBX => same
    '41 202': '43 209',  # SUB EDX,ECX => same
    '41 210': '43 210',  # SUB EDX,EDX => same
    '41 226': '43 212',  # SUB EDX,ESP => same
    '41 234': '43 213',  # SUB EDX,EBP => same
    '41 242': '43 214',  # SUB EDX,ESI => same
    '41 250': '43 215',  # SUB EDX,EDI => same
    '41 196': '43 224',  # SUB ESP,EAX => same
    '41 220': '43 227',  # SUB ESP,EBX => same
    '41 204': '43 225',  # SUB ESP,ECX => same
    '41 212': '43 226',  # SUB ESP,EDX => same
    '41 228': '43 228',  # SUB ESP,ESP => same
    '41 236': '43 229',  # SUB ESP,EBP => same
    '41 244': '43 230',  # SUB ESP,ESI => same
    '41 252': '43 231',  # SUB ESP,EDI => same
    '41 197': '43 232',  # SUB EBP,EAX => same
    '41 221': '43 235',  # SUB EBP,EBX => same
    '41 205': '43 233',  # SUB EBP,ECX => same
    '41 213': '43 234',  # SUB EBP,EDX => same
    '41 229': '43 236',  # SUB EBP,ESP => same
    '41 237': '43 237',  # SUB EBP,EBP => same
    '41 245': '43 238',  # SUB EBP,ESI => same
    '41 253': '43 239',  # SUB EBP,EDI => same
    '41 198': '43 240',  # SUB ESI,EAX => same
    '41 222': '43 243',  # SUB ESI,EBX => same
    '41 206': '43 241',  # SUB ESI,ECX => same
    '41 214': '43 242',  # SUB ESI,EDX => same
    '41 230': '43 244',  # SUB ESI,ESP => same
    '41 238': '43 245',  # SUB ESI,EBP => same
    '41 246': '43 246',  # SUB ESI,ESI => same
    '41 254': '43 247',  # SUB ESI,EDI => same
    '41 199': '43 248',  # SUB EDI,EAX => same
    '41 223': '43 251',  # SUB EDI,EBX => same
    '41 207': '43 249',  # SUB EDI,ECX => same
    '41 215': '43 250',  # SUB EDI,EDX => same
    '41 231': '43 252',  # SUB EDI,ESP => same
    '41 239': '43 253',  # SUB EDI,EBP => same
    '41 247': '43 254',  # SUB EDI,ESI => same
    '41 255': '43 255',  # SUB EDI,EDI => same
    '40 228': '42 228',  # SUB AH,AH => same
    '40 252': '42 231',  # SUB AH,BH => same
    '40 236': '42 229',  # SUB AH,CH => same
    '40 244': '42 230',  # SUB AH,DH => same
    '40 231': '42 252',  # SUB BH,AH => same
    '40 255': '42 255',  # SUB BH,BH => same
    '40 239': '42 253',  # SUB BH,CH => same
    '40 247': '42 254',  # SUB BH,DH => same
    '40 229': '42 236',  # SUB CH,AH => same
    '40 253': '42 239',  # SUB CH,BH => same
    '40 237': '42 237',  # SUB CH,CH => same
    '40 245': '42 238',  # SUB CH,DH => same
    '40 230': '42 244',  # SUB DH,AH => same
    '40 254': '42 247',  # SUB DH,BH => same
    '40 238': '42 245',  # SUB DH,CH => same
    '40 246': '42 246',  # SUB DH,DH => same
    '40 192': '42 192',  # SUB AL,AL => same
    '40 216': '42 195',  # SUB AL,BL => same
    '40 200': '42 193',  # SUB AL,CL => same
    '40 208': '42 194',  # SUB AL,DL => same
    '40 195': '42 216',  # SUB BL,AL => same
    '40 219': '42 219',  # SUB BL,BL => same
    '40 203': '42 217',  # SUB BL,CL => same
    '40 211': '42 218',  # SUB BL,DL => same
    '40 193': '42 200',  # SUB CL,AL => same
    '40 217': '42 203',  # SUB CL,BL => same
    '40 201': '42 201',  # SUB CL,CL => same
    '40 209': '42 202',  # SUB CL,DL => same
    '40 194': '42 208',  # SUB DL,AL => same
    '40 218': '42 211',  # SUB DL,BL => same
    '40 202': '42 209',  # SUB DL,CL => same
    '40 210': '42 210',  # SUB DL,DL => same
    '57 192': '59 192',  # CMP EAX,EAX => same
    '57 216': '59 195',  # CMP EAX,EBX => same
    '57 200': '59 193',  # CMP EAX,ECX => same
    '57 208': '59 194',  # CMP EAX,EDX => same
    '57 224': '59 196',  # CMP EAX,ESP => same
    '57 232': '59 197',  # CMP EAX,EBP => same
    '57 240': '59 198',  # CMP EAX,ESI => same
    '57 248': '59 199',  # CMP EAX,EDI => same
    '57 195': '59 216',  # CMP EBX,EAX => same
    '57 219': '59 219',  # CMP EBX,EBX => same
    '57 203': '59 217',  # CMP EBX,ECX => same
    '57 211': '59 218',  # CMP EBX,EDX => same
    '57 227': '59 220',  # CMP EBX,ESP => same
    '57 235': '59 221',  # CMP EBX,EBP => same
    '57 243': '59 222',  # CMP EBX,ESI => same
    '57 251': '59 223',  # CMP EBX,EDI => same
    '57 193': '59 200',  # CMP ECX,EAX => same
    '57 217': '59 203',  # CMP ECX,EBX => same
    '57 201': '59 201',  # CMP ECX,ECX => same
    '57 209': '59 202',  # CMP ECX,EDX => same
    '57 225': '59 204',  # CMP ECX,ESP => same
    '57 233': '59 205',  # CMP ECX,EBP => same
    '57 241': '59 206',  # CMP ECX,ESI => same
    '57 249': '59 207',  # CMP ECX,EDI => same
    '57 194': '59 208',  # CMP EDX,EAX => same
    '57 218': '59 211',  # CMP EDX,EBX => same
    '57 202': '59 209',  # CMP EDX,ECX => same
    '57 210': '59 210',  # CMP EDX,EDX => same
    '57 226': '59 212',  # CMP EDX,ESP => same
    '57 234': '59 213',  # CMP EDX,EBP => same
    '57 242': '59 214',  # CMP EDX,ESI => same
    '57 250': '59 215',  # CMP EDX,EDI => same
    '57 196': '59 224',  # CMP ESP,EAX => same
    '57 220': '59 227',  # CMP ESP,EBX => same
    '57 204': '59 225',  # CMP ESP,ECX => same
    '57 212': '59 226',  # CMP ESP,EDX => same
    '57 228': '59 228',  # CMP ESP,ESP => same
    '57 236': '59 229',  # CMP ESP,EBP => same
    '57 244': '59 230',  # CMP ESP,ESI => same
    '57 252': '59 231',  # CMP ESP,EDI => same
    '57 197': '59 232',  # CMP EBP,EAX => same
    '57 221': '59 235',  # CMP EBP,EBX => same
    '57 205': '59 233',  # CMP EBP,ECX => same
    '57 213': '59 234',  # CMP EBP,EDX => same
    '57 229': '59 236',  # CMP EBP,ESP => same
    '57 237': '59 237',  # CMP EBP,EBP => same
    '57 245': '59 238',  # CMP EBP,ESI => same
    '57 253': '59 239',  # CMP EBP,EDI => same
    '57 198': '59 240',  # CMP ESI,EAX => same
    '57 222': '59 243',  # CMP ESI,EBX => same
    '57 206': '59 241',  # CMP ESI,ECX => same
    '57 214': '59 242',  # CMP ESI,EDX => same
    '57 230': '59 244',  # CMP ESI,ESP => same
    '57 238': '59 245',  # CMP ESI,EBP => same
    '57 246': '59 246',  # CMP ESI,ESI => same
    '57 254': '59 247',  # CMP ESI,EDI => same
    '57 199': '59 248',  # CMP EDI,EAX => same
    '57 223': '59 251',  # CMP EDI,EBX => same
    '57 207': '59 249',  # CMP EDI,ECX => same
    '57 215': '59 250',  # CMP EDI,EDX => same
    '57 231': '59 252',  # CMP EDI,ESP => same
    '57 239': '59 253',  # CMP EDI,EBP => same
    '57 247': '59 254',  # CMP EDI,ESI => same
    '57 255': '59 255',  # CMP EDI,EDI => same
    '56 228': '58 228',  # CMP AH,AH => same
    '56 252': '58 231',  # CMP AH,BH => same
    '56 236': '58 229',  # CMP AH,CH => same
    '56 244': '58 230',  # CMP AH,DH => same
    '56 231': '58 252',  # CMP BH,AH => same
    '56 255': '58 255',  # CMP BH,BH => same
    '56 239': '58 253',  # CMP BH,CH => same
    '56 247': '58 254',  # CMP BH,DH => same
    '56 229': '58 236',  # CMP CH,AH => same
    '56 253': '58 239',  # CMP CH,BH => same
    '56 237': '58 237',  # CMP CH,CH => same
    '56 245': '58 238',  # CMP CH,DH => same
    '56 230': '58 244',  # CMP DH,AH => same
    '56 254': '58 247',  # CMP DH,BH => same
    '56 238': '58 245',  # CMP DH,CH => same
    '56 246': '58 246',  # CMP DH,DH => same
    '56 192': '58 192',  # CMP AL,AL => same
    '56 216': '58 195',  # CMP AL,BL => same
    '56 200': '58 193',  # CMP AL,CL => same
    '56 208': '58 194',  # CMP AL,DL => same
    '56 195': '58 216',  # CMP BL,AL => same
    '56 219': '58 219',  # CMP BL,BL => same
    '56 203': '58 217',  # CMP BL,CL => same
    '56 211': '58 218',  # CMP BL,DL => same
    '56 193': '58 200',  # CMP CL,AL => same
    '56 217': '58 203',  # CMP CL,BL => same
    '56 201': '58 201',  # CMP CL,CL => same
    '56 209': '58 202',  # CMP CL,DL => same
    '56 194': '58 208',  # CMP DL,AL => same
    '56 218': '58 211',  # CMP DL,BL => same
    '56 202': '58 209',  # CMP DL,CL => same
    '56 210': '58 210',  # CMP DL,DL => same
    '133 216': '133 195',     # TEST EAX,EBX => same
    '133 200': '133 193',     # TEST EAX,ECX => same
    '133 208': '133 194',     # TEST EAX,EDX => same
    '133 224': '133 196',     # TEST EAX,ESP => same
    '133 232': '133 197',     # TEST EAX,EBP => same
    '133 240': '133 198',     # TEST EAX,ESI => same
    '133 248': '133 199',     # TEST EAX,EDI => same
    '133 203': '133 217',     # TEST EBX,ECX => same
    '133 211': '133 218',     # TEST EBX,EDX => same
    '133 227': '133 220',     # TEST EBX,ESP => same
    '133 235': '133 221',     # TEST EBX,EBP => same
    '133 243': '133 222',     # TEST EBX,ESI => same
    '133 251': '133 223',     # TEST EBX,EDI => same
    '133 209': '133 202',     # TEST ECX,EDX => same
    '133 225': '133 204',     # TEST ECX,ESP => same
    '133 233': '133 205',     # TEST ECX,EBP => same
    '133 241': '133 206',     # TEST ECX,ESI => same
    '133 249': '133 207',     # TEST ECX,EDI => same
    '133 226': '133 212',     # TEST EDX,ESP => same
    '133 234': '133 213',     # TEST EDX,EBP => same
    '133 242': '133 214',     # TEST EDX,ESI => same
    '133 250': '133 215',     # TEST EDX,EDI => same
    '133 236': '133 229',     # TEST ESP,EBP => same
    '133 244': '133 230',     # TEST ESP,ESI => same
    '133 252': '133 231',     # TEST ESP,EDI => same
    '133 245': '133 238',     # TEST EBP,ESI => same
    '133 253': '133 239',     # TEST EBP,EDI => same
    '133 254': '133 247',     # TEST ESI,EDI => same

}


decode_opcode_map_1_to_0 = \
{
    '51 192': '49 192',  # XOR EAX,EAX => same
    '51 195': '49 216',  # XOR EAX,EBX => same
    '51 193': '49 200',  # XOR EAX,ECX => same
    '51 194': '49 208',  # XOR EAX,EDX => same
    '51 196': '49 224',  # XOR EAX,ESP => same
    '51 197': '49 232',  # XOR EAX,EBP => same
    '51 198': '49 240',  # XOR EAX,ESI => same
    '51 199': '49 248',  # XOR EAX,EDI => same
    '51 216': '49 195',  # XOR EBX,EAX => same
    '51 219': '49 219',  # XOR EBX,EBX => same
    '51 217': '49 203',  # XOR EBX,ECX => same
    '51 218': '49 211',  # XOR EBX,EDX => same
    '51 220': '49 227',  # XOR EBX,ESP => same
    '51 221': '49 235',  # XOR EBX,EBP => same
    '51 222': '49 243',  # XOR EBX,ESI => same
    '51 223': '49 251',  # XOR EBX,EDI => same
    '51 200': '49 193',  # XOR ECX,EAX => same
    '51 203': '49 217',  # XOR ECX,EBX => same
    '51 201': '49 201',  # XOR ECX,ECX => same
    '51 202': '49 209',  # XOR ECX,EDX => same
    '51 204': '49 225',  # XOR ECX,ESP => same
    '51 205': '49 233',  # XOR ECX,EBP => same
    '51 206': '49 241',  # XOR ECX,ESI => same
    '51 207': '49 249',  # XOR ECX,EDI => same
    '51 208': '49 194',  # XOR EDX,EAX => same
    '51 211': '49 218',  # XOR EDX,EBX => same
    '51 209': '49 202',  # XOR EDX,ECX => same
    '51 210': '49 210',  # XOR EDX,EDX => same
    '51 212': '49 226',  # XOR EDX,ESP => same
    '51 213': '49 234',  # XOR EDX,EBP => same
    '51 214': '49 242',  # XOR EDX,ESI => same
    '51 215': '49 250',  # XOR EDX,EDI => same
    '51 224': '49 196',  # XOR ESP,EAX => same
    '51 227': '49 220',  # XOR ESP,EBX => same
    '51 225': '49 204',  # XOR ESP,ECX => same
    '51 226': '49 212',  # XOR ESP,EDX => same
    '51 228': '49 228',  # XOR ESP,ESP => same
    '51 229': '49 236',  # XOR ESP,EBP => same
    '51 230': '49 244',  # XOR ESP,ESI => same
    '51 231': '49 252',  # XOR ESP,EDI => same
    '51 232': '49 197',  # XOR EBP,EAX => same
    '51 235': '49 221',  # XOR EBP,EBX => same
    '51 233': '49 205',  # XOR EBP,ECX => same
    '51 234': '49 213',  # XOR EBP,EDX => same
    '51 236': '49 229',  # XOR EBP,ESP => same
    '51 237': '49 237',  # XOR EBP,EBP => same
    '51 238': '49 245',  # XOR EBP,ESI => same
    '51 239': '49 253',  # XOR EBP,EDI => same
    '51 240': '49 198',  # XOR ESI,EAX => same
    '51 243': '49 222',  # XOR ESI,EBX => same
    '51 241': '49 206',  # XOR ESI,ECX => same
    '51 242': '49 214',  # XOR ESI,EDX => same
    '51 244': '49 230',  # XOR ESI,ESP => same
    '51 245': '49 238',  # XOR ESI,EBP => same
    '51 246': '49 246',  # XOR ESI,ESI => same
    '51 247': '49 254',  # XOR ESI,EDI => same
    '51 248': '49 199',  # XOR EDI,EAX => same
    '51 251': '49 223',  # XOR EDI,EBX => same
    '51 249': '49 207',  # XOR EDI,ECX => same
    '51 250': '49 215',  # XOR EDI,EDX => same
    '51 252': '49 231',  # XOR EDI,ESP => same
    '51 253': '49 239',  # XOR EDI,EBP => same
    '51 254': '49 247',  # XOR EDI,ESI => same
    '51 255': '49 255',  # XOR EDI,EDI => same
    '50 228': '48 228',  # XOR AH,AH => same
    '50 231': '48 252',  # XOR AH,BH => same
    '50 229': '48 236',  # XOR AH,CH => same
    '50 230': '48 244',  # XOR AH,DH => same
    '50 252': '48 231',  # XOR BH,AH => same
    '50 255': '48 255',  # XOR BH,BH => same
    '50 253': '48 239',  # XOR BH,CH => same
    '50 254': '48 247',  # XOR BH,DH => same
    '50 236': '48 229',  # XOR CH,AH => same
    '50 239': '48 253',  # XOR CH,BH => same
    '50 237': '48 237',  # XOR CH,CH => same
    '50 238': '48 245',  # XOR CH,DH => same
    '50 244': '48 230',  # XOR DH,AH => same
    '50 247': '48 254',  # XOR DH,BH => same
    '50 245': '48 238',  # XOR DH,CH => same
    '50 246': '48 246',  # XOR DH,DH => same
    '50 192': '48 192',  # XOR AL,AL => same
    '50 195': '48 216',  # XOR AL,BL => same
    '50 193': '48 200',  # XOR AL,CL => same
    '50 194': '48 208',  # XOR AL,DL => same
    '50 216': '48 195',  # XOR BL,AL => same
    '50 219': '48 219',  # XOR BL,BL => same
    '50 217': '48 203',  # XOR BL,CL => same
    '50 218': '48 211',  # XOR BL,DL => same
    '50 200': '48 193',  # XOR CL,AL => same
    '50 203': '48 217',  # XOR CL,BL => same
    '50 201': '48 201',  # XOR CL,CL => same
    '50 202': '48 209',  # XOR CL,DL => same
    '50 208': '48 194',  # XOR DL,AL => same
    '50 211': '48 218',  # XOR DL,BL => same
    '50 209': '48 202',  # XOR DL,CL => same
    '50 210': '48 210',  # XOR DL,DL => same
    '139 192': '137 192',  # MOV EAX,EAX => same
    '139 195': '137 216',  # MOV EAX,EBX => same
    '139 193': '137 200',  # MOV EAX,ECX => same
    '139 194': '137 208',  # MOV EAX,EDX => same
    '139 196': '137 224',  # MOV EAX,ESP => same
    '139 197': '137 232',  # MOV EAX,EBP => same
    '139 198': '137 240',  # MOV EAX,ESI => same
    '139 199': '137 248',  # MOV EAX,EDI => same
    '139 216': '137 195',  # MOV EBX,EAX => same
    '139 219': '137 219',  # MOV EBX,EBX => same
    '139 217': '137 203',  # MOV EBX,ECX => same
    '139 218': '137 211',  # MOV EBX,EDX => same
    '139 220': '137 227',  # MOV EBX,ESP => same
    '139 221': '137 235',  # MOV EBX,EBP => same
    '139 222': '137 243',  # MOV EBX,ESI => same
    '139 223': '137 251',  # MOV EBX,EDI => same
    '139 200': '137 193',  # MOV ECX,EAX => same
    '139 203': '137 217',  # MOV ECX,EBX => same
    '139 201': '137 201',  # MOV ECX,ECX => same
    '139 202': '137 209',  # MOV ECX,EDX => same
    '139 204': '137 225',  # MOV ECX,ESP => same
    '139 205': '137 233',  # MOV ECX,EBP => same
    '139 206': '137 241',  # MOV ECX,ESI => same
    '139 207': '137 249',  # MOV ECX,EDI => same
    '139 208': '137 194',  # MOV EDX,EAX => same
    '139 211': '137 218',  # MOV EDX,EBX => same
    '139 209': '137 202',  # MOV EDX,ECX => same
    '139 210': '137 210',  # MOV EDX,EDX => same
    '139 212': '137 226',  # MOV EDX,ESP => same
    '139 213': '137 234',  # MOV EDX,EBP => same
    '139 214': '137 242',  # MOV EDX,ESI => same
    '139 215': '137 250',  # MOV EDX,EDI => same
    '139 224': '137 196',  # MOV ESP,EAX => same
    '139 227': '137 220',  # MOV ESP,EBX => same
    '139 225': '137 204',  # MOV ESP,ECX => same
    '139 226': '137 212',  # MOV ESP,EDX => same
    '139 228': '137 228',  # MOV ESP,ESP => same
    '139 229': '137 236',  # MOV ESP,EBP => same
    '139 230': '137 244',  # MOV ESP,ESI => same
    '139 231': '137 252',  # MOV ESP,EDI => same
    '139 232': '137 197',  # MOV EBP,EAX => same
    '139 235': '137 221',  # MOV EBP,EBX => same
    '139 233': '137 205',  # MOV EBP,ECX => same
    '139 234': '137 213',  # MOV EBP,EDX => same
    '139 236': '137 229',  # MOV EBP,ESP => same
    '139 237': '137 237',  # MOV EBP,EBP => same
    '139 238': '137 245',  # MOV EBP,ESI => same
    '139 239': '137 253',  # MOV EBP,EDI => same
    '139 240': '137 198',  # MOV ESI,EAX => same
    '139 243': '137 222',  # MOV ESI,EBX => same
    '139 241': '137 206',  # MOV ESI,ECX => same
    '139 242': '137 214',  # MOV ESI,EDX => same
    '139 244': '137 230',  # MOV ESI,ESP => same
    '139 245': '137 238',  # MOV ESI,EBP => same
    '139 246': '137 246',  # MOV ESI,ESI => same
    '139 247': '137 254',  # MOV ESI,EDI => same
    '139 248': '137 199',  # MOV EDI,EAX => same
    '139 251': '137 223',  # MOV EDI,EBX => same
    '139 249': '137 207',  # MOV EDI,ECX => same
    '139 250': '137 215',  # MOV EDI,EDX => same
    '139 252': '137 231',  # MOV EDI,ESP => same
    '139 253': '137 239',  # MOV EDI,EBP => same
    '139 254': '137 247',  # MOV EDI,ESI => same
    '139 255': '137 255',  # MOV EDI,EDI => same
    '138 228': '136 228',  # MOV AH,AH => same
    '138 231': '136 252',  # MOV AH,BH => same
    '138 229': '136 236',  # MOV AH,CH => same
    '138 230': '136 244',  # MOV AH,DH => same
    '138 252': '136 231',  # MOV BH,AH => same
    '138 255': '136 255',  # MOV BH,BH => same
    '138 253': '136 239',  # MOV BH,CH => same
    '138 254': '136 247',  # MOV BH,DH => same
    '138 236': '136 229',  # MOV CH,AH => same
    '138 239': '136 253',  # MOV CH,BH => same
    '138 237': '136 237',  # MOV CH,CH => same
    '138 238': '136 245',  # MOV CH,DH => same
    '138 244': '136 230',  # MOV DH,AH => same
    '138 247': '136 254',  # MOV DH,BH => same
    '138 245': '136 238',  # MOV DH,CH => same
    '138 246': '136 246',  # MOV DH,DH => same
    '138 192': '136 192',  # MOV AL,AL => same
    '138 195': '136 216',  # MOV AL,BL => same
    '138 193': '136 200',  # MOV AL,CL => same
    '138 194': '136 208',  # MOV AL,DL => same
    '138 216': '136 195',  # MOV BL,AL => same
    '138 219': '136 219',  # MOV BL,BL => same
    '138 217': '136 203',  # MOV BL,CL => same
    '138 218': '136 211',  # MOV BL,DL => same
    '138 200': '136 193',  # MOV CL,AL => same
    '138 203': '136 217',  # MOV CL,BL => same
    '138 201': '136 201',  # MOV CL,CL => same
    '138 202': '136 209',  # MOV CL,DL => same
    '138 208': '136 194',  # MOV DL,AL => same
    '138 211': '136 218',  # MOV DL,BL => same
    '138 209': '136 202',  # MOV DL,CL => same
    '138 210': '136 210',  # MOV DL,DL => same
    '3 192': '1 192',  # ADD EAX,EAX => same
    '3 195': '1 216',  # ADD EAX,EBX => same
    '3 193': '1 200',  # ADD EAX,ECX => same
    '3 194': '1 208',  # ADD EAX,EDX => same
    '3 196': '1 224',  # ADD EAX,ESP => same
    '3 197': '1 232',  # ADD EAX,EBP => same
    '3 198': '1 240',  # ADD EAX,ESI => same
    '3 199': '1 248',  # ADD EAX,EDI => same
    '3 216': '1 195',  # ADD EBX,EAX => same
    '3 219': '1 219',  # ADD EBX,EBX => same
    '3 217': '1 203',  # ADD EBX,ECX => same
    '3 218': '1 211',  # ADD EBX,EDX => same
    '3 220': '1 227',  # ADD EBX,ESP => same
    '3 221': '1 235',  # ADD EBX,EBP => same
    '3 222': '1 243',  # ADD EBX,ESI => same
    '3 223': '1 251',  # ADD EBX,EDI => same
    '3 200': '1 193',  # ADD ECX,EAX => same
    '3 203': '1 217',  # ADD ECX,EBX => same
    '3 201': '1 201',  # ADD ECX,ECX => same
    '3 202': '1 209',  # ADD ECX,EDX => same
    '3 204': '1 225',  # ADD ECX,ESP => same
    '3 205': '1 233',  # ADD ECX,EBP => same
    '3 206': '1 241',  # ADD ECX,ESI => same
    '3 207': '1 249',  # ADD ECX,EDI => same
    '3 208': '1 194',  # ADD EDX,EAX => same
    '3 211': '1 218',  # ADD EDX,EBX => same
    '3 209': '1 202',  # ADD EDX,ECX => same
    '3 210': '1 210',  # ADD EDX,EDX => same
    '3 212': '1 226',  # ADD EDX,ESP => same
    '3 213': '1 234',  # ADD EDX,EBP => same
    '3 214': '1 242',  # ADD EDX,ESI => same
    '3 215': '1 250',  # ADD EDX,EDI => same
    '3 224': '1 196',  # ADD ESP,EAX => same
    '3 227': '1 220',  # ADD ESP,EBX => same
    '3 225': '1 204',  # ADD ESP,ECX => same
    '3 226': '1 212',  # ADD ESP,EDX => same
    '3 228': '1 228',  # ADD ESP,ESP => same
    '3 229': '1 236',  # ADD ESP,EBP => same
    '3 230': '1 244',  # ADD ESP,ESI => same
    '3 231': '1 252',  # ADD ESP,EDI => same
    '3 232': '1 197',  # ADD EBP,EAX => same
    '3 235': '1 221',  # ADD EBP,EBX => same
    '3 233': '1 205',  # ADD EBP,ECX => same
    '3 234': '1 213',  # ADD EBP,EDX => same
    '3 236': '1 229',  # ADD EBP,ESP => same
    '3 237': '1 237',  # ADD EBP,EBP => same
    '3 238': '1 245',  # ADD EBP,ESI => same
    '3 239': '1 253',  # ADD EBP,EDI => same
    '3 240': '1 198',  # ADD ESI,EAX => same
    '3 243': '1 222',  # ADD ESI,EBX => same
    '3 241': '1 206',  # ADD ESI,ECX => same
    '3 242': '1 214',  # ADD ESI,EDX => same
    '3 244': '1 230',  # ADD ESI,ESP => same
    '3 245': '1 238',  # ADD ESI,EBP => same
    '3 246': '1 246',  # ADD ESI,ESI => same
    '3 247': '1 254',  # ADD ESI,EDI => same
    '3 248': '1 199',  # ADD EDI,EAX => same
    '3 251': '1 223',  # ADD EDI,EBX => same
    '3 249': '1 207',  # ADD EDI,ECX => same
    '3 250': '1 215',  # ADD EDI,EDX => same
    '3 252': '1 231',  # ADD EDI,ESP => same
    '3 253': '1 239',  # ADD EDI,EBP => same
    '3 254': '1 247',  # ADD EDI,ESI => same
    '3 255': '1 255',  # ADD EDI,EDI => same
    '2 228': '0 228',  # ADD AH,AH => same
    '2 231': '0 252',  # ADD AH,BH => same
    '2 229': '0 236',  # ADD AH,CH => same
    '2 230': '0 244',  # ADD AH,DH => same
    '2 252': '0 231',  # ADD BH,AH => same
    '2 255': '0 255',  # ADD BH,BH => same
    '2 253': '0 239',  # ADD BH,CH => same
    '2 254': '0 247',  # ADD BH,DH => same
    '2 236': '0 229',  # ADD CH,AH => same
    '2 239': '0 253',  # ADD CH,BH => same
    '2 237': '0 237',  # ADD CH,CH => same
    '2 238': '0 245',  # ADD CH,DH => same
    '2 244': '0 230',  # ADD DH,AH => same
    '2 247': '0 254',  # ADD DH,BH => same
    '2 245': '0 238',  # ADD DH,CH => same
    '2 246': '0 246',  # ADD DH,DH => same
    '2 192': '0 192',  # ADD AL,AL => same
    '2 195': '0 216',  # ADD AL,BL => same
    '2 193': '0 200',  # ADD AL,CL => same
    '2 194': '0 208',  # ADD AL,DL => same
    '2 216': '0 195',  # ADD BL,AL => same
    '2 219': '0 219',  # ADD BL,BL => same
    '2 217': '0 203',  # ADD BL,CL => same
    '2 218': '0 211',  # ADD BL,DL => same
    '2 200': '0 193',  # ADD CL,AL => same
    '2 203': '0 217',  # ADD CL,BL => same
    '2 201': '0 201',  # ADD CL,CL => same
    '2 202': '0 209',  # ADD CL,DL => same
    '2 208': '0 194',  # ADD DL,AL => same
    '2 211': '0 218',  # ADD DL,BL => same
    '2 209': '0 202',  # ADD DL,CL => same
    '2 210': '0 210',  # ADD DL,DL => same
    '19 192': '17 192',  # ADC EAX,EAX => same
    '19 195': '17 216',  # ADC EAX,EBX => same
    '19 193': '17 200',  # ADC EAX,ECX => same
    '19 194': '17 208',  # ADC EAX,EDX => same
    '19 196': '17 224',  # ADC EAX,ESP => same
    '19 197': '17 232',  # ADC EAX,EBP => same
    '19 198': '17 240',  # ADC EAX,ESI => same
    '19 199': '17 248',  # ADC EAX,EDI => same
    '19 216': '17 195',  # ADC EBX,EAX => same
    '19 219': '17 219',  # ADC EBX,EBX => same
    '19 217': '17 203',  # ADC EBX,ECX => same
    '19 218': '17 211',  # ADC EBX,EDX => same
    '19 220': '17 227',  # ADC EBX,ESP => same
    '19 221': '17 235',  # ADC EBX,EBP => same
    '19 222': '17 243',  # ADC EBX,ESI => same
    '19 223': '17 251',  # ADC EBX,EDI => same
    '19 200': '17 193',  # ADC ECX,EAX => same
    '19 203': '17 217',  # ADC ECX,EBX => same
    '19 201': '17 201',  # ADC ECX,ECX => same
    '19 202': '17 209',  # ADC ECX,EDX => same
    '19 204': '17 225',  # ADC ECX,ESP => same
    '19 205': '17 233',  # ADC ECX,EBP => same
    '19 206': '17 241',  # ADC ECX,ESI => same
    '19 207': '17 249',  # ADC ECX,EDI => same
    '19 208': '17 194',  # ADC EDX,EAX => same
    '19 211': '17 218',  # ADC EDX,EBX => same
    '19 209': '17 202',  # ADC EDX,ECX => same
    '19 210': '17 210',  # ADC EDX,EDX => same
    '19 212': '17 226',  # ADC EDX,ESP => same
    '19 213': '17 234',  # ADC EDX,EBP => same
    '19 214': '17 242',  # ADC EDX,ESI => same
    '19 215': '17 250',  # ADC EDX,EDI => same
    '19 224': '17 196',  # ADC ESP,EAX => same
    '19 227': '17 220',  # ADC ESP,EBX => same
    '19 225': '17 204',  # ADC ESP,ECX => same
    '19 226': '17 212',  # ADC ESP,EDX => same
    '19 228': '17 228',  # ADC ESP,ESP => same
    '19 229': '17 236',  # ADC ESP,EBP => same
    '19 230': '17 244',  # ADC ESP,ESI => same
    '19 231': '17 252',  # ADC ESP,EDI => same
    '19 232': '17 197',  # ADC EBP,EAX => same
    '19 235': '17 221',  # ADC EBP,EBX => same
    '19 233': '17 205',  # ADC EBP,ECX => same
    '19 234': '17 213',  # ADC EBP,EDX => same
    '19 236': '17 229',  # ADC EBP,ESP => same
    '19 237': '17 237',  # ADC EBP,EBP => same
    '19 238': '17 245',  # ADC EBP,ESI => same
    '19 239': '17 253',  # ADC EBP,EDI => same
    '19 240': '17 198',  # ADC ESI,EAX => same
    '19 243': '17 222',  # ADC ESI,EBX => same
    '19 241': '17 206',  # ADC ESI,ECX => same
    '19 242': '17 214',  # ADC ESI,EDX => same
    '19 244': '17 230',  # ADC ESI,ESP => same
    '19 245': '17 238',  # ADC ESI,EBP => same
    '19 246': '17 246',  # ADC ESI,ESI => same
    '19 247': '17 254',  # ADC ESI,EDI => same
    '19 248': '17 199',  # ADC EDI,EAX => same
    '19 251': '17 223',  # ADC EDI,EBX => same
    '19 249': '17 207',  # ADC EDI,ECX => same
    '19 250': '17 215',  # ADC EDI,EDX => same
    '19 252': '17 231',  # ADC EDI,ESP => same
    '19 253': '17 239',  # ADC EDI,EBP => same
    '19 254': '17 247',  # ADC EDI,ESI => same
    '19 255': '17 255',  # ADC EDI,EDI => same
    '18 228': '16 228',  # ADC AH,AH => same
    '18 231': '16 252',  # ADC AH,BH => same
    '18 229': '16 236',  # ADC AH,CH => same
    '18 230': '16 244',  # ADC AH,DH => same
    '18 252': '16 231',  # ADC BH,AH => same
    '18 255': '16 255',  # ADC BH,BH => same
    '18 253': '16 239',  # ADC BH,CH => same
    '18 254': '16 247',  # ADC BH,DH => same
    '18 236': '16 229',  # ADC CH,AH => same
    '18 239': '16 253',  # ADC CH,BH => same
    '18 237': '16 237',  # ADC CH,CH => same
    '18 238': '16 245',  # ADC CH,DH => same
    '18 244': '16 230',  # ADC DH,AH => same
    '18 247': '16 254',  # ADC DH,BH => same
    '18 245': '16 238',  # ADC DH,CH => same
    '18 246': '16 246',  # ADC DH,DH => same
    '18 192': '16 192',  # ADC AL,AL => same
    '18 195': '16 216',  # ADC AL,BL => same
    '18 193': '16 200',  # ADC AL,CL => same
    '18 194': '16 208',  # ADC AL,DL => same
    '18 216': '16 195',  # ADC BL,AL => same
    '18 219': '16 219',  # ADC BL,BL => same
    '18 217': '16 203',  # ADC BL,CL => same
    '18 218': '16 211',  # ADC BL,DL => same
    '18 200': '16 193',  # ADC CL,AL => same
    '18 203': '16 217',  # ADC CL,BL => same
    '18 201': '16 201',  # ADC CL,CL => same
    '18 202': '16 209',  # ADC CL,DL => same
    '18 208': '16 194',  # ADC DL,AL => same
    '18 211': '16 218',  # ADC DL,BL => same
    '18 209': '16 202',  # ADC DL,CL => same
    '18 210': '16 210',  # ADC DL,DL => same
    '35 192': '33 192',  # AND EAX,EAX => same
    '35 195': '33 216',  # AND EAX,EBX => same
    '35 193': '33 200',  # AND EAX,ECX => same
    '35 194': '33 208',  # AND EAX,EDX => same
    '35 196': '33 224',  # AND EAX,ESP => same
    '35 197': '33 232',  # AND EAX,EBP => same
    '35 198': '33 240',  # AND EAX,ESI => same
    '35 199': '33 248',  # AND EAX,EDI => same
    '35 216': '33 195',  # AND EBX,EAX => same
    '35 219': '33 219',  # AND EBX,EBX => same
    '35 217': '33 203',  # AND EBX,ECX => same
    '35 218': '33 211',  # AND EBX,EDX => same
    '35 220': '33 227',  # AND EBX,ESP => same
    '35 221': '33 235',  # AND EBX,EBP => same
    '35 222': '33 243',  # AND EBX,ESI => same
    '35 223': '33 251',  # AND EBX,EDI => same
    '35 200': '33 193',  # AND ECX,EAX => same
    '35 203': '33 217',  # AND ECX,EBX => same
    '35 201': '33 201',  # AND ECX,ECX => same
    '35 202': '33 209',  # AND ECX,EDX => same
    '35 204': '33 225',  # AND ECX,ESP => same
    '35 205': '33 233',  # AND ECX,EBP => same
    '35 206': '33 241',  # AND ECX,ESI => same
    '35 207': '33 249',  # AND ECX,EDI => same
    '35 208': '33 194',  # AND EDX,EAX => same
    '35 211': '33 218',  # AND EDX,EBX => same
    '35 209': '33 202',  # AND EDX,ECX => same
    '35 210': '33 210',  # AND EDX,EDX => same
    '35 212': '33 226',  # AND EDX,ESP => same
    '35 213': '33 234',  # AND EDX,EBP => same
    '35 214': '33 242',  # AND EDX,ESI => same
    '35 215': '33 250',  # AND EDX,EDI => same
    '35 224': '33 196',  # AND ESP,EAX => same
    '35 227': '33 220',  # AND ESP,EBX => same
    '35 225': '33 204',  # AND ESP,ECX => same
    '35 226': '33 212',  # AND ESP,EDX => same
    '35 228': '33 228',  # AND ESP,ESP => same
    '35 229': '33 236',  # AND ESP,EBP => same
    '35 230': '33 244',  # AND ESP,ESI => same
    '35 231': '33 252',  # AND ESP,EDI => same
    '35 232': '33 197',  # AND EBP,EAX => same
    '35 235': '33 221',  # AND EBP,EBX => same
    '35 233': '33 205',  # AND EBP,ECX => same
    '35 234': '33 213',  # AND EBP,EDX => same
    '35 236': '33 229',  # AND EBP,ESP => same
    '35 237': '33 237',  # AND EBP,EBP => same
    '35 238': '33 245',  # AND EBP,ESI => same
    '35 239': '33 253',  # AND EBP,EDI => same
    '35 240': '33 198',  # AND ESI,EAX => same
    '35 243': '33 222',  # AND ESI,EBX => same
    '35 241': '33 206',  # AND ESI,ECX => same
    '35 242': '33 214',  # AND ESI,EDX => same
    '35 244': '33 230',  # AND ESI,ESP => same
    '35 245': '33 238',  # AND ESI,EBP => same
    '35 246': '33 246',  # AND ESI,ESI => same
    '35 247': '33 254',  # AND ESI,EDI => same
    '35 248': '33 199',  # AND EDI,EAX => same
    '35 251': '33 223',  # AND EDI,EBX => same
    '35 249': '33 207',  # AND EDI,ECX => same
    '35 250': '33 215',  # AND EDI,EDX => same
    '35 252': '33 231',  # AND EDI,ESP => same
    '35 253': '33 239',  # AND EDI,EBP => same
    '35 254': '33 247',  # AND EDI,ESI => same
    '35 255': '33 255',  # AND EDI,EDI => same
    '34 228': '32 228',  # AND AH,AH => same
    '34 231': '32 252',  # AND AH,BH => same
    '34 229': '32 236',  # AND AH,CH => same
    '34 230': '32 244',  # AND AH,DH => same
    '34 252': '32 231',  # AND BH,AH => same
    '34 255': '32 255',  # AND BH,BH => same
    '34 253': '32 239',  # AND BH,CH => same
    '34 254': '32 247',  # AND BH,DH => same
    '34 236': '32 229',  # AND CH,AH => same
    '34 239': '32 253',  # AND CH,BH => same
    '34 237': '32 237',  # AND CH,CH => same
    '34 238': '32 245',  # AND CH,DH => same
    '34 244': '32 230',  # AND DH,AH => same
    '34 247': '32 254',  # AND DH,BH => same
    '34 245': '32 238',  # AND DH,CH => same
    '34 246': '32 246',  # AND DH,DH => same
    '34 192': '32 192',  # AND AL,AL => same
    '34 195': '32 216',  # AND AL,BL => same
    '34 193': '32 200',  # AND AL,CL => same
    '34 194': '32 208',  # AND AL,DL => same
    '34 216': '32 195',  # AND BL,AL => same
    '34 219': '32 219',  # AND BL,BL => same
    '34 217': '32 203',  # AND BL,CL => same
    '34 218': '32 211',  # AND BL,DL => same
    '34 200': '32 193',  # AND CL,AL => same
    '34 203': '32 217',  # AND CL,BL => same
    '34 201': '32 201',  # AND CL,CL => same
    '34 202': '32 209',  # AND CL,DL => same
    '34 208': '32 194',  # AND DL,AL => same
    '34 211': '32 218',  # AND DL,BL => same
    '34 209': '32 202',  # AND DL,CL => same
    '34 210': '32 210',  # AND DL,DL => same
    '11 192': '9 192',  # OR EAX,EAX => same
    '11 195': '9 216',  # OR EAX,EBX => same
    '11 193': '9 200',  # OR EAX,ECX => same
    '11 194': '9 208',  # OR EAX,EDX => same
    '11 196': '9 224',  # OR EAX,ESP => same
    '11 197': '9 232',  # OR EAX,EBP => same
    '11 198': '9 240',  # OR EAX,ESI => same
    '11 199': '9 248',  # OR EAX,EDI => same
    '11 216': '9 195',  # OR EBX,EAX => same
    '11 219': '9 219',  # OR EBX,EBX => same
    '11 217': '9 203',  # OR EBX,ECX => same
    '11 218': '9 211',  # OR EBX,EDX => same
    '11 220': '9 227',  # OR EBX,ESP => same
    '11 221': '9 235',  # OR EBX,EBP => same
    '11 222': '9 243',  # OR EBX,ESI => same
    '11 223': '9 251',  # OR EBX,EDI => same
    '11 200': '9 193',  # OR ECX,EAX => same
    '11 203': '9 217',  # OR ECX,EBX => same
    '11 201': '9 201',  # OR ECX,ECX => same
    '11 202': '9 209',  # OR ECX,EDX => same
    '11 204': '9 225',  # OR ECX,ESP => same
    '11 205': '9 233',  # OR ECX,EBP => same
    '11 206': '9 241',  # OR ECX,ESI => same
    '11 207': '9 249',  # OR ECX,EDI => same
    '11 208': '9 194',  # OR EDX,EAX => same
    '11 211': '9 218',  # OR EDX,EBX => same
    '11 209': '9 202',  # OR EDX,ECX => same
    '11 210': '9 210',  # OR EDX,EDX => same
    '11 212': '9 226',  # OR EDX,ESP => same
    '11 213': '9 234',  # OR EDX,EBP => same
    '11 214': '9 242',  # OR EDX,ESI => same
    '11 215': '9 250',  # OR EDX,EDI => same
    '11 224': '9 196',  # OR ESP,EAX => same
    '11 227': '9 220',  # OR ESP,EBX => same
    '11 225': '9 204',  # OR ESP,ECX => same
    '11 226': '9 212',  # OR ESP,EDX => same
    '11 228': '9 228',  # OR ESP,ESP => same
    '11 229': '9 236',  # OR ESP,EBP => same
    '11 230': '9 244',  # OR ESP,ESI => same
    '11 231': '9 252',  # OR ESP,EDI => same
    '11 232': '9 197',  # OR EBP,EAX => same
    '11 235': '9 221',  # OR EBP,EBX => same
    '11 233': '9 205',  # OR EBP,ECX => same
    '11 234': '9 213',  # OR EBP,EDX => same
    '11 236': '9 229',  # OR EBP,ESP => same
    '11 237': '9 237',  # OR EBP,EBP => same
    '11 238': '9 245',  # OR EBP,ESI => same
    '11 239': '9 253',  # OR EBP,EDI => same
    '11 240': '9 198',  # OR ESI,EAX => same
    '11 243': '9 222',  # OR ESI,EBX => same
    '11 241': '9 206',  # OR ESI,ECX => same
    '11 242': '9 214',  # OR ESI,EDX => same
    '11 244': '9 230',  # OR ESI,ESP => same
    '11 245': '9 238',  # OR ESI,EBP => same
    '11 246': '9 246',  # OR ESI,ESI => same
    '11 247': '9 254',  # OR ESI,EDI => same
    '11 248': '9 199',  # OR EDI,EAX => same
    '11 251': '9 223',  # OR EDI,EBX => same
    '11 249': '9 207',  # OR EDI,ECX => same
    '11 250': '9 215',  # OR EDI,EDX => same
    '11 252': '9 231',  # OR EDI,ESP => same
    '11 253': '9 239',  # OR EDI,EBP => same
    '11 254': '9 247',  # OR EDI,ESI => same
    '11 255': '9 255',  # OR EDI,EDI => same
    '10 228': '8 228',  # OR AH,AH => same
    '10 231': '8 252',  # OR AH,BH => same
    '10 229': '8 236',  # OR AH,CH => same
    '10 230': '8 244',  # OR AH,DH => same
    '10 252': '8 231',  # OR BH,AH => same
    '10 255': '8 255',  # OR BH,BH => same
    '10 253': '8 239',  # OR BH,CH => same
    '10 254': '8 247',  # OR BH,DH => same
    '10 236': '8 229',  # OR CH,AH => same
    '10 239': '8 253',  # OR CH,BH => same
    '10 237': '8 237',  # OR CH,CH => same
    '10 238': '8 245',  # OR CH,DH => same
    '10 244': '8 230',  # OR DH,AH => same
    '10 247': '8 254',  # OR DH,BH => same
    '10 245': '8 238',  # OR DH,CH => same
    '10 246': '8 246',  # OR DH,DH => same
    '10 192': '8 192',  # OR AL,AL => same
    '10 195': '8 216',  # OR AL,BL => same
    '10 193': '8 200',  # OR AL,CL => same
    '10 194': '8 208',  # OR AL,DL => same
    '10 216': '8 195',  # OR BL,AL => same
    '10 219': '8 219',  # OR BL,BL => same
    '10 217': '8 203',  # OR BL,CL => same
    '10 218': '8 211',  # OR BL,DL => same
    '10 200': '8 193',  # OR CL,AL => same
    '10 203': '8 217',  # OR CL,BL => same
    '10 201': '8 201',  # OR CL,CL => same
    '10 202': '8 209',  # OR CL,DL => same
    '10 208': '8 194',  # OR DL,AL => same
    '10 211': '8 218',  # OR DL,BL => same
    '10 209': '8 202',  # OR DL,CL => same
    '10 210': '8 210',  # OR DL,DL => same
    '27 192': '25 192',  # SBB EAX,EAX => same
    '27 195': '25 216',  # SBB EAX,EBX => same
    '27 193': '25 200',  # SBB EAX,ECX => same
    '27 194': '25 208',  # SBB EAX,EDX => same
    '27 196': '25 224',  # SBB EAX,ESP => same
    '27 197': '25 232',  # SBB EAX,EBP => same
    '27 198': '25 240',  # SBB EAX,ESI => same
    '27 199': '25 248',  # SBB EAX,EDI => same
    '27 216': '25 195',  # SBB EBX,EAX => same
    '27 219': '25 219',  # SBB EBX,EBX => same
    '27 217': '25 203',  # SBB EBX,ECX => same
    '27 218': '25 211',  # SBB EBX,EDX => same
    '27 220': '25 227',  # SBB EBX,ESP => same
    '27 221': '25 235',  # SBB EBX,EBP => same
    '27 222': '25 243',  # SBB EBX,ESI => same
    '27 223': '25 251',  # SBB EBX,EDI => same
    '27 200': '25 193',  # SBB ECX,EAX => same
    '27 203': '25 217',  # SBB ECX,EBX => same
    '27 201': '25 201',  # SBB ECX,ECX => same
    '27 202': '25 209',  # SBB ECX,EDX => same
    '27 204': '25 225',  # SBB ECX,ESP => same
    '27 205': '25 233',  # SBB ECX,EBP => same
    '27 206': '25 241',  # SBB ECX,ESI => same
    '27 207': '25 249',  # SBB ECX,EDI => same
    '27 208': '25 194',  # SBB EDX,EAX => same
    '27 211': '25 218',  # SBB EDX,EBX => same
    '27 209': '25 202',  # SBB EDX,ECX => same
    '27 210': '25 210',  # SBB EDX,EDX => same
    '27 212': '25 226',  # SBB EDX,ESP => same
    '27 213': '25 234',  # SBB EDX,EBP => same
    '27 214': '25 242',  # SBB EDX,ESI => same
    '27 215': '25 250',  # SBB EDX,EDI => same
    '27 224': '25 196',  # SBB ESP,EAX => same
    '27 227': '25 220',  # SBB ESP,EBX => same
    '27 225': '25 204',  # SBB ESP,ECX => same
    '27 226': '25 212',  # SBB ESP,EDX => same
    '27 228': '25 228',  # SBB ESP,ESP => same
    '27 229': '25 236',  # SBB ESP,EBP => same
    '27 230': '25 244',  # SBB ESP,ESI => same
    '27 231': '25 252',  # SBB ESP,EDI => same
    '27 232': '25 197',  # SBB EBP,EAX => same
    '27 235': '25 221',  # SBB EBP,EBX => same
    '27 233': '25 205',  # SBB EBP,ECX => same
    '27 234': '25 213',  # SBB EBP,EDX => same
    '27 236': '25 229',  # SBB EBP,ESP => same
    '27 237': '25 237',  # SBB EBP,EBP => same
    '27 238': '25 245',  # SBB EBP,ESI => same
    '27 239': '25 253',  # SBB EBP,EDI => same
    '27 240': '25 198',  # SBB ESI,EAX => same
    '27 243': '25 222',  # SBB ESI,EBX => same
    '27 241': '25 206',  # SBB ESI,ECX => same
    '27 242': '25 214',  # SBB ESI,EDX => same
    '27 244': '25 230',  # SBB ESI,ESP => same
    '27 245': '25 238',  # SBB ESI,EBP => same
    '27 246': '25 246',  # SBB ESI,ESI => same
    '27 247': '25 254',  # SBB ESI,EDI => same
    '27 248': '25 199',  # SBB EDI,EAX => same
    '27 251': '25 223',  # SBB EDI,EBX => same
    '27 249': '25 207',  # SBB EDI,ECX => same
    '27 250': '25 215',  # SBB EDI,EDX => same
    '27 252': '25 231',  # SBB EDI,ESP => same
    '27 253': '25 239',  # SBB EDI,EBP => same
    '27 254': '25 247',  # SBB EDI,ESI => same
    '27 255': '25 255',  # SBB EDI,EDI => same
    '26 228': '24 228',  # SBB AH,AH => same
    '26 231': '24 252',  # SBB AH,BH => same
    '26 229': '24 236',  # SBB AH,CH => same
    '26 230': '24 244',  # SBB AH,DH => same
    '26 252': '24 231',  # SBB BH,AH => same
    '26 255': '24 255',  # SBB BH,BH => same
    '26 253': '24 239',  # SBB BH,CH => same
    '26 254': '24 247',  # SBB BH,DH => same
    '26 236': '24 229',  # SBB CH,AH => same
    '26 239': '24 253',  # SBB CH,BH => same
    '26 237': '24 237',  # SBB CH,CH => same
    '26 238': '24 245',  # SBB CH,DH => same
    '26 244': '24 230',  # SBB DH,AH => same
    '26 247': '24 254',  # SBB DH,BH => same
    '26 245': '24 238',  # SBB DH,CH => same
    '26 246': '24 246',  # SBB DH,DH => same
    '26 192': '24 192',  # SBB AL,AL => same
    '26 195': '24 216',  # SBB AL,BL => same
    '26 193': '24 200',  # SBB AL,CL => same
    '26 194': '24 208',  # SBB AL,DL => same
    '26 216': '24 195',  # SBB BL,AL => same
    '26 219': '24 219',  # SBB BL,BL => same
    '26 217': '24 203',  # SBB BL,CL => same
    '26 218': '24 211',  # SBB BL,DL => same
    '26 200': '24 193',  # SBB CL,AL => same
    '26 203': '24 217',  # SBB CL,BL => same
    '26 201': '24 201',  # SBB CL,CL => same
    '26 202': '24 209',  # SBB CL,DL => same
    '26 208': '24 194',  # SBB DL,AL => same
    '26 211': '24 218',  # SBB DL,BL => same
    '26 209': '24 202',  # SBB DL,CL => same
    '26 210': '24 210',  # SBB DL,DL => same
    '43 192': '41 192',  # SUB EAX,EAX => same
    '43 195': '41 216',  # SUB EAX,EBX => same
    '43 193': '41 200',  # SUB EAX,ECX => same
    '43 194': '41 208',  # SUB EAX,EDX => same
    '43 196': '41 224',  # SUB EAX,ESP => same
    '43 197': '41 232',  # SUB EAX,EBP => same
    '43 198': '41 240',  # SUB EAX,ESI => same
    '43 199': '41 248',  # SUB EAX,EDI => same
    '43 216': '41 195',  # SUB EBX,EAX => same
    '43 219': '41 219',  # SUB EBX,EBX => same
    '43 217': '41 203',  # SUB EBX,ECX => same
    '43 218': '41 211',  # SUB EBX,EDX => same
    '43 220': '41 227',  # SUB EBX,ESP => same
    '43 221': '41 235',  # SUB EBX,EBP => same
    '43 222': '41 243',  # SUB EBX,ESI => same
    '43 223': '41 251',  # SUB EBX,EDI => same
    '43 200': '41 193',  # SUB ECX,EAX => same
    '43 203': '41 217',  # SUB ECX,EBX => same
    '43 201': '41 201',  # SUB ECX,ECX => same
    '43 202': '41 209',  # SUB ECX,EDX => same
    '43 204': '41 225',  # SUB ECX,ESP => same
    '43 205': '41 233',  # SUB ECX,EBP => same
    '43 206': '41 241',  # SUB ECX,ESI => same
    '43 207': '41 249',  # SUB ECX,EDI => same
    '43 208': '41 194',  # SUB EDX,EAX => same
    '43 211': '41 218',  # SUB EDX,EBX => same
    '43 209': '41 202',  # SUB EDX,ECX => same
    '43 210': '41 210',  # SUB EDX,EDX => same
    '43 212': '41 226',  # SUB EDX,ESP => same
    '43 213': '41 234',  # SUB EDX,EBP => same
    '43 214': '41 242',  # SUB EDX,ESI => same
    '43 215': '41 250',  # SUB EDX,EDI => same
    '43 224': '41 196',  # SUB ESP,EAX => same
    '43 227': '41 220',  # SUB ESP,EBX => same
    '43 225': '41 204',  # SUB ESP,ECX => same
    '43 226': '41 212',  # SUB ESP,EDX => same
    '43 228': '41 228',  # SUB ESP,ESP => same
    '43 229': '41 236',  # SUB ESP,EBP => same
    '43 230': '41 244',  # SUB ESP,ESI => same
    '43 231': '41 252',  # SUB ESP,EDI => same
    '43 232': '41 197',  # SUB EBP,EAX => same
    '43 235': '41 221',  # SUB EBP,EBX => same
    '43 233': '41 205',  # SUB EBP,ECX => same
    '43 234': '41 213',  # SUB EBP,EDX => same
    '43 236': '41 229',  # SUB EBP,ESP => same
    '43 237': '41 237',  # SUB EBP,EBP => same
    '43 238': '41 245',  # SUB EBP,ESI => same
    '43 239': '41 253',  # SUB EBP,EDI => same
    '43 240': '41 198',  # SUB ESI,EAX => same
    '43 243': '41 222',  # SUB ESI,EBX => same
    '43 241': '41 206',  # SUB ESI,ECX => same
    '43 242': '41 214',  # SUB ESI,EDX => same
    '43 244': '41 230',  # SUB ESI,ESP => same
    '43 245': '41 238',  # SUB ESI,EBP => same
    '43 246': '41 246',  # SUB ESI,ESI => same
    '43 247': '41 254',  # SUB ESI,EDI => same
    '43 248': '41 199',  # SUB EDI,EAX => same
    '43 251': '41 223',  # SUB EDI,EBX => same
    '43 249': '41 207',  # SUB EDI,ECX => same
    '43 250': '41 215',  # SUB EDI,EDX => same
    '43 252': '41 231',  # SUB EDI,ESP => same
    '43 253': '41 239',  # SUB EDI,EBP => same
    '43 254': '41 247',  # SUB EDI,ESI => same
    '43 255': '41 255',  # SUB EDI,EDI => same
    '42 228': '40 228',  # SUB AH,AH => same
    '42 231': '40 252',  # SUB AH,BH => same
    '42 229': '40 236',  # SUB AH,CH => same
    '42 230': '40 244',  # SUB AH,DH => same
    '42 252': '40 231',  # SUB BH,AH => same
    '42 255': '40 255',  # SUB BH,BH => same
    '42 253': '40 239',  # SUB BH,CH => same
    '42 254': '40 247',  # SUB BH,DH => same
    '42 236': '40 229',  # SUB CH,AH => same
    '42 239': '40 253',  # SUB CH,BH => same
    '42 237': '40 237',  # SUB CH,CH => same
    '42 238': '40 245',  # SUB CH,DH => same
    '42 244': '40 230',  # SUB DH,AH => same
    '42 247': '40 254',  # SUB DH,BH => same
    '42 245': '40 238',  # SUB DH,CH => same
    '42 246': '40 246',  # SUB DH,DH => same
    '42 192': '40 192',  # SUB AL,AL => same
    '42 195': '40 216',  # SUB AL,BL => same
    '42 193': '40 200',  # SUB AL,CL => same
    '42 194': '40 208',  # SUB AL,DL => same
    '42 216': '40 195',  # SUB BL,AL => same
    '42 219': '40 219',  # SUB BL,BL => same
    '42 217': '40 203',  # SUB BL,CL => same
    '42 218': '40 211',  # SUB BL,DL => same
    '42 200': '40 193',  # SUB CL,AL => same
    '42 203': '40 217',  # SUB CL,BL => same
    '42 201': '40 201',  # SUB CL,CL => same
    '42 202': '40 209',  # SUB CL,DL => same
    '42 208': '40 194',  # SUB DL,AL => same
    '42 211': '40 218',  # SUB DL,BL => same
    '42 209': '40 202',  # SUB DL,CL => same
    '42 210': '40 210',  # SUB DL,DL => same
    '59 192': '57 192',  # CMP EAX,EAX => same
    '59 195': '57 216',  # CMP EAX,EBX => same
    '59 193': '57 200',  # CMP EAX,ECX => same
    '59 194': '57 208',  # CMP EAX,EDX => same
    '59 196': '57 224',  # CMP EAX,ESP => same
    '59 197': '57 232',  # CMP EAX,EBP => same
    '59 198': '57 240',  # CMP EAX,ESI => same
    '59 199': '57 248',  # CMP EAX,EDI => same
    '59 216': '57 195',  # CMP EBX,EAX => same
    '59 219': '57 219',  # CMP EBX,EBX => same
    '59 217': '57 203',  # CMP EBX,ECX => same
    '59 218': '57 211',  # CMP EBX,EDX => same
    '59 220': '57 227',  # CMP EBX,ESP => same
    '59 221': '57 235',  # CMP EBX,EBP => same
    '59 222': '57 243',  # CMP EBX,ESI => same
    '59 223': '57 251',  # CMP EBX,EDI => same
    '59 200': '57 193',  # CMP ECX,EAX => same
    '59 203': '57 217',  # CMP ECX,EBX => same
    '59 201': '57 201',  # CMP ECX,ECX => same
    '59 202': '57 209',  # CMP ECX,EDX => same
    '59 204': '57 225',  # CMP ECX,ESP => same
    '59 205': '57 233',  # CMP ECX,EBP => same
    '59 206': '57 241',  # CMP ECX,ESI => same
    '59 207': '57 249',  # CMP ECX,EDI => same
    '59 208': '57 194',  # CMP EDX,EAX => same
    '59 211': '57 218',  # CMP EDX,EBX => same
    '59 209': '57 202',  # CMP EDX,ECX => same
    '59 210': '57 210',  # CMP EDX,EDX => same
    '59 212': '57 226',  # CMP EDX,ESP => same
    '59 213': '57 234',  # CMP EDX,EBP => same
    '59 214': '57 242',  # CMP EDX,ESI => same
    '59 215': '57 250',  # CMP EDX,EDI => same
    '59 224': '57 196',  # CMP ESP,EAX => same
    '59 227': '57 220',  # CMP ESP,EBX => same
    '59 225': '57 204',  # CMP ESP,ECX => same
    '59 226': '57 212',  # CMP ESP,EDX => same
    '59 228': '57 228',  # CMP ESP,ESP => same
    '59 229': '57 236',  # CMP ESP,EBP => same
    '59 230': '57 244',  # CMP ESP,ESI => same
    '59 231': '57 252',  # CMP ESP,EDI => same
    '59 232': '57 197',  # CMP EBP,EAX => same
    '59 235': '57 221',  # CMP EBP,EBX => same
    '59 233': '57 205',  # CMP EBP,ECX => same
    '59 234': '57 213',  # CMP EBP,EDX => same
    '59 236': '57 229',  # CMP EBP,ESP => same
    '59 237': '57 237',  # CMP EBP,EBP => same
    '59 238': '57 245',  # CMP EBP,ESI => same
    '59 239': '57 253',  # CMP EBP,EDI => same
    '59 240': '57 198',  # CMP ESI,EAX => same
    '59 243': '57 222',  # CMP ESI,EBX => same
    '59 241': '57 206',  # CMP ESI,ECX => same
    '59 242': '57 214',  # CMP ESI,EDX => same
    '59 244': '57 230',  # CMP ESI,ESP => same
    '59 245': '57 238',  # CMP ESI,EBP => same
    '59 246': '57 246',  # CMP ESI,ESI => same
    '59 247': '57 254',  # CMP ESI,EDI => same
    '59 248': '57 199',  # CMP EDI,EAX => same
    '59 251': '57 223',  # CMP EDI,EBX => same
    '59 249': '57 207',  # CMP EDI,ECX => same
    '59 250': '57 215',  # CMP EDI,EDX => same
    '59 252': '57 231',  # CMP EDI,ESP => same
    '59 253': '57 239',  # CMP EDI,EBP => same
    '59 254': '57 247',  # CMP EDI,ESI => same
    '59 255': '57 255',  # CMP EDI,EDI => same
    '58 228': '56 228',  # CMP AH,AH => same
    '58 231': '56 252',  # CMP AH,BH => same
    '58 229': '56 236',  # CMP AH,CH => same
    '58 230': '56 244',  # CMP AH,DH => same
    '58 252': '56 231',  # CMP BH,AH => same
    '58 255': '56 255',  # CMP BH,BH => same
    '58 253': '56 239',  # CMP BH,CH => same
    '58 254': '56 247',  # CMP BH,DH => same
    '58 236': '56 229',  # CMP CH,AH => same
    '58 239': '56 253',  # CMP CH,BH => same
    '58 237': '56 237',  # CMP CH,CH => same
    '58 238': '56 245',  # CMP CH,DH => same
    '58 244': '56 230',  # CMP DH,AH => same
    '58 247': '56 254',  # CMP DH,BH => same
    '58 245': '56 238',  # CMP DH,CH => same
    '58 246': '56 246',  # CMP DH,DH => same
    '58 192': '56 192',  # CMP AL,AL => same
    '58 195': '56 216',  # CMP AL,BL => same
    '58 193': '56 200',  # CMP AL,CL => same
    '58 194': '56 208',  # CMP AL,DL => same
    '58 216': '56 195',  # CMP BL,AL => same
    '58 219': '56 219',  # CMP BL,BL => same
    '58 217': '56 203',  # CMP BL,CL => same
    '58 218': '56 211',  # CMP BL,DL => same
    '58 200': '56 193',  # CMP CL,AL => same
    '58 203': '56 217',  # CMP CL,BL => same
    '58 201': '56 201',  # CMP CL,CL => same
    '58 202': '56 209',  # CMP CL,DL => same
    '58 208': '56 194',  # CMP DL,AL => same
    '58 211': '56 218',  # CMP DL,BL => same
    '58 209': '56 202',  # CMP DL,CL => same
    '58 210': '56 210',  # CMP DL,DL => same
    '133 195': '133 216',     # TEST EAX,EBX => same
    '133 193': '133 200',     # TEST EAX,ECX => same
    '133 194': '133 208',     # TEST EAX,EDX => same
    '133 196': '133 224',     # TEST EAX,ESP => same
    '133 197': '133 232',     # TEST EAX,EBP => same
    '133 198': '133 240',     # TEST EAX,ESI => same
    '133 199': '133 248',     # TEST EAX,EDI => same
    '133 217': '133 203',     # TEST EBX,ECX => same
    '133 218': '133 211',     # TEST EBX,EDX => same
    '133 220': '133 227',     # TEST EBX,ESP => same
    '133 221': '133 235',     # TEST EBX,EBP => same
    '133 222': '133 243',     # TEST EBX,ESI => same
    '133 223': '133 251',     # TEST EBX,EDI => same
    '133 202': '133 209',     # TEST ECX,EDX => same
    '133 204': '133 225',     # TEST ECX,ESP => same
    '133 205': '133 233',     # TEST ECX,EBP => same
    '133 206': '133 241',     # TEST ECX,ESI => same
    '133 207': '133 249',     # TEST ECX,EDI => same
    '133 212': '133 226',     # TEST EDX,ESP => same
    '133 213': '133 234',     # TEST EDX,EBP => same
    '133 214': '133 242',     # TEST EDX,ESI => same
    '133 215': '133 250',     # TEST EDX,EDI => same
    '133 229': '133 236',     # TEST ESP,EBP => same
    '133 230': '133 244',     # TEST ESP,ESI => same
    '133 231': '133 252',     # TEST ESP,EDI => same
    '133 238': '133 245',     # TEST EBP,ESI => same
    '133 239': '133 253',     # TEST EBP,EDI => same
    '133 247': '133 254',     # TEST ESI,EDI => same
}



extraction_opcode_map = \
{
    '49 192': '0',  # XOR EAX,EAX => 0
    '51 192': '1',  # XOR EAX,EAX => 1
    '49 216': '0',  # XOR EAX,EBX => 0
    '51 195': '1',  # XOR EAX,EBX => 1
    '49 200': '0',  # XOR EAX,ECX => 0
    '51 193': '1',  # XOR EAX,ECX => 1
    '49 208': '0',  # XOR EAX,EDX => 0
    '51 194': '1',  # XOR EAX,EDX => 1
    '49 224': '0',  # XOR EAX,ESP => 0
    '51 196': '1',  # XOR EAX,ESP => 1
    '49 232': '0',  # XOR EAX,EBP => 0
    '51 197': '1',  # XOR EAX,EBP => 1
    '49 240': '0',  # XOR EAX,ESI => 0
    '51 198': '1',  # XOR EAX,ESI => 1
    '49 248': '0',  # XOR EAX,EDI => 0
    '51 199': '1',  # XOR EAX,EDI => 1
    '49 195': '0',  # XOR EBX,EAX => 0
    '51 216': '1',  # XOR EBX,EAX => 1
    '49 219': '0',  # XOR EBX,EBX => 0
    '51 219': '1',  # XOR EBX,EBX => 1
    '49 203': '0',  # XOR EBX,ECX => 0
    '51 217': '1',  # XOR EBX,ECX => 1
    '49 211': '0',  # XOR EBX,EDX => 0
    '51 218': '1',  # XOR EBX,EDX => 1
    '49 227': '0',  # XOR EBX,ESP => 0
    '51 220': '1',  # XOR EBX,ESP => 1
    '49 235': '0',  # XOR EBX,EBP => 0
    '51 221': '1',  # XOR EBX,EBP => 1
    '49 243': '0',  # XOR EBX,ESI => 0
    '51 222': '1',  # XOR EBX,ESI => 1
    '49 251': '0',  # XOR EBX,EDI => 0
    '51 223': '1',  # XOR EBX,EDI => 1
    '49 193': '0',  # XOR ECX,EAX => 0
    '51 200': '1',  # XOR ECX,EAX => 1
    '49 217': '0',  # XOR ECX,EBX => 0
    '51 203': '1',  # XOR ECX,EBX => 1
    '49 201': '0',  # XOR ECX,ECX => 0
    '51 201': '1',  # XOR ECX,ECX => 1
    '49 209': '0',  # XOR ECX,EDX => 0
    '51 202': '1',  # XOR ECX,EDX => 1
    '49 225': '0',  # XOR ECX,ESP => 0
    '51 204': '1',  # XOR ECX,ESP => 1
    '49 233': '0',  # XOR ECX,EBP => 0
    '51 205': '1',  # XOR ECX,EBP => 1
    '49 241': '0',  # XOR ECX,ESI => 0
    '51 206': '1',  # XOR ECX,ESI => 1
    '49 249': '0',  # XOR ECX,EDI => 0
    '51 207': '1',  # XOR ECX,EDI => 1
    '49 194': '0',  # XOR EDX,EAX => 0
    '51 208': '1',  # XOR EDX,EAX => 1
    '49 218': '0',  # XOR EDX,EBX => 0
    '51 211': '1',  # XOR EDX,EBX => 1
    '49 202': '0',  # XOR EDX,ECX => 0
    '51 209': '1',  # XOR EDX,ECX => 1
    '49 210': '0',  # XOR EDX,EDX => 0
    '51 210': '1',  # XOR EDX,EDX => 1
    '49 226': '0',  # XOR EDX,ESP => 0
    '51 212': '1',  # XOR EDX,ESP => 1
    '49 234': '0',  # XOR EDX,EBP => 0
    '51 213': '1',  # XOR EDX,EBP => 1
    '49 242': '0',  # XOR EDX,ESI => 0
    '51 214': '1',  # XOR EDX,ESI => 1
    '49 250': '0',  # XOR EDX,EDI => 0
    '51 215': '1',  # XOR EDX,EDI => 1
    '49 196': '0',  # XOR ESP,EAX => 0
    '51 224': '1',  # XOR ESP,EAX => 1
    '49 220': '0',  # XOR ESP,EBX => 0
    '51 227': '1',  # XOR ESP,EBX => 1
    '49 204': '0',  # XOR ESP,ECX => 0
    '51 225': '1',  # XOR ESP,ECX => 1
    '49 212': '0',  # XOR ESP,EDX => 0
    '51 226': '1',  # XOR ESP,EDX => 1
    '49 228': '0',  # XOR ESP,ESP => 0
    '51 228': '1',  # XOR ESP,ESP => 1
    '49 236': '0',  # XOR ESP,EBP => 0
    '51 229': '1',  # XOR ESP,EBP => 1
    '49 244': '0',  # XOR ESP,ESI => 0
    '51 230': '1',  # XOR ESP,ESI => 1
    '49 252': '0',  # XOR ESP,EDI => 0
    '51 231': '1',  # XOR ESP,EDI => 1
    '49 197': '0',  # XOR EBP,EAX => 0
    '51 232': '1',  # XOR EBP,EAX => 1
    '49 221': '0',  # XOR EBP,EBX => 0
    '51 235': '1',  # XOR EBP,EBX => 1
    '49 205': '0',  # XOR EBP,ECX => 0
    '51 233': '1',  # XOR EBP,ECX => 1
    '49 213': '0',  # XOR EBP,EDX => 0
    '51 234': '1',  # XOR EBP,EDX => 1
    '49 229': '0',  # XOR EBP,ESP => 0
    '51 236': '1',  # XOR EBP,ESP => 1
    '49 237': '0',  # XOR EBP,EBP => 0
    '51 237': '1',  # XOR EBP,EBP => 1
    '49 245': '0',  # XOR EBP,ESI => 0
    '51 238': '1',  # XOR EBP,ESI => 1
    '49 253': '0',  # XOR EBP,EDI => 0
    '51 239': '1',  # XOR EBP,EDI => 1
    '49 198': '0',  # XOR ESI,EAX => 0
    '51 240': '1',  # XOR ESI,EAX => 1
    '49 222': '0',  # XOR ESI,EBX => 0
    '51 243': '1',  # XOR ESI,EBX => 1
    '49 206': '0',  # XOR ESI,ECX => 0
    '51 241': '1',  # XOR ESI,ECX => 1
    '49 214': '0',  # XOR ESI,EDX => 0
    '51 242': '1',  # XOR ESI,EDX => 1
    '49 230': '0',  # XOR ESI,ESP => 0
    '51 244': '1',  # XOR ESI,ESP => 1
    '49 238': '0',  # XOR ESI,EBP => 0
    '51 245': '1',  # XOR ESI,EBP => 1
    '49 246': '0',  # XOR ESI,ESI => 0
    '51 246': '1',  # XOR ESI,ESI => 1
    '49 254': '0',  # XOR ESI,EDI => 0
    '51 247': '1',  # XOR ESI,EDI => 1
    '49 199': '0',  # XOR EDI,EAX => 0
    '51 248': '1',  # XOR EDI,EAX => 1
    '49 223': '0',  # XOR EDI,EBX => 0
    '51 251': '1',  # XOR EDI,EBX => 1
    '49 207': '0',  # XOR EDI,ECX => 0
    '51 249': '1',  # XOR EDI,ECX => 1
    '49 215': '0',  # XOR EDI,EDX => 0
    '51 250': '1',  # XOR EDI,EDX => 1
    '49 231': '0',  # XOR EDI,ESP => 0
    '51 252': '1',  # XOR EDI,ESP => 1
    '49 239': '0',  # XOR EDI,EBP => 0
    '51 253': '1',  # XOR EDI,EBP => 1
    '49 247': '0',  # XOR EDI,ESI => 0
    '51 254': '1',  # XOR EDI,ESI => 1
    '49 255': '0',  # XOR EDI,EDI => 0
    '51 255': '1',  # XOR EDI,EDI => 1
    '48 228': '0',  # XOR AH,AH => 0
    '50 228': '1',  # XOR AH,AH => 1
    '48 252': '0',  # XOR AH,BH => 0
    '50 231': '1',  # XOR AH,BH => 1
    '48 236': '0',  # XOR AH,CH => 0
    '50 229': '1',  # XOR AH,CH => 1
    '48 244': '0',  # XOR AH,DH => 0
    '50 230': '1',  # XOR AH,DH => 1
    '48 231': '0',  # XOR BH,AH => 0
    '50 252': '1',  # XOR BH,AH => 1
    '48 255': '0',  # XOR BH,BH => 0
    '50 255': '1',  # XOR BH,BH => 1
    '48 239': '0',  # XOR BH,CH => 0
    '50 253': '1',  # XOR BH,CH => 1
    '48 247': '0',  # XOR BH,DH => 0
    '50 254': '1',  # XOR BH,DH => 1
    '48 229': '0',  # XOR CH,AH => 0
    '50 236': '1',  # XOR CH,AH => 1
    '48 253': '0',  # XOR CH,BH => 0
    '50 239': '1',  # XOR CH,BH => 1
    '48 237': '0',  # XOR CH,CH => 0
    '50 237': '1',  # XOR CH,CH => 1
    '48 245': '0',  # XOR CH,DH => 0
    '50 238': '1',  # XOR CH,DH => 1
    '48 230': '0',  # XOR DH,AH => 0
    '50 244': '1',  # XOR DH,AH => 1
    '48 254': '0',  # XOR DH,BH => 0
    '50 247': '1',  # XOR DH,BH => 1
    '48 238': '0',  # XOR DH,CH => 0
    '50 245': '1',  # XOR DH,CH => 1
    '48 246': '0',  # XOR DH,DH => 0
    '50 246': '1',  # XOR DH,DH => 1
    '48 192': '0',  # XOR AL,AL => 0
    '50 192': '1',  # XOR AL,AL => 1
    '48 216': '0',  # XOR AL,BL => 0
    '50 195': '1',  # XOR AL,BL => 1
    '48 200': '0',  # XOR AL,CL => 0
    '50 193': '1',  # XOR AL,CL => 1
    '48 208': '0',  # XOR AL,DL => 0
    '50 194': '1',  # XOR AL,DL => 1
    '48 195': '0',  # XOR BL,AL => 0
    '50 216': '1',  # XOR BL,AL => 1
    '48 219': '0',  # XOR BL,BL => 0
    '50 219': '1',  # XOR BL,BL => 1
    '48 203': '0',  # XOR BL,CL => 0
    '50 217': '1',  # XOR BL,CL => 1
    '48 211': '0',  # XOR BL,DL => 0
    '50 218': '1',  # XOR BL,DL => 1
    '48 193': '0',  # XOR CL,AL => 0
    '50 200': '1',  # XOR CL,AL => 1
    '48 217': '0',  # XOR CL,BL => 0
    '50 203': '1',  # XOR CL,BL => 1
    '48 201': '0',  # XOR CL,CL => 0
    '50 201': '1',  # XOR CL,CL => 1
    '48 209': '0',  # XOR CL,DL => 0
    '50 202': '1',  # XOR CL,DL => 1
    '48 194': '0',  # XOR DL,AL => 0
    '50 208': '1',  # XOR DL,AL => 1
    '48 218': '0',  # XOR DL,BL => 0
    '50 211': '1',  # XOR DL,BL => 1
    '48 202': '0',  # XOR DL,CL => 0
    '50 209': '1',  # XOR DL,CL => 1
    '48 210': '0',  # XOR DL,DL => 0
    '50 210': '1',  # XOR DL,DL => 1
    '137 192': '0',  # MOV EAX,EAX => 0
    '139 192': '1',  # MOV EAX,EAX => 1
    '137 216': '0',  # MOV EAX,EBX => 0
    '139 195': '1',  # MOV EAX,EBX => 1
    '137 200': '0',  # MOV EAX,ECX => 0
    '139 193': '1',  # MOV EAX,ECX => 1
    '137 208': '0',  # MOV EAX,EDX => 0
    '139 194': '1',  # MOV EAX,EDX => 1
    '137 224': '0',  # MOV EAX,ESP => 0
    '139 196': '1',  # MOV EAX,ESP => 1
    '137 232': '0',  # MOV EAX,EBP => 0
    '139 197': '1',  # MOV EAX,EBP => 1
    '137 240': '0',  # MOV EAX,ESI => 0
    '139 198': '1',  # MOV EAX,ESI => 1
    '137 248': '0',  # MOV EAX,EDI => 0
    '139 199': '1',  # MOV EAX,EDI => 1
    '137 195': '0',  # MOV EBX,EAX => 0
    '139 216': '1',  # MOV EBX,EAX => 1
    '137 219': '0',  # MOV EBX,EBX => 0
    '139 219': '1',  # MOV EBX,EBX => 1
    '137 203': '0',  # MOV EBX,ECX => 0
    '139 217': '1',  # MOV EBX,ECX => 1
    '137 211': '0',  # MOV EBX,EDX => 0
    '139 218': '1',  # MOV EBX,EDX => 1
    '137 227': '0',  # MOV EBX,ESP => 0
    '139 220': '1',  # MOV EBX,ESP => 1
    '137 235': '0',  # MOV EBX,EBP => 0
    '139 221': '1',  # MOV EBX,EBP => 1
    '137 243': '0',  # MOV EBX,ESI => 0
    '139 222': '1',  # MOV EBX,ESI => 1
    '137 251': '0',  # MOV EBX,EDI => 0
    '139 223': '1',  # MOV EBX,EDI => 1
    '137 193': '0',  # MOV ECX,EAX => 0
    '139 200': '1',  # MOV ECX,EAX => 1
    '137 217': '0',  # MOV ECX,EBX => 0
    '139 203': '1',  # MOV ECX,EBX => 1
    '137 201': '0',  # MOV ECX,ECX => 0
    '139 201': '1',  # MOV ECX,ECX => 1
    '137 209': '0',  # MOV ECX,EDX => 0
    '139 202': '1',  # MOV ECX,EDX => 1
    '137 225': '0',  # MOV ECX,ESP => 0
    '139 204': '1',  # MOV ECX,ESP => 1
    '137 233': '0',  # MOV ECX,EBP => 0
    '139 205': '1',  # MOV ECX,EBP => 1
    '137 241': '0',  # MOV ECX,ESI => 0
    '139 206': '1',  # MOV ECX,ESI => 1
    '137 249': '0',  # MOV ECX,EDI => 0
    '139 207': '1',  # MOV ECX,EDI => 1
    '137 194': '0',  # MOV EDX,EAX => 0
    '139 208': '1',  # MOV EDX,EAX => 1
    '137 218': '0',  # MOV EDX,EBX => 0
    '139 211': '1',  # MOV EDX,EBX => 1
    '137 202': '0',  # MOV EDX,ECX => 0
    '139 209': '1',  # MOV EDX,ECX => 1
    '137 210': '0',  # MOV EDX,EDX => 0
    '139 210': '1',  # MOV EDX,EDX => 1
    '137 226': '0',  # MOV EDX,ESP => 0
    '139 212': '1',  # MOV EDX,ESP => 1
    '137 234': '0',  # MOV EDX,EBP => 0
    '139 213': '1',  # MOV EDX,EBP => 1
    '137 242': '0',  # MOV EDX,ESI => 0
    '139 214': '1',  # MOV EDX,ESI => 1
    '137 250': '0',  # MOV EDX,EDI => 0
    '139 215': '1',  # MOV EDX,EDI => 1
    '137 196': '0',  # MOV ESP,EAX => 0
    '139 224': '1',  # MOV ESP,EAX => 1
    '137 220': '0',  # MOV ESP,EBX => 0
    '139 227': '1',  # MOV ESP,EBX => 1
    '137 204': '0',  # MOV ESP,ECX => 0
    '139 225': '1',  # MOV ESP,ECX => 1
    '137 212': '0',  # MOV ESP,EDX => 0
    '139 226': '1',  # MOV ESP,EDX => 1
    '137 228': '0',  # MOV ESP,ESP => 0
    '139 228': '1',  # MOV ESP,ESP => 1
    '137 236': '0',  # MOV ESP,EBP => 0
    '139 229': '1',  # MOV ESP,EBP => 1
    '137 244': '0',  # MOV ESP,ESI => 0
    '139 230': '1',  # MOV ESP,ESI => 1
    '137 252': '0',  # MOV ESP,EDI => 0
    '139 231': '1',  # MOV ESP,EDI => 1
    '137 197': '0',  # MOV EBP,EAX => 0
    '139 232': '1',  # MOV EBP,EAX => 1
    '137 221': '0',  # MOV EBP,EBX => 0
    '139 235': '1',  # MOV EBP,EBX => 1
    '137 205': '0',  # MOV EBP,ECX => 0
    '139 233': '1',  # MOV EBP,ECX => 1
    '137 213': '0',  # MOV EBP,EDX => 0
    '139 234': '1',  # MOV EBP,EDX => 1
    '137 229': '0',  # MOV EBP,ESP => 0
    '139 236': '1',  # MOV EBP,ESP => 1
    '137 237': '0',  # MOV EBP,EBP => 0
    '139 237': '1',  # MOV EBP,EBP => 1
    '137 245': '0',  # MOV EBP,ESI => 0
    '139 238': '1',  # MOV EBP,ESI => 1
    '137 253': '0',  # MOV EBP,EDI => 0
    '139 239': '1',  # MOV EBP,EDI => 1
    '137 198': '0',  # MOV ESI,EAX => 0
    '139 240': '1',  # MOV ESI,EAX => 1
    '137 222': '0',  # MOV ESI,EBX => 0
    '139 243': '1',  # MOV ESI,EBX => 1
    '137 206': '0',  # MOV ESI,ECX => 0
    '139 241': '1',  # MOV ESI,ECX => 1
    '137 214': '0',  # MOV ESI,EDX => 0
    '139 242': '1',  # MOV ESI,EDX => 1
    '137 230': '0',  # MOV ESI,ESP => 0
    '139 244': '1',  # MOV ESI,ESP => 1
    '137 238': '0',  # MOV ESI,EBP => 0
    '139 245': '1',  # MOV ESI,EBP => 1
    '137 246': '0',  # MOV ESI,ESI => 0
    '139 246': '1',  # MOV ESI,ESI => 1
    '137 254': '0',  # MOV ESI,EDI => 0
    '139 247': '1',  # MOV ESI,EDI => 1
    '137 199': '0',  # MOV EDI,EAX => 0
    '139 248': '1',  # MOV EDI,EAX => 1
    '137 223': '0',  # MOV EDI,EBX => 0
    '139 251': '1',  # MOV EDI,EBX => 1
    '137 207': '0',  # MOV EDI,ECX => 0
    '139 249': '1',  # MOV EDI,ECX => 1
    '137 215': '0',  # MOV EDI,EDX => 0
    '139 250': '1',  # MOV EDI,EDX => 1
    '137 231': '0',  # MOV EDI,ESP => 0
    '139 252': '1',  # MOV EDI,ESP => 1
    '137 239': '0',  # MOV EDI,EBP => 0
    '139 253': '1',  # MOV EDI,EBP => 1
    '137 247': '0',  # MOV EDI,ESI => 0
    '139 254': '1',  # MOV EDI,ESI => 1
    '137 255': '0',  # MOV EDI,EDI => 0
    '139 255': '1',  # MOV EDI,EDI => 1
    '136 228': '0',  # MOV AH,AH => 0
    '138 228': '1',  # MOV AH,AH => 1
    '136 252': '0',  # MOV AH,BH => 0
    '138 231': '1',  # MOV AH,BH => 1
    '136 236': '0',  # MOV AH,CH => 0
    '138 229': '1',  # MOV AH,CH => 1
    '136 244': '0',  # MOV AH,DH => 0
    '138 230': '1',  # MOV AH,DH => 1
    '136 231': '0',  # MOV BH,AH => 0
    '138 252': '1',  # MOV BH,AH => 1
    '136 255': '0',  # MOV BH,BH => 0
    '138 255': '1',  # MOV BH,BH => 1
    '136 239': '0',  # MOV BH,CH => 0
    '138 253': '1',  # MOV BH,CH => 1
    '136 247': '0',  # MOV BH,DH => 0
    '138 254': '1',  # MOV BH,DH => 1
    '136 229': '0',  # MOV CH,AH => 0
    '138 236': '1',  # MOV CH,AH => 1
    '136 253': '0',  # MOV CH,BH => 0
    '138 239': '1',  # MOV CH,BH => 1
    '136 237': '0',  # MOV CH,CH => 0
    '138 237': '1',  # MOV CH,CH => 1
    '136 245': '0',  # MOV CH,DH => 0
    '138 238': '1',  # MOV CH,DH => 1
    '136 230': '0',  # MOV DH,AH => 0
    '138 244': '1',  # MOV DH,AH => 1
    '136 254': '0',  # MOV DH,BH => 0
    '138 247': '1',  # MOV DH,BH => 1
    '136 238': '0',  # MOV DH,CH => 0
    '138 245': '1',  # MOV DH,CH => 1
    '136 246': '0',  # MOV DH,DH => 0
    '138 246': '1',  # MOV DH,DH => 1
    '136 192': '0',  # MOV AL,AL => 0
    '138 192': '1',  # MOV AL,AL => 1
    '136 216': '0',  # MOV AL,BL => 0
    '138 195': '1',  # MOV AL,BL => 1
    '136 200': '0',  # MOV AL,CL => 0
    '138 193': '1',  # MOV AL,CL => 1
    '136 208': '0',  # MOV AL,DL => 0
    '138 194': '1',  # MOV AL,DL => 1
    '136 195': '0',  # MOV BL,AL => 0
    '138 216': '1',  # MOV BL,AL => 1
    '136 219': '0',  # MOV BL,BL => 0
    '138 219': '1',  # MOV BL,BL => 1
    '136 203': '0',  # MOV BL,CL => 0
    '138 217': '1',  # MOV BL,CL => 1
    '136 211': '0',  # MOV BL,DL => 0
    '138 218': '1',  # MOV BL,DL => 1
    '136 193': '0',  # MOV CL,AL => 0
    '138 200': '1',  # MOV CL,AL => 1
    '136 217': '0',  # MOV CL,BL => 0
    '138 203': '1',  # MOV CL,BL => 1
    '136 201': '0',  # MOV CL,CL => 0
    '138 201': '1',  # MOV CL,CL => 1
    '136 209': '0',  # MOV CL,DL => 0
    '138 202': '1',  # MOV CL,DL => 1
    '136 194': '0',  # MOV DL,AL => 0
    '138 208': '1',  # MOV DL,AL => 1
    '136 218': '0',  # MOV DL,BL => 0
    '138 211': '1',  # MOV DL,BL => 1
    '136 202': '0',  # MOV DL,CL => 0
    '138 209': '1',  # MOV DL,CL => 1
    '136 210': '0',  # MOV DL,DL => 0
    '138 210': '1',  # MOV DL,DL => 1
    '1 192': '0',  # ADD EAX,EAX => 0
    '3 192': '1',  # ADD EAX,EAX => 1
    '1 216': '0',  # ADD EAX,EBX => 0
    '3 195': '1',  # ADD EAX,EBX => 1
    '1 200': '0',  # ADD EAX,ECX => 0
    '3 193': '1',  # ADD EAX,ECX => 1
    '1 208': '0',  # ADD EAX,EDX => 0
    '3 194': '1',  # ADD EAX,EDX => 1
    '1 224': '0',  # ADD EAX,ESP => 0
    '3 196': '1',  # ADD EAX,ESP => 1
    '1 232': '0',  # ADD EAX,EBP => 0
    '3 197': '1',  # ADD EAX,EBP => 1
    '1 240': '0',  # ADD EAX,ESI => 0
    '3 198': '1',  # ADD EAX,ESI => 1
    '1 248': '0',  # ADD EAX,EDI => 0
    '3 199': '1',  # ADD EAX,EDI => 1
    '1 195': '0',  # ADD EBX,EAX => 0
    '3 216': '1',  # ADD EBX,EAX => 1
    '1 219': '0',  # ADD EBX,EBX => 0
    '3 219': '1',  # ADD EBX,EBX => 1
    '1 203': '0',  # ADD EBX,ECX => 0
    '3 217': '1',  # ADD EBX,ECX => 1
    '1 211': '0',  # ADD EBX,EDX => 0
    '3 218': '1',  # ADD EBX,EDX => 1
    '1 227': '0',  # ADD EBX,ESP => 0
    '3 220': '1',  # ADD EBX,ESP => 1
    '1 235': '0',  # ADD EBX,EBP => 0
    '3 221': '1',  # ADD EBX,EBP => 1
    '1 243': '0',  # ADD EBX,ESI => 0
    '3 222': '1',  # ADD EBX,ESI => 1
    '1 251': '0',  # ADD EBX,EDI => 0
    '3 223': '1',  # ADD EBX,EDI => 1
    '1 193': '0',  # ADD ECX,EAX => 0
    '3 200': '1',  # ADD ECX,EAX => 1
    '1 217': '0',  # ADD ECX,EBX => 0
    '3 203': '1',  # ADD ECX,EBX => 1
    '1 201': '0',  # ADD ECX,ECX => 0
    '3 201': '1',  # ADD ECX,ECX => 1
    '1 209': '0',  # ADD ECX,EDX => 0
    '3 202': '1',  # ADD ECX,EDX => 1
    '1 225': '0',  # ADD ECX,ESP => 0
    '3 204': '1',  # ADD ECX,ESP => 1
    '1 233': '0',  # ADD ECX,EBP => 0
    '3 205': '1',  # ADD ECX,EBP => 1
    '1 241': '0',  # ADD ECX,ESI => 0
    '3 206': '1',  # ADD ECX,ESI => 1
    '1 249': '0',  # ADD ECX,EDI => 0
    '3 207': '1',  # ADD ECX,EDI => 1
    '1 194': '0',  # ADD EDX,EAX => 0
    '3 208': '1',  # ADD EDX,EAX => 1
    '1 218': '0',  # ADD EDX,EBX => 0
    '3 211': '1',  # ADD EDX,EBX => 1
    '1 202': '0',  # ADD EDX,ECX => 0
    '3 209': '1',  # ADD EDX,ECX => 1
    '1 210': '0',  # ADD EDX,EDX => 0
    '3 210': '1',  # ADD EDX,EDX => 1
    '1 226': '0',  # ADD EDX,ESP => 0
    '3 212': '1',  # ADD EDX,ESP => 1
    '1 234': '0',  # ADD EDX,EBP => 0
    '3 213': '1',  # ADD EDX,EBP => 1
    '1 242': '0',  # ADD EDX,ESI => 0
    '3 214': '1',  # ADD EDX,ESI => 1
    '1 250': '0',  # ADD EDX,EDI => 0
    '3 215': '1',  # ADD EDX,EDI => 1
    '1 196': '0',  # ADD ESP,EAX => 0
    '3 224': '1',  # ADD ESP,EAX => 1
    '1 220': '0',  # ADD ESP,EBX => 0
    '3 227': '1',  # ADD ESP,EBX => 1
    '1 204': '0',  # ADD ESP,ECX => 0
    '3 225': '1',  # ADD ESP,ECX => 1
    '1 212': '0',  # ADD ESP,EDX => 0
    '3 226': '1',  # ADD ESP,EDX => 1
    '1 228': '0',  # ADD ESP,ESP => 0
    '3 228': '1',  # ADD ESP,ESP => 1
    '1 236': '0',  # ADD ESP,EBP => 0
    '3 229': '1',  # ADD ESP,EBP => 1
    '1 244': '0',  # ADD ESP,ESI => 0
    '3 230': '1',  # ADD ESP,ESI => 1
    '1 252': '0',  # ADD ESP,EDI => 0
    '3 231': '1',  # ADD ESP,EDI => 1
    '1 197': '0',  # ADD EBP,EAX => 0
    '3 232': '1',  # ADD EBP,EAX => 1
    '1 221': '0',  # ADD EBP,EBX => 0
    '3 235': '1',  # ADD EBP,EBX => 1
    '1 205': '0',  # ADD EBP,ECX => 0
    '3 233': '1',  # ADD EBP,ECX => 1
    '1 213': '0',  # ADD EBP,EDX => 0
    '3 234': '1',  # ADD EBP,EDX => 1
    '1 229': '0',  # ADD EBP,ESP => 0
    '3 236': '1',  # ADD EBP,ESP => 1
    '1 237': '0',  # ADD EBP,EBP => 0
    '3 237': '1',  # ADD EBP,EBP => 1
    '1 245': '0',  # ADD EBP,ESI => 0
    '3 238': '1',  # ADD EBP,ESI => 1
    '1 253': '0',  # ADD EBP,EDI => 0
    '3 239': '1',  # ADD EBP,EDI => 1
    '1 198': '0',  # ADD ESI,EAX => 0
    '3 240': '1',  # ADD ESI,EAX => 1
    '1 222': '0',  # ADD ESI,EBX => 0
    '3 243': '1',  # ADD ESI,EBX => 1
    '1 206': '0',  # ADD ESI,ECX => 0
    '3 241': '1',  # ADD ESI,ECX => 1
    '1 214': '0',  # ADD ESI,EDX => 0
    '3 242': '1',  # ADD ESI,EDX => 1
    '1 230': '0',  # ADD ESI,ESP => 0
    '3 244': '1',  # ADD ESI,ESP => 1
    '1 238': '0',  # ADD ESI,EBP => 0
    '3 245': '1',  # ADD ESI,EBP => 1
    '1 246': '0',  # ADD ESI,ESI => 0
    '3 246': '1',  # ADD ESI,ESI => 1
    '1 254': '0',  # ADD ESI,EDI => 0
    '3 247': '1',  # ADD ESI,EDI => 1
    '1 199': '0',  # ADD EDI,EAX => 0
    '3 248': '1',  # ADD EDI,EAX => 1
    '1 223': '0',  # ADD EDI,EBX => 0
    '3 251': '1',  # ADD EDI,EBX => 1
    '1 207': '0',  # ADD EDI,ECX => 0
    '3 249': '1',  # ADD EDI,ECX => 1
    '1 215': '0',  # ADD EDI,EDX => 0
    '3 250': '1',  # ADD EDI,EDX => 1
    '1 231': '0',  # ADD EDI,ESP => 0
    '3 252': '1',  # ADD EDI,ESP => 1
    '1 239': '0',  # ADD EDI,EBP => 0
    '3 253': '1',  # ADD EDI,EBP => 1
    '1 247': '0',  # ADD EDI,ESI => 0
    '3 254': '1',  # ADD EDI,ESI => 1
    '1 255': '0',  # ADD EDI,EDI => 0
    '3 255': '1',  # ADD EDI,EDI => 1
    '0 228': '0',  # ADD AH,AH => 0
    '2 228': '1',  # ADD AH,AH => 1
    '0 252': '0',  # ADD AH,BH => 0
    '2 231': '1',  # ADD AH,BH => 1
    '0 236': '0',  # ADD AH,CH => 0
    '2 229': '1',  # ADD AH,CH => 1
    '0 244': '0',  # ADD AH,DH => 0
    '2 230': '1',  # ADD AH,DH => 1
    '0 231': '0',  # ADD BH,AH => 0
    '2 252': '1',  # ADD BH,AH => 1
    '0 255': '0',  # ADD BH,BH => 0
    '2 255': '1',  # ADD BH,BH => 1
    '0 239': '0',  # ADD BH,CH => 0
    '2 253': '1',  # ADD BH,CH => 1
    '0 247': '0',  # ADD BH,DH => 0
    '2 254': '1',  # ADD BH,DH => 1
    '0 229': '0',  # ADD CH,AH => 0
    '2 236': '1',  # ADD CH,AH => 1
    '0 253': '0',  # ADD CH,BH => 0
    '2 239': '1',  # ADD CH,BH => 1
    '0 237': '0',  # ADD CH,CH => 0
    '2 237': '1',  # ADD CH,CH => 1
    '0 245': '0',  # ADD CH,DH => 0
    '2 238': '1',  # ADD CH,DH => 1
    '0 230': '0',  # ADD DH,AH => 0
    '2 244': '1',  # ADD DH,AH => 1
    '0 254': '0',  # ADD DH,BH => 0
    '2 247': '1',  # ADD DH,BH => 1
    '0 238': '0',  # ADD DH,CH => 0
    '2 245': '1',  # ADD DH,CH => 1
    '0 246': '0',  # ADD DH,DH => 0
    '2 246': '1',  # ADD DH,DH => 1
    '0 192': '0',  # ADD AL,AL => 0
    '2 192': '1',  # ADD AL,AL => 1
    '0 216': '0',  # ADD AL,BL => 0
    '2 195': '1',  # ADD AL,BL => 1
    '0 200': '0',  # ADD AL,CL => 0
    '2 193': '1',  # ADD AL,CL => 1
    '0 208': '0',  # ADD AL,DL => 0
    '2 194': '1',  # ADD AL,DL => 1
    '0 195': '0',  # ADD BL,AL => 0
    '2 216': '1',  # ADD BL,AL => 1
    '0 219': '0',  # ADD BL,BL => 0
    '2 219': '1',  # ADD BL,BL => 1
    '0 203': '0',  # ADD BL,CL => 0
    '2 217': '1',  # ADD BL,CL => 1
    '0 211': '0',  # ADD BL,DL => 0
    '2 218': '1',  # ADD BL,DL => 1
    '0 193': '0',  # ADD CL,AL => 0
    '2 200': '1',  # ADD CL,AL => 1
    '0 217': '0',  # ADD CL,BL => 0
    '2 203': '1',  # ADD CL,BL => 1
    '0 201': '0',  # ADD CL,CL => 0
    '2 201': '1',  # ADD CL,CL => 1
    '0 209': '0',  # ADD CL,DL => 0
    '2 202': '1',  # ADD CL,DL => 1
    '0 194': '0',  # ADD DL,AL => 0
    '2 208': '1',  # ADD DL,AL => 1
    '0 218': '0',  # ADD DL,BL => 0
    '2 211': '1',  # ADD DL,BL => 1
    '0 202': '0',  # ADD DL,CL => 0
    '2 209': '1',  # ADD DL,CL => 1
    '0 210': '0',  # ADD DL,DL => 0
    '2 210': '1',  # ADD DL,DL => 1
    '17 192': '0',  # ADC EAX,EAX => 0
    '19 192': '1',  # ADC EAX,EAX => 1
    '17 216': '0',  # ADC EAX,EBX => 0
    '19 195': '1',  # ADC EAX,EBX => 1
    '17 200': '0',  # ADC EAX,ECX => 0
    '19 193': '1',  # ADC EAX,ECX => 1
    '17 208': '0',  # ADC EAX,EDX => 0
    '19 194': '1',  # ADC EAX,EDX => 1
    '17 224': '0',  # ADC EAX,ESP => 0
    '19 196': '1',  # ADC EAX,ESP => 1
    '17 232': '0',  # ADC EAX,EBP => 0
    '19 197': '1',  # ADC EAX,EBP => 1
    '17 240': '0',  # ADC EAX,ESI => 0
    '19 198': '1',  # ADC EAX,ESI => 1
    '17 248': '0',  # ADC EAX,EDI => 0
    '19 199': '1',  # ADC EAX,EDI => 1
    '17 195': '0',  # ADC EBX,EAX => 0
    '19 216': '1',  # ADC EBX,EAX => 1
    '17 219': '0',  # ADC EBX,EBX => 0
    '19 219': '1',  # ADC EBX,EBX => 1
    '17 203': '0',  # ADC EBX,ECX => 0
    '19 217': '1',  # ADC EBX,ECX => 1
    '17 211': '0',  # ADC EBX,EDX => 0
    '19 218': '1',  # ADC EBX,EDX => 1
    '17 227': '0',  # ADC EBX,ESP => 0
    '19 220': '1',  # ADC EBX,ESP => 1
    '17 235': '0',  # ADC EBX,EBP => 0
    '19 221': '1',  # ADC EBX,EBP => 1
    '17 243': '0',  # ADC EBX,ESI => 0
    '19 222': '1',  # ADC EBX,ESI => 1
    '17 251': '0',  # ADC EBX,EDI => 0
    '19 223': '1',  # ADC EBX,EDI => 1
    '17 193': '0',  # ADC ECX,EAX => 0
    '19 200': '1',  # ADC ECX,EAX => 1
    '17 217': '0',  # ADC ECX,EBX => 0
    '19 203': '1',  # ADC ECX,EBX => 1
    '17 201': '0',  # ADC ECX,ECX => 0
    '19 201': '1',  # ADC ECX,ECX => 1
    '17 209': '0',  # ADC ECX,EDX => 0
    '19 202': '1',  # ADC ECX,EDX => 1
    '17 225': '0',  # ADC ECX,ESP => 0
    '19 204': '1',  # ADC ECX,ESP => 1
    '17 233': '0',  # ADC ECX,EBP => 0
    '19 205': '1',  # ADC ECX,EBP => 1
    '17 241': '0',  # ADC ECX,ESI => 0
    '19 206': '1',  # ADC ECX,ESI => 1
    '17 249': '0',  # ADC ECX,EDI => 0
    '19 207': '1',  # ADC ECX,EDI => 1
    '17 194': '0',  # ADC EDX,EAX => 0
    '19 208': '1',  # ADC EDX,EAX => 1
    '17 218': '0',  # ADC EDX,EBX => 0
    '19 211': '1',  # ADC EDX,EBX => 1
    '17 202': '0',  # ADC EDX,ECX => 0
    '19 209': '1',  # ADC EDX,ECX => 1
    '17 210': '0',  # ADC EDX,EDX => 0
    '19 210': '1',  # ADC EDX,EDX => 1
    '17 226': '0',  # ADC EDX,ESP => 0
    '19 212': '1',  # ADC EDX,ESP => 1
    '17 234': '0',  # ADC EDX,EBP => 0
    '19 213': '1',  # ADC EDX,EBP => 1
    '17 242': '0',  # ADC EDX,ESI => 0
    '19 214': '1',  # ADC EDX,ESI => 1
    '17 250': '0',  # ADC EDX,EDI => 0
    '19 215': '1',  # ADC EDX,EDI => 1
    '17 196': '0',  # ADC ESP,EAX => 0
    '19 224': '1',  # ADC ESP,EAX => 1
    '17 220': '0',  # ADC ESP,EBX => 0
    '19 227': '1',  # ADC ESP,EBX => 1
    '17 204': '0',  # ADC ESP,ECX => 0
    '19 225': '1',  # ADC ESP,ECX => 1
    '17 212': '0',  # ADC ESP,EDX => 0
    '19 226': '1',  # ADC ESP,EDX => 1
    '17 228': '0',  # ADC ESP,ESP => 0
    '19 228': '1',  # ADC ESP,ESP => 1
    '17 236': '0',  # ADC ESP,EBP => 0
    '19 229': '1',  # ADC ESP,EBP => 1
    '17 244': '0',  # ADC ESP,ESI => 0
    '19 230': '1',  # ADC ESP,ESI => 1
    '17 252': '0',  # ADC ESP,EDI => 0
    '19 231': '1',  # ADC ESP,EDI => 1
    '17 197': '0',  # ADC EBP,EAX => 0
    '19 232': '1',  # ADC EBP,EAX => 1
    '17 221': '0',  # ADC EBP,EBX => 0
    '19 235': '1',  # ADC EBP,EBX => 1
    '17 205': '0',  # ADC EBP,ECX => 0
    '19 233': '1',  # ADC EBP,ECX => 1
    '17 213': '0',  # ADC EBP,EDX => 0
    '19 234': '1',  # ADC EBP,EDX => 1
    '17 229': '0',  # ADC EBP,ESP => 0
    '19 236': '1',  # ADC EBP,ESP => 1
    '17 237': '0',  # ADC EBP,EBP => 0
    '19 237': '1',  # ADC EBP,EBP => 1
    '17 245': '0',  # ADC EBP,ESI => 0
    '19 238': '1',  # ADC EBP,ESI => 1
    '17 253': '0',  # ADC EBP,EDI => 0
    '19 239': '1',  # ADC EBP,EDI => 1
    '17 198': '0',  # ADC ESI,EAX => 0
    '19 240': '1',  # ADC ESI,EAX => 1
    '17 222': '0',  # ADC ESI,EBX => 0
    '19 243': '1',  # ADC ESI,EBX => 1
    '17 206': '0',  # ADC ESI,ECX => 0
    '19 241': '1',  # ADC ESI,ECX => 1
    '17 214': '0',  # ADC ESI,EDX => 0
    '19 242': '1',  # ADC ESI,EDX => 1
    '17 230': '0',  # ADC ESI,ESP => 0
    '19 244': '1',  # ADC ESI,ESP => 1
    '17 238': '0',  # ADC ESI,EBP => 0
    '19 245': '1',  # ADC ESI,EBP => 1
    '17 246': '0',  # ADC ESI,ESI => 0
    '19 246': '1',  # ADC ESI,ESI => 1
    '17 254': '0',  # ADC ESI,EDI => 0
    '19 247': '1',  # ADC ESI,EDI => 1
    '17 199': '0',  # ADC EDI,EAX => 0
    '19 248': '1',  # ADC EDI,EAX => 1
    '17 223': '0',  # ADC EDI,EBX => 0
    '19 251': '1',  # ADC EDI,EBX => 1
    '17 207': '0',  # ADC EDI,ECX => 0
    '19 249': '1',  # ADC EDI,ECX => 1
    '17 215': '0',  # ADC EDI,EDX => 0
    '19 250': '1',  # ADC EDI,EDX => 1
    '17 231': '0',  # ADC EDI,ESP => 0
    '19 252': '1',  # ADC EDI,ESP => 1
    '17 239': '0',  # ADC EDI,EBP => 0
    '19 253': '1',  # ADC EDI,EBP => 1
    '17 247': '0',  # ADC EDI,ESI => 0
    '19 254': '1',  # ADC EDI,ESI => 1
    '17 255': '0',  # ADC EDI,EDI => 0
    '19 255': '1',  # ADC EDI,EDI => 1
    '16 228': '0',  # ADC AH,AH => 0
    '18 228': '1',  # ADC AH,AH => 1
    '16 252': '0',  # ADC AH,BH => 0
    '18 231': '1',  # ADC AH,BH => 1
    '16 236': '0',  # ADC AH,CH => 0
    '18 229': '1',  # ADC AH,CH => 1
    '16 244': '0',  # ADC AH,DH => 0
    '18 230': '1',  # ADC AH,DH => 1
    '16 231': '0',  # ADC BH,AH => 0
    '18 252': '1',  # ADC BH,AH => 1
    '16 255': '0',  # ADC BH,BH => 0
    '18 255': '1',  # ADC BH,BH => 1
    '16 239': '0',  # ADC BH,CH => 0
    '18 253': '1',  # ADC BH,CH => 1
    '16 247': '0',  # ADC BH,DH => 0
    '18 254': '1',  # ADC BH,DH => 1
    '16 229': '0',  # ADC CH,AH => 0
    '18 236': '1',  # ADC CH,AH => 1
    '16 253': '0',  # ADC CH,BH => 0
    '18 239': '1',  # ADC CH,BH => 1
    '16 237': '0',  # ADC CH,CH => 0
    '18 237': '1',  # ADC CH,CH => 1
    '16 245': '0',  # ADC CH,DH => 0
    '18 238': '1',  # ADC CH,DH => 1
    '16 230': '0',  # ADC DH,AH => 0
    '18 244': '1',  # ADC DH,AH => 1
    '16 254': '0',  # ADC DH,BH => 0
    '18 247': '1',  # ADC DH,BH => 1
    '16 238': '0',  # ADC DH,CH => 0
    '18 245': '1',  # ADC DH,CH => 1
    '16 246': '0',  # ADC DH,DH => 0
    '18 246': '1',  # ADC DH,DH => 1
    '16 192': '0',  # ADC AL,AL => 0
    '18 192': '1',  # ADC AL,AL => 1
    '16 216': '0',  # ADC AL,BL => 0
    '18 195': '1',  # ADC AL,BL => 1
    '16 200': '0',  # ADC AL,CL => 0
    '18 193': '1',  # ADC AL,CL => 1
    '16 208': '0',  # ADC AL,DL => 0
    '18 194': '1',  # ADC AL,DL => 1
    '16 195': '0',  # ADC BL,AL => 0
    '18 216': '1',  # ADC BL,AL => 1
    '16 219': '0',  # ADC BL,BL => 0
    '18 219': '1',  # ADC BL,BL => 1
    '16 203': '0',  # ADC BL,CL => 0
    '18 217': '1',  # ADC BL,CL => 1
    '16 211': '0',  # ADC BL,DL => 0
    '18 218': '1',  # ADC BL,DL => 1
    '16 193': '0',  # ADC CL,AL => 0
    '18 200': '1',  # ADC CL,AL => 1
    '16 217': '0',  # ADC CL,BL => 0
    '18 203': '1',  # ADC CL,BL => 1
    '16 201': '0',  # ADC CL,CL => 0
    '18 201': '1',  # ADC CL,CL => 1
    '16 209': '0',  # ADC CL,DL => 0
    '18 202': '1',  # ADC CL,DL => 1
    '16 194': '0',  # ADC DL,AL => 0
    '18 208': '1',  # ADC DL,AL => 1
    '16 218': '0',  # ADC DL,BL => 0
    '18 211': '1',  # ADC DL,BL => 1
    '16 202': '0',  # ADC DL,CL => 0
    '18 209': '1',  # ADC DL,CL => 1
    '16 210': '0',  # ADC DL,DL => 0
    '18 210': '1',  # ADC DL,DL => 1
    '33 192': '0',  # AND EAX,EAX => 0
    '35 192': '1',  # AND EAX,EAX => 1
    '33 216': '0',  # AND EAX,EBX => 0
    '35 195': '1',  # AND EAX,EBX => 1
    '33 200': '0',  # AND EAX,ECX => 0
    '35 193': '1',  # AND EAX,ECX => 1
    '33 208': '0',  # AND EAX,EDX => 0
    '35 194': '1',  # AND EAX,EDX => 1
    '33 224': '0',  # AND EAX,ESP => 0
    '35 196': '1',  # AND EAX,ESP => 1
    '33 232': '0',  # AND EAX,EBP => 0
    '35 197': '1',  # AND EAX,EBP => 1
    '33 240': '0',  # AND EAX,ESI => 0
    '35 198': '1',  # AND EAX,ESI => 1
    '33 248': '0',  # AND EAX,EDI => 0
    '35 199': '1',  # AND EAX,EDI => 1
    '33 195': '0',  # AND EBX,EAX => 0
    '35 216': '1',  # AND EBX,EAX => 1
    '33 219': '0',  # AND EBX,EBX => 0
    '35 219': '1',  # AND EBX,EBX => 1
    '33 203': '0',  # AND EBX,ECX => 0
    '35 217': '1',  # AND EBX,ECX => 1
    '33 211': '0',  # AND EBX,EDX => 0
    '35 218': '1',  # AND EBX,EDX => 1
    '33 227': '0',  # AND EBX,ESP => 0
    '35 220': '1',  # AND EBX,ESP => 1
    '33 235': '0',  # AND EBX,EBP => 0
    '35 221': '1',  # AND EBX,EBP => 1
    '33 243': '0',  # AND EBX,ESI => 0
    '35 222': '1',  # AND EBX,ESI => 1
    '33 251': '0',  # AND EBX,EDI => 0
    '35 223': '1',  # AND EBX,EDI => 1
    '33 193': '0',  # AND ECX,EAX => 0
    '35 200': '1',  # AND ECX,EAX => 1
    '33 217': '0',  # AND ECX,EBX => 0
    '35 203': '1',  # AND ECX,EBX => 1
    '33 201': '0',  # AND ECX,ECX => 0
    '35 201': '1',  # AND ECX,ECX => 1
    '33 209': '0',  # AND ECX,EDX => 0
    '35 202': '1',  # AND ECX,EDX => 1
    '33 225': '0',  # AND ECX,ESP => 0
    '35 204': '1',  # AND ECX,ESP => 1
    '33 233': '0',  # AND ECX,EBP => 0
    '35 205': '1',  # AND ECX,EBP => 1
    '33 241': '0',  # AND ECX,ESI => 0
    '35 206': '1',  # AND ECX,ESI => 1
    '33 249': '0',  # AND ECX,EDI => 0
    '35 207': '1',  # AND ECX,EDI => 1
    '33 194': '0',  # AND EDX,EAX => 0
    '35 208': '1',  # AND EDX,EAX => 1
    '33 218': '0',  # AND EDX,EBX => 0
    '35 211': '1',  # AND EDX,EBX => 1
    '33 202': '0',  # AND EDX,ECX => 0
    '35 209': '1',  # AND EDX,ECX => 1
    '33 210': '0',  # AND EDX,EDX => 0
    '35 210': '1',  # AND EDX,EDX => 1
    '33 226': '0',  # AND EDX,ESP => 0
    '35 212': '1',  # AND EDX,ESP => 1
    '33 234': '0',  # AND EDX,EBP => 0
    '35 213': '1',  # AND EDX,EBP => 1
    '33 242': '0',  # AND EDX,ESI => 0
    '35 214': '1',  # AND EDX,ESI => 1
    '33 250': '0',  # AND EDX,EDI => 0
    '35 215': '1',  # AND EDX,EDI => 1
    '33 196': '0',  # AND ESP,EAX => 0
    '35 224': '1',  # AND ESP,EAX => 1
    '33 220': '0',  # AND ESP,EBX => 0
    '35 227': '1',  # AND ESP,EBX => 1
    '33 204': '0',  # AND ESP,ECX => 0
    '35 225': '1',  # AND ESP,ECX => 1
    '33 212': '0',  # AND ESP,EDX => 0
    '35 226': '1',  # AND ESP,EDX => 1
    '33 228': '0',  # AND ESP,ESP => 0
    '35 228': '1',  # AND ESP,ESP => 1
    '33 236': '0',  # AND ESP,EBP => 0
    '35 229': '1',  # AND ESP,EBP => 1
    '33 244': '0',  # AND ESP,ESI => 0
    '35 230': '1',  # AND ESP,ESI => 1
    '33 252': '0',  # AND ESP,EDI => 0
    '35 231': '1',  # AND ESP,EDI => 1
    '33 197': '0',  # AND EBP,EAX => 0
    '35 232': '1',  # AND EBP,EAX => 1
    '33 221': '0',  # AND EBP,EBX => 0
    '35 235': '1',  # AND EBP,EBX => 1
    '33 205': '0',  # AND EBP,ECX => 0
    '35 233': '1',  # AND EBP,ECX => 1
    '33 213': '0',  # AND EBP,EDX => 0
    '35 234': '1',  # AND EBP,EDX => 1
    '33 229': '0',  # AND EBP,ESP => 0
    '35 236': '1',  # AND EBP,ESP => 1
    '33 237': '0',  # AND EBP,EBP => 0
    '35 237': '1',  # AND EBP,EBP => 1
    '33 245': '0',  # AND EBP,ESI => 0
    '35 238': '1',  # AND EBP,ESI => 1
    '33 253': '0',  # AND EBP,EDI => 0
    '35 239': '1',  # AND EBP,EDI => 1
    '33 198': '0',  # AND ESI,EAX => 0
    '35 240': '1',  # AND ESI,EAX => 1
    '33 222': '0',  # AND ESI,EBX => 0
    '35 243': '1',  # AND ESI,EBX => 1
    '33 206': '0',  # AND ESI,ECX => 0
    '35 241': '1',  # AND ESI,ECX => 1
    '33 214': '0',  # AND ESI,EDX => 0
    '35 242': '1',  # AND ESI,EDX => 1
    '33 230': '0',  # AND ESI,ESP => 0
    '35 244': '1',  # AND ESI,ESP => 1
    '33 238': '0',  # AND ESI,EBP => 0
    '35 245': '1',  # AND ESI,EBP => 1
    '33 246': '0',  # AND ESI,ESI => 0
    '35 246': '1',  # AND ESI,ESI => 1
    '33 254': '0',  # AND ESI,EDI => 0
    '35 247': '1',  # AND ESI,EDI => 1
    '33 199': '0',  # AND EDI,EAX => 0
    '35 248': '1',  # AND EDI,EAX => 1
    '33 223': '0',  # AND EDI,EBX => 0
    '35 251': '1',  # AND EDI,EBX => 1
    '33 207': '0',  # AND EDI,ECX => 0
    '35 249': '1',  # AND EDI,ECX => 1
    '33 215': '0',  # AND EDI,EDX => 0
    '35 250': '1',  # AND EDI,EDX => 1
    '33 231': '0',  # AND EDI,ESP => 0
    '35 252': '1',  # AND EDI,ESP => 1
    '33 239': '0',  # AND EDI,EBP => 0
    '35 253': '1',  # AND EDI,EBP => 1
    '33 247': '0',  # AND EDI,ESI => 0
    '35 254': '1',  # AND EDI,ESI => 1
    '33 255': '0',  # AND EDI,EDI => 0
    '35 255': '1',  # AND EDI,EDI => 1
    '32 228': '0',  # AND AH,AH => 0
    '34 228': '1',  # AND AH,AH => 1
    '32 252': '0',  # AND AH,BH => 0
    '34 231': '1',  # AND AH,BH => 1
    '32 236': '0',  # AND AH,CH => 0
    '34 229': '1',  # AND AH,CH => 1
    '32 244': '0',  # AND AH,DH => 0
    '34 230': '1',  # AND AH,DH => 1
    '32 231': '0',  # AND BH,AH => 0
    '34 252': '1',  # AND BH,AH => 1
    '32 255': '0',  # AND BH,BH => 0
    '34 255': '1',  # AND BH,BH => 1
    '32 239': '0',  # AND BH,CH => 0
    '34 253': '1',  # AND BH,CH => 1
    '32 247': '0',  # AND BH,DH => 0
    '34 254': '1',  # AND BH,DH => 1
    '32 229': '0',  # AND CH,AH => 0
    '34 236': '1',  # AND CH,AH => 1
    '32 253': '0',  # AND CH,BH => 0
    '34 239': '1',  # AND CH,BH => 1
    '32 237': '0',  # AND CH,CH => 0
    '34 237': '1',  # AND CH,CH => 1
    '32 245': '0',  # AND CH,DH => 0
    '34 238': '1',  # AND CH,DH => 1
    '32 230': '0',  # AND DH,AH => 0
    '34 244': '1',  # AND DH,AH => 1
    '32 254': '0',  # AND DH,BH => 0
    '34 247': '1',  # AND DH,BH => 1
    '32 238': '0',  # AND DH,CH => 0
    '34 245': '1',  # AND DH,CH => 1
    '32 246': '0',  # AND DH,DH => 0
    '34 246': '1',  # AND DH,DH => 1
    '32 192': '0',  # AND AL,AL => 0
    '34 192': '1',  # AND AL,AL => 1
    '32 216': '0',  # AND AL,BL => 0
    '34 195': '1',  # AND AL,BL => 1
    '32 200': '0',  # AND AL,CL => 0
    '34 193': '1',  # AND AL,CL => 1
    '32 208': '0',  # AND AL,DL => 0
    '34 194': '1',  # AND AL,DL => 1
    '32 195': '0',  # AND BL,AL => 0
    '34 216': '1',  # AND BL,AL => 1
    '32 219': '0',  # AND BL,BL => 0
    '34 219': '1',  # AND BL,BL => 1
    '32 203': '0',  # AND BL,CL => 0
    '34 217': '1',  # AND BL,CL => 1
    '32 211': '0',  # AND BL,DL => 0
    '34 218': '1',  # AND BL,DL => 1
    '32 193': '0',  # AND CL,AL => 0
    '34 200': '1',  # AND CL,AL => 1
    '32 217': '0',  # AND CL,BL => 0
    '34 203': '1',  # AND CL,BL => 1
    '32 201': '0',  # AND CL,CL => 0
    '34 201': '1',  # AND CL,CL => 1
    '32 209': '0',  # AND CL,DL => 0
    '34 202': '1',  # AND CL,DL => 1
    '32 194': '0',  # AND DL,AL => 0
    '34 208': '1',  # AND DL,AL => 1
    '32 218': '0',  # AND DL,BL => 0
    '34 211': '1',  # AND DL,BL => 1
    '32 202': '0',  # AND DL,CL => 0
    '34 209': '1',  # AND DL,CL => 1
    '32 210': '0',  # AND DL,DL => 0
    '34 210': '1',  # AND DL,DL => 1
    '9 192': '0',  # OR EAX,EAX => 0
    '11 192': '1',  # OR EAX,EAX => 1
    '9 216': '0',  # OR EAX,EBX => 0
    '11 195': '1',  # OR EAX,EBX => 1
    '9 200': '0',  # OR EAX,ECX => 0
    '11 193': '1',  # OR EAX,ECX => 1
    '9 208': '0',  # OR EAX,EDX => 0
    '11 194': '1',  # OR EAX,EDX => 1
    '9 224': '0',  # OR EAX,ESP => 0
    '11 196': '1',  # OR EAX,ESP => 1
    '9 232': '0',  # OR EAX,EBP => 0
    '11 197': '1',  # OR EAX,EBP => 1
    '9 240': '0',  # OR EAX,ESI => 0
    '11 198': '1',  # OR EAX,ESI => 1
    '9 248': '0',  # OR EAX,EDI => 0
    '11 199': '1',  # OR EAX,EDI => 1
    '9 195': '0',  # OR EBX,EAX => 0
    '11 216': '1',  # OR EBX,EAX => 1
    '9 219': '0',  # OR EBX,EBX => 0
    '11 219': '1',  # OR EBX,EBX => 1
    '9 203': '0',  # OR EBX,ECX => 0
    '11 217': '1',  # OR EBX,ECX => 1
    '9 211': '0',  # OR EBX,EDX => 0
    '11 218': '1',  # OR EBX,EDX => 1
    '9 227': '0',  # OR EBX,ESP => 0
    '11 220': '1',  # OR EBX,ESP => 1
    '9 235': '0',  # OR EBX,EBP => 0
    '11 221': '1',  # OR EBX,EBP => 1
    '9 243': '0',  # OR EBX,ESI => 0
    '11 222': '1',  # OR EBX,ESI => 1
    '9 251': '0',  # OR EBX,EDI => 0
    '11 223': '1',  # OR EBX,EDI => 1
    '9 193': '0',  # OR ECX,EAX => 0
    '11 200': '1',  # OR ECX,EAX => 1
    '9 217': '0',  # OR ECX,EBX => 0
    '11 203': '1',  # OR ECX,EBX => 1
    '9 201': '0',  # OR ECX,ECX => 0
    '11 201': '1',  # OR ECX,ECX => 1
    '9 209': '0',  # OR ECX,EDX => 0
    '11 202': '1',  # OR ECX,EDX => 1
    '9 225': '0',  # OR ECX,ESP => 0
    '11 204': '1',  # OR ECX,ESP => 1
    '9 233': '0',  # OR ECX,EBP => 0
    '11 205': '1',  # OR ECX,EBP => 1
    '9 241': '0',  # OR ECX,ESI => 0
    '11 206': '1',  # OR ECX,ESI => 1
    '9 249': '0',  # OR ECX,EDI => 0
    '11 207': '1',  # OR ECX,EDI => 1
    '9 194': '0',  # OR EDX,EAX => 0
    '11 208': '1',  # OR EDX,EAX => 1
    '9 218': '0',  # OR EDX,EBX => 0
    '11 211': '1',  # OR EDX,EBX => 1
    '9 202': '0',  # OR EDX,ECX => 0
    '11 209': '1',  # OR EDX,ECX => 1
    '9 210': '0',  # OR EDX,EDX => 0
    '11 210': '1',  # OR EDX,EDX => 1
    '9 226': '0',  # OR EDX,ESP => 0
    '11 212': '1',  # OR EDX,ESP => 1
    '9 234': '0',  # OR EDX,EBP => 0
    '11 213': '1',  # OR EDX,EBP => 1
    '9 242': '0',  # OR EDX,ESI => 0
    '11 214': '1',  # OR EDX,ESI => 1
    '9 250': '0',  # OR EDX,EDI => 0
    '11 215': '1',  # OR EDX,EDI => 1
    '9 196': '0',  # OR ESP,EAX => 0
    '11 224': '1',  # OR ESP,EAX => 1
    '9 220': '0',  # OR ESP,EBX => 0
    '11 227': '1',  # OR ESP,EBX => 1
    '9 204': '0',  # OR ESP,ECX => 0
    '11 225': '1',  # OR ESP,ECX => 1
    '9 212': '0',  # OR ESP,EDX => 0
    '11 226': '1',  # OR ESP,EDX => 1
    '9 228': '0',  # OR ESP,ESP => 0
    '11 228': '1',  # OR ESP,ESP => 1
    '9 236': '0',  # OR ESP,EBP => 0
    '11 229': '1',  # OR ESP,EBP => 1
    '9 244': '0',  # OR ESP,ESI => 0
    '11 230': '1',  # OR ESP,ESI => 1
    '9 252': '0',  # OR ESP,EDI => 0
    '11 231': '1',  # OR ESP,EDI => 1
    '9 197': '0',  # OR EBP,EAX => 0
    '11 232': '1',  # OR EBP,EAX => 1
    '9 221': '0',  # OR EBP,EBX => 0
    '11 235': '1',  # OR EBP,EBX => 1
    '9 205': '0',  # OR EBP,ECX => 0
    '11 233': '1',  # OR EBP,ECX => 1
    '9 213': '0',  # OR EBP,EDX => 0
    '11 234': '1',  # OR EBP,EDX => 1
    '9 229': '0',  # OR EBP,ESP => 0
    '11 236': '1',  # OR EBP,ESP => 1
    '9 237': '0',  # OR EBP,EBP => 0
    '11 237': '1',  # OR EBP,EBP => 1
    '9 245': '0',  # OR EBP,ESI => 0
    '11 238': '1',  # OR EBP,ESI => 1
    '9 253': '0',  # OR EBP,EDI => 0
    '11 239': '1',  # OR EBP,EDI => 1
    '9 198': '0',  # OR ESI,EAX => 0
    '11 240': '1',  # OR ESI,EAX => 1
    '9 222': '0',  # OR ESI,EBX => 0
    '11 243': '1',  # OR ESI,EBX => 1
    '9 206': '0',  # OR ESI,ECX => 0
    '11 241': '1',  # OR ESI,ECX => 1
    '9 214': '0',  # OR ESI,EDX => 0
    '11 242': '1',  # OR ESI,EDX => 1
    '9 230': '0',  # OR ESI,ESP => 0
    '11 244': '1',  # OR ESI,ESP => 1
    '9 238': '0',  # OR ESI,EBP => 0
    '11 245': '1',  # OR ESI,EBP => 1
    '9 246': '0',  # OR ESI,ESI => 0
    '11 246': '1',  # OR ESI,ESI => 1
    '9 254': '0',  # OR ESI,EDI => 0
    '11 247': '1',  # OR ESI,EDI => 1
    '9 199': '0',  # OR EDI,EAX => 0
    '11 248': '1',  # OR EDI,EAX => 1
    '9 223': '0',  # OR EDI,EBX => 0
    '11 251': '1',  # OR EDI,EBX => 1
    '9 207': '0',  # OR EDI,ECX => 0
    '11 249': '1',  # OR EDI,ECX => 1
    '9 215': '0',  # OR EDI,EDX => 0
    '11 250': '1',  # OR EDI,EDX => 1
    '9 231': '0',  # OR EDI,ESP => 0
    '11 252': '1',  # OR EDI,ESP => 1
    '9 239': '0',  # OR EDI,EBP => 0
    '11 253': '1',  # OR EDI,EBP => 1
    '9 247': '0',  # OR EDI,ESI => 0
    '11 254': '1',  # OR EDI,ESI => 1
    '9 255': '0',  # OR EDI,EDI => 0
    '11 255': '1',  # OR EDI,EDI => 1
    '8 228': '0',  # OR AH,AH => 0
    '10 228': '1',  # OR AH,AH => 1
    '8 252': '0',  # OR AH,BH => 0
    '10 231': '1',  # OR AH,BH => 1
    '8 236': '0',  # OR AH,CH => 0
    '10 229': '1',  # OR AH,CH => 1
    '8 244': '0',  # OR AH,DH => 0
    '10 230': '1',  # OR AH,DH => 1
    '8 231': '0',  # OR BH,AH => 0
    '10 252': '1',  # OR BH,AH => 1
    '8 255': '0',  # OR BH,BH => 0
    '10 255': '1',  # OR BH,BH => 1
    '8 239': '0',  # OR BH,CH => 0
    '10 253': '1',  # OR BH,CH => 1
    '8 247': '0',  # OR BH,DH => 0
    '10 254': '1',  # OR BH,DH => 1
    '8 229': '0',  # OR CH,AH => 0
    '10 236': '1',  # OR CH,AH => 1
    '8 253': '0',  # OR CH,BH => 0
    '10 239': '1',  # OR CH,BH => 1
    '8 237': '0',  # OR CH,CH => 0
    '10 237': '1',  # OR CH,CH => 1
    '8 245': '0',  # OR CH,DH => 0
    '10 238': '1',  # OR CH,DH => 1
    '8 230': '0',  # OR DH,AH => 0
    '10 244': '1',  # OR DH,AH => 1
    '8 254': '0',  # OR DH,BH => 0
    '10 247': '1',  # OR DH,BH => 1
    '8 238': '0',  # OR DH,CH => 0
    '10 245': '1',  # OR DH,CH => 1
    '8 246': '0',  # OR DH,DH => 0
    '10 246': '1',  # OR DH,DH => 1
    '8 192': '0',  # OR AL,AL => 0
    '10 192': '1',  # OR AL,AL => 1
    '8 216': '0',  # OR AL,BL => 0
    '10 195': '1',  # OR AL,BL => 1
    '8 200': '0',  # OR AL,CL => 0
    '10 193': '1',  # OR AL,CL => 1
    '8 208': '0',  # OR AL,DL => 0
    '10 194': '1',  # OR AL,DL => 1
    '8 195': '0',  # OR BL,AL => 0
    '10 216': '1',  # OR BL,AL => 1
    '8 219': '0',  # OR BL,BL => 0
    '10 219': '1',  # OR BL,BL => 1
    '8 203': '0',  # OR BL,CL => 0
    '10 217': '1',  # OR BL,CL => 1
    '8 211': '0',  # OR BL,DL => 0
    '10 218': '1',  # OR BL,DL => 1
    '8 193': '0',  # OR CL,AL => 0
    '10 200': '1',  # OR CL,AL => 1
    '8 217': '0',  # OR CL,BL => 0
    '10 203': '1',  # OR CL,BL => 1
    '8 201': '0',  # OR CL,CL => 0
    '10 201': '1',  # OR CL,CL => 1
    '8 209': '0',  # OR CL,DL => 0
    '10 202': '1',  # OR CL,DL => 1
    '8 194': '0',  # OR DL,AL => 0
    '10 208': '1',  # OR DL,AL => 1
    '8 218': '0',  # OR DL,BL => 0
    '10 211': '1',  # OR DL,BL => 1
    '8 202': '0',  # OR DL,CL => 0
    '10 209': '1',  # OR DL,CL => 1
    '8 210': '0',  # OR DL,DL => 0
    '10 210': '1',  # OR DL,DL => 1
    '25 192': '0',  # SBB EAX,EAX => 0
    '27 192': '1',  # SBB EAX,EAX => 1
    '25 216': '0',  # SBB EAX,EBX => 0
    '27 195': '1',  # SBB EAX,EBX => 1
    '25 200': '0',  # SBB EAX,ECX => 0
    '27 193': '1',  # SBB EAX,ECX => 1
    '25 208': '0',  # SBB EAX,EDX => 0
    '27 194': '1',  # SBB EAX,EDX => 1
    '25 224': '0',  # SBB EAX,ESP => 0
    '27 196': '1',  # SBB EAX,ESP => 1
    '25 232': '0',  # SBB EAX,EBP => 0
    '27 197': '1',  # SBB EAX,EBP => 1
    '25 240': '0',  # SBB EAX,ESI => 0
    '27 198': '1',  # SBB EAX,ESI => 1
    '25 248': '0',  # SBB EAX,EDI => 0
    '27 199': '1',  # SBB EAX,EDI => 1
    '25 195': '0',  # SBB EBX,EAX => 0
    '27 216': '1',  # SBB EBX,EAX => 1
    '25 219': '0',  # SBB EBX,EBX => 0
    '27 219': '1',  # SBB EBX,EBX => 1
    '25 203': '0',  # SBB EBX,ECX => 0
    '27 217': '1',  # SBB EBX,ECX => 1
    '25 211': '0',  # SBB EBX,EDX => 0
    '27 218': '1',  # SBB EBX,EDX => 1
    '25 227': '0',  # SBB EBX,ESP => 0
    '27 220': '1',  # SBB EBX,ESP => 1
    '25 235': '0',  # SBB EBX,EBP => 0
    '27 221': '1',  # SBB EBX,EBP => 1
    '25 243': '0',  # SBB EBX,ESI => 0
    '27 222': '1',  # SBB EBX,ESI => 1
    '25 251': '0',  # SBB EBX,EDI => 0
    '27 223': '1',  # SBB EBX,EDI => 1
    '25 193': '0',  # SBB ECX,EAX => 0
    '27 200': '1',  # SBB ECX,EAX => 1
    '25 217': '0',  # SBB ECX,EBX => 0
    '27 203': '1',  # SBB ECX,EBX => 1
    '25 201': '0',  # SBB ECX,ECX => 0
    '27 201': '1',  # SBB ECX,ECX => 1
    '25 209': '0',  # SBB ECX,EDX => 0
    '27 202': '1',  # SBB ECX,EDX => 1
    '25 225': '0',  # SBB ECX,ESP => 0
    '27 204': '1',  # SBB ECX,ESP => 1
    '25 233': '0',  # SBB ECX,EBP => 0
    '27 205': '1',  # SBB ECX,EBP => 1
    '25 241': '0',  # SBB ECX,ESI => 0
    '27 206': '1',  # SBB ECX,ESI => 1
    '25 249': '0',  # SBB ECX,EDI => 0
    '27 207': '1',  # SBB ECX,EDI => 1
    '25 194': '0',  # SBB EDX,EAX => 0
    '27 208': '1',  # SBB EDX,EAX => 1
    '25 218': '0',  # SBB EDX,EBX => 0
    '27 211': '1',  # SBB EDX,EBX => 1
    '25 202': '0',  # SBB EDX,ECX => 0
    '27 209': '1',  # SBB EDX,ECX => 1
    '25 210': '0',  # SBB EDX,EDX => 0
    '27 210': '1',  # SBB EDX,EDX => 1
    '25 226': '0',  # SBB EDX,ESP => 0
    '27 212': '1',  # SBB EDX,ESP => 1
    '25 234': '0',  # SBB EDX,EBP => 0
    '27 213': '1',  # SBB EDX,EBP => 1
    '25 242': '0',  # SBB EDX,ESI => 0
    '27 214': '1',  # SBB EDX,ESI => 1
    '25 250': '0',  # SBB EDX,EDI => 0
    '27 215': '1',  # SBB EDX,EDI => 1
    '25 196': '0',  # SBB ESP,EAX => 0
    '27 224': '1',  # SBB ESP,EAX => 1
    '25 220': '0',  # SBB ESP,EBX => 0
    '27 227': '1',  # SBB ESP,EBX => 1
    '25 204': '0',  # SBB ESP,ECX => 0
    '27 225': '1',  # SBB ESP,ECX => 1
    '25 212': '0',  # SBB ESP,EDX => 0
    '27 226': '1',  # SBB ESP,EDX => 1
    '25 228': '0',  # SBB ESP,ESP => 0
    '27 228': '1',  # SBB ESP,ESP => 1
    '25 236': '0',  # SBB ESP,EBP => 0
    '27 229': '1',  # SBB ESP,EBP => 1
    '25 244': '0',  # SBB ESP,ESI => 0
    '27 230': '1',  # SBB ESP,ESI => 1
    '25 252': '0',  # SBB ESP,EDI => 0
    '27 231': '1',  # SBB ESP,EDI => 1
    '25 197': '0',  # SBB EBP,EAX => 0
    '27 232': '1',  # SBB EBP,EAX => 1
    '25 221': '0',  # SBB EBP,EBX => 0
    '27 235': '1',  # SBB EBP,EBX => 1
    '25 205': '0',  # SBB EBP,ECX => 0
    '27 233': '1',  # SBB EBP,ECX => 1
    '25 213': '0',  # SBB EBP,EDX => 0
    '27 234': '1',  # SBB EBP,EDX => 1
    '25 229': '0',  # SBB EBP,ESP => 0
    '27 236': '1',  # SBB EBP,ESP => 1
    '25 237': '0',  # SBB EBP,EBP => 0
    '27 237': '1',  # SBB EBP,EBP => 1
    '25 245': '0',  # SBB EBP,ESI => 0
    '27 238': '1',  # SBB EBP,ESI => 1
    '25 253': '0',  # SBB EBP,EDI => 0
    '27 239': '1',  # SBB EBP,EDI => 1
    '25 198': '0',  # SBB ESI,EAX => 0
    '27 240': '1',  # SBB ESI,EAX => 1
    '25 222': '0',  # SBB ESI,EBX => 0
    '27 243': '1',  # SBB ESI,EBX => 1
    '25 206': '0',  # SBB ESI,ECX => 0
    '27 241': '1',  # SBB ESI,ECX => 1
    '25 214': '0',  # SBB ESI,EDX => 0
    '27 242': '1',  # SBB ESI,EDX => 1
    '25 230': '0',  # SBB ESI,ESP => 0
    '27 244': '1',  # SBB ESI,ESP => 1
    '25 238': '0',  # SBB ESI,EBP => 0
    '27 245': '1',  # SBB ESI,EBP => 1
    '25 246': '0',  # SBB ESI,ESI => 0
    '27 246': '1',  # SBB ESI,ESI => 1
    '25 254': '0',  # SBB ESI,EDI => 0
    '27 247': '1',  # SBB ESI,EDI => 1
    '25 199': '0',  # SBB EDI,EAX => 0
    '27 248': '1',  # SBB EDI,EAX => 1
    '25 223': '0',  # SBB EDI,EBX => 0
    '27 251': '1',  # SBB EDI,EBX => 1
    '25 207': '0',  # SBB EDI,ECX => 0
    '27 249': '1',  # SBB EDI,ECX => 1
    '25 215': '0',  # SBB EDI,EDX => 0
    '27 250': '1',  # SBB EDI,EDX => 1
    '25 231': '0',  # SBB EDI,ESP => 0
    '27 252': '1',  # SBB EDI,ESP => 1
    '25 239': '0',  # SBB EDI,EBP => 0
    '27 253': '1',  # SBB EDI,EBP => 1
    '25 247': '0',  # SBB EDI,ESI => 0
    '27 254': '1',  # SBB EDI,ESI => 1
    '25 255': '0',  # SBB EDI,EDI => 0
    '27 255': '1',  # SBB EDI,EDI => 1
    '24 228': '0',  # SBB AH,AH => 0
    '26 228': '1',  # SBB AH,AH => 1
    '24 252': '0',  # SBB AH,BH => 0
    '26 231': '1',  # SBB AH,BH => 1
    '24 236': '0',  # SBB AH,CH => 0
    '26 229': '1',  # SBB AH,CH => 1
    '24 244': '0',  # SBB AH,DH => 0
    '26 230': '1',  # SBB AH,DH => 1
    '24 231': '0',  # SBB BH,AH => 0
    '26 252': '1',  # SBB BH,AH => 1
    '24 255': '0',  # SBB BH,BH => 0
    '26 255': '1',  # SBB BH,BH => 1
    '24 239': '0',  # SBB BH,CH => 0
    '26 253': '1',  # SBB BH,CH => 1
    '24 247': '0',  # SBB BH,DH => 0
    '26 254': '1',  # SBB BH,DH => 1
    '24 229': '0',  # SBB CH,AH => 0
    '26 236': '1',  # SBB CH,AH => 1
    '24 253': '0',  # SBB CH,BH => 0
    '26 239': '1',  # SBB CH,BH => 1
    '24 237': '0',  # SBB CH,CH => 0
    '26 237': '1',  # SBB CH,CH => 1
    '24 245': '0',  # SBB CH,DH => 0
    '26 238': '1',  # SBB CH,DH => 1
    '24 230': '0',  # SBB DH,AH => 0
    '26 244': '1',  # SBB DH,AH => 1
    '24 254': '0',  # SBB DH,BH => 0
    '26 247': '1',  # SBB DH,BH => 1
    '24 238': '0',  # SBB DH,CH => 0
    '26 245': '1',  # SBB DH,CH => 1
    '24 246': '0',  # SBB DH,DH => 0
    '26 246': '1',  # SBB DH,DH => 1
    '24 192': '0',  # SBB AL,AL => 0
    '26 192': '1',  # SBB AL,AL => 1
    '24 216': '0',  # SBB AL,BL => 0
    '26 195': '1',  # SBB AL,BL => 1
    '24 200': '0',  # SBB AL,CL => 0
    '26 193': '1',  # SBB AL,CL => 1
    '24 208': '0',  # SBB AL,DL => 0
    '26 194': '1',  # SBB AL,DL => 1
    '24 195': '0',  # SBB BL,AL => 0
    '26 216': '1',  # SBB BL,AL => 1
    '24 219': '0',  # SBB BL,BL => 0
    '26 219': '1',  # SBB BL,BL => 1
    '24 203': '0',  # SBB BL,CL => 0
    '26 217': '1',  # SBB BL,CL => 1
    '24 211': '0',  # SBB BL,DL => 0
    '26 218': '1',  # SBB BL,DL => 1
    '24 193': '0',  # SBB CL,AL => 0
    '26 200': '1',  # SBB CL,AL => 1
    '24 217': '0',  # SBB CL,BL => 0
    '26 203': '1',  # SBB CL,BL => 1
    '24 201': '0',  # SBB CL,CL => 0
    '26 201': '1',  # SBB CL,CL => 1
    '24 209': '0',  # SBB CL,DL => 0
    '26 202': '1',  # SBB CL,DL => 1
    '24 194': '0',  # SBB DL,AL => 0
    '26 208': '1',  # SBB DL,AL => 1
    '24 218': '0',  # SBB DL,BL => 0
    '26 211': '1',  # SBB DL,BL => 1
    '24 202': '0',  # SBB DL,CL => 0
    '26 209': '1',  # SBB DL,CL => 1
    '24 210': '0',  # SBB DL,DL => 0
    '26 210': '1',  # SBB DL,DL => 1
    '41 192': '0',  # SUB EAX,EAX => 0
    '43 192': '1',  # SUB EAX,EAX => 1
    '41 216': '0',  # SUB EAX,EBX => 0
    '43 195': '1',  # SUB EAX,EBX => 1
    '41 200': '0',  # SUB EAX,ECX => 0
    '43 193': '1',  # SUB EAX,ECX => 1
    '41 208': '0',  # SUB EAX,EDX => 0
    '43 194': '1',  # SUB EAX,EDX => 1
    '41 224': '0',  # SUB EAX,ESP => 0
    '43 196': '1',  # SUB EAX,ESP => 1
    '41 232': '0',  # SUB EAX,EBP => 0
    '43 197': '1',  # SUB EAX,EBP => 1
    '41 240': '0',  # SUB EAX,ESI => 0
    '43 198': '1',  # SUB EAX,ESI => 1
    '41 248': '0',  # SUB EAX,EDI => 0
    '43 199': '1',  # SUB EAX,EDI => 1
    '41 195': '0',  # SUB EBX,EAX => 0
    '43 216': '1',  # SUB EBX,EAX => 1
    '41 219': '0',  # SUB EBX,EBX => 0
    '43 219': '1',  # SUB EBX,EBX => 1
    '41 203': '0',  # SUB EBX,ECX => 0
    '43 217': '1',  # SUB EBX,ECX => 1
    '41 211': '0',  # SUB EBX,EDX => 0
    '43 218': '1',  # SUB EBX,EDX => 1
    '41 227': '0',  # SUB EBX,ESP => 0
    '43 220': '1',  # SUB EBX,ESP => 1
    '41 235': '0',  # SUB EBX,EBP => 0
    '43 221': '1',  # SUB EBX,EBP => 1
    '41 243': '0',  # SUB EBX,ESI => 0
    '43 222': '1',  # SUB EBX,ESI => 1
    '41 251': '0',  # SUB EBX,EDI => 0
    '43 223': '1',  # SUB EBX,EDI => 1
    '41 193': '0',  # SUB ECX,EAX => 0
    '43 200': '1',  # SUB ECX,EAX => 1
    '41 217': '0',  # SUB ECX,EBX => 0
    '43 203': '1',  # SUB ECX,EBX => 1
    '41 201': '0',  # SUB ECX,ECX => 0
    '43 201': '1',  # SUB ECX,ECX => 1
    '41 209': '0',  # SUB ECX,EDX => 0
    '43 202': '1',  # SUB ECX,EDX => 1
    '41 225': '0',  # SUB ECX,ESP => 0
    '43 204': '1',  # SUB ECX,ESP => 1
    '41 233': '0',  # SUB ECX,EBP => 0
    '43 205': '1',  # SUB ECX,EBP => 1
    '41 241': '0',  # SUB ECX,ESI => 0
    '43 206': '1',  # SUB ECX,ESI => 1
    '41 249': '0',  # SUB ECX,EDI => 0
    '43 207': '1',  # SUB ECX,EDI => 1
    '41 194': '0',  # SUB EDX,EAX => 0
    '43 208': '1',  # SUB EDX,EAX => 1
    '41 218': '0',  # SUB EDX,EBX => 0
    '43 211': '1',  # SUB EDX,EBX => 1
    '41 202': '0',  # SUB EDX,ECX => 0
    '43 209': '1',  # SUB EDX,ECX => 1
    '41 210': '0',  # SUB EDX,EDX => 0
    '43 210': '1',  # SUB EDX,EDX => 1
    '41 226': '0',  # SUB EDX,ESP => 0
    '43 212': '1',  # SUB EDX,ESP => 1
    '41 234': '0',  # SUB EDX,EBP => 0
    '43 213': '1',  # SUB EDX,EBP => 1
    '41 242': '0',  # SUB EDX,ESI => 0
    '43 214': '1',  # SUB EDX,ESI => 1
    '41 250': '0',  # SUB EDX,EDI => 0
    '43 215': '1',  # SUB EDX,EDI => 1
    '41 196': '0',  # SUB ESP,EAX => 0
    '43 224': '1',  # SUB ESP,EAX => 1
    '41 220': '0',  # SUB ESP,EBX => 0
    '43 227': '1',  # SUB ESP,EBX => 1
    '41 204': '0',  # SUB ESP,ECX => 0
    '43 225': '1',  # SUB ESP,ECX => 1
    '41 212': '0',  # SUB ESP,EDX => 0
    '43 226': '1',  # SUB ESP,EDX => 1
    '41 228': '0',  # SUB ESP,ESP => 0
    '43 228': '1',  # SUB ESP,ESP => 1
    '41 236': '0',  # SUB ESP,EBP => 0
    '43 229': '1',  # SUB ESP,EBP => 1
    '41 244': '0',  # SUB ESP,ESI => 0
    '43 230': '1',  # SUB ESP,ESI => 1
    '41 252': '0',  # SUB ESP,EDI => 0
    '43 231': '1',  # SUB ESP,EDI => 1
    '41 197': '0',  # SUB EBP,EAX => 0
    '43 232': '1',  # SUB EBP,EAX => 1
    '41 221': '0',  # SUB EBP,EBX => 0
    '43 235': '1',  # SUB EBP,EBX => 1
    '41 205': '0',  # SUB EBP,ECX => 0
    '43 233': '1',  # SUB EBP,ECX => 1
    '41 213': '0',  # SUB EBP,EDX => 0
    '43 234': '1',  # SUB EBP,EDX => 1
    '41 229': '0',  # SUB EBP,ESP => 0
    '43 236': '1',  # SUB EBP,ESP => 1
    '41 237': '0',  # SUB EBP,EBP => 0
    '43 237': '1',  # SUB EBP,EBP => 1
    '41 245': '0',  # SUB EBP,ESI => 0
    '43 238': '1',  # SUB EBP,ESI => 1
    '41 253': '0',  # SUB EBP,EDI => 0
    '43 239': '1',  # SUB EBP,EDI => 1
    '41 198': '0',  # SUB ESI,EAX => 0
    '43 240': '1',  # SUB ESI,EAX => 1
    '41 222': '0',  # SUB ESI,EBX => 0
    '43 243': '1',  # SUB ESI,EBX => 1
    '41 206': '0',  # SUB ESI,ECX => 0
    '43 241': '1',  # SUB ESI,ECX => 1
    '41 214': '0',  # SUB ESI,EDX => 0
    '43 242': '1',  # SUB ESI,EDX => 1
    '41 230': '0',  # SUB ESI,ESP => 0
    '43 244': '1',  # SUB ESI,ESP => 1
    '41 238': '0',  # SUB ESI,EBP => 0
    '43 245': '1',  # SUB ESI,EBP => 1
    '41 246': '0',  # SUB ESI,ESI => 0
    '43 246': '1',  # SUB ESI,ESI => 1
    '41 254': '0',  # SUB ESI,EDI => 0
    '43 247': '1',  # SUB ESI,EDI => 1
    '41 199': '0',  # SUB EDI,EAX => 0
    '43 248': '1',  # SUB EDI,EAX => 1
    '41 223': '0',  # SUB EDI,EBX => 0
    '43 251': '1',  # SUB EDI,EBX => 1
    '41 207': '0',  # SUB EDI,ECX => 0
    '43 249': '1',  # SUB EDI,ECX => 1
    '41 215': '0',  # SUB EDI,EDX => 0
    '43 250': '1',  # SUB EDI,EDX => 1
    '41 231': '0',  # SUB EDI,ESP => 0
    '43 252': '1',  # SUB EDI,ESP => 1
    '41 239': '0',  # SUB EDI,EBP => 0
    '43 253': '1',  # SUB EDI,EBP => 1
    '41 247': '0',  # SUB EDI,ESI => 0
    '43 254': '1',  # SUB EDI,ESI => 1
    '41 255': '0',  # SUB EDI,EDI => 0
    '43 255': '1',  # SUB EDI,EDI => 1
    '40 228': '0',  # SUB AH,AH => 0
    '42 228': '1',  # SUB AH,AH => 1
    '40 252': '0',  # SUB AH,BH => 0
    '42 231': '1',  # SUB AH,BH => 1
    '40 236': '0',  # SUB AH,CH => 0
    '42 229': '1',  # SUB AH,CH => 1
    '40 244': '0',  # SUB AH,DH => 0
    '42 230': '1',  # SUB AH,DH => 1
    '40 231': '0',  # SUB BH,AH => 0
    '42 252': '1',  # SUB BH,AH => 1
    '40 255': '0',  # SUB BH,BH => 0
    '42 255': '1',  # SUB BH,BH => 1
    '40 239': '0',  # SUB BH,CH => 0
    '42 253': '1',  # SUB BH,CH => 1
    '40 247': '0',  # SUB BH,DH => 0
    '42 254': '1',  # SUB BH,DH => 1
    '40 229': '0',  # SUB CH,AH => 0
    '42 236': '1',  # SUB CH,AH => 1
    '40 253': '0',  # SUB CH,BH => 0
    '42 239': '1',  # SUB CH,BH => 1
    '40 237': '0',  # SUB CH,CH => 0
    '42 237': '1',  # SUB CH,CH => 1
    '40 245': '0',  # SUB CH,DH => 0
    '42 238': '1',  # SUB CH,DH => 1
    '40 230': '0',  # SUB DH,AH => 0
    '42 244': '1',  # SUB DH,AH => 1
    '40 254': '0',  # SUB DH,BH => 0
    '42 247': '1',  # SUB DH,BH => 1
    '40 238': '0',  # SUB DH,CH => 0
    '42 245': '1',  # SUB DH,CH => 1
    '40 246': '0',  # SUB DH,DH => 0
    '42 246': '1',  # SUB DH,DH => 1
    '40 192': '0',  # SUB AL,AL => 0
    '42 192': '1',  # SUB AL,AL => 1
    '40 216': '0',  # SUB AL,BL => 0
    '42 195': '1',  # SUB AL,BL => 1
    '40 200': '0',  # SUB AL,CL => 0
    '42 193': '1',  # SUB AL,CL => 1
    '40 208': '0',  # SUB AL,DL => 0
    '42 194': '1',  # SUB AL,DL => 1
    '40 195': '0',  # SUB BL,AL => 0
    '42 216': '1',  # SUB BL,AL => 1
    '40 219': '0',  # SUB BL,BL => 0
    '42 219': '1',  # SUB BL,BL => 1
    '40 203': '0',  # SUB BL,CL => 0
    '42 217': '1',  # SUB BL,CL => 1
    '40 211': '0',  # SUB BL,DL => 0
    '42 218': '1',  # SUB BL,DL => 1
    '40 193': '0',  # SUB CL,AL => 0
    '42 200': '1',  # SUB CL,AL => 1
    '40 217': '0',  # SUB CL,BL => 0
    '42 203': '1',  # SUB CL,BL => 1
    '40 201': '0',  # SUB CL,CL => 0
    '42 201': '1',  # SUB CL,CL => 1
    '40 209': '0',  # SUB CL,DL => 0
    '42 202': '1',  # SUB CL,DL => 1
    '40 194': '0',  # SUB DL,AL => 0
    '42 208': '1',  # SUB DL,AL => 1
    '40 218': '0',  # SUB DL,BL => 0
    '42 211': '1',  # SUB DL,BL => 1
    '40 202': '0',  # SUB DL,CL => 0
    '42 209': '1',  # SUB DL,CL => 1
    '40 210': '0',  # SUB DL,DL => 0
    '42 210': '1',  # SUB DL,DL => 1
    '57 192': '0',  # CMP EAX,EAX => 0
    '59 192': '1',  # CMP EAX,EAX => 1
    '57 216': '0',  # CMP EAX,EBX => 0
    '59 195': '1',  # CMP EAX,EBX => 1
    '57 200': '0',  # CMP EAX,ECX => 0
    '59 193': '1',  # CMP EAX,ECX => 1
    '57 208': '0',  # CMP EAX,EDX => 0
    '59 194': '1',  # CMP EAX,EDX => 1
    '57 224': '0',  # CMP EAX,ESP => 0
    '59 196': '1',  # CMP EAX,ESP => 1
    '57 232': '0',  # CMP EAX,EBP => 0
    '59 197': '1',  # CMP EAX,EBP => 1
    '57 240': '0',  # CMP EAX,ESI => 0
    '59 198': '1',  # CMP EAX,ESI => 1
    '57 248': '0',  # CMP EAX,EDI => 0
    '59 199': '1',  # CMP EAX,EDI => 1
    '57 195': '0',  # CMP EBX,EAX => 0
    '59 216': '1',  # CMP EBX,EAX => 1
    '57 219': '0',  # CMP EBX,EBX => 0
    '59 219': '1',  # CMP EBX,EBX => 1
    '57 203': '0',  # CMP EBX,ECX => 0
    '59 217': '1',  # CMP EBX,ECX => 1
    '57 211': '0',  # CMP EBX,EDX => 0
    '59 218': '1',  # CMP EBX,EDX => 1
    '57 227': '0',  # CMP EBX,ESP => 0
    '59 220': '1',  # CMP EBX,ESP => 1
    '57 235': '0',  # CMP EBX,EBP => 0
    '59 221': '1',  # CMP EBX,EBP => 1
    '57 243': '0',  # CMP EBX,ESI => 0
    '59 222': '1',  # CMP EBX,ESI => 1
    '57 251': '0',  # CMP EBX,EDI => 0
    '59 223': '1',  # CMP EBX,EDI => 1
    '57 193': '0',  # CMP ECX,EAX => 0
    '59 200': '1',  # CMP ECX,EAX => 1
    '57 217': '0',  # CMP ECX,EBX => 0
    '59 203': '1',  # CMP ECX,EBX => 1
    '57 201': '0',  # CMP ECX,ECX => 0
    '59 201': '1',  # CMP ECX,ECX => 1
    '57 209': '0',  # CMP ECX,EDX => 0
    '59 202': '1',  # CMP ECX,EDX => 1
    '57 225': '0',  # CMP ECX,ESP => 0
    '59 204': '1',  # CMP ECX,ESP => 1
    '57 233': '0',  # CMP ECX,EBP => 0
    '59 205': '1',  # CMP ECX,EBP => 1
    '57 241': '0',  # CMP ECX,ESI => 0
    '59 206': '1',  # CMP ECX,ESI => 1
    '57 249': '0',  # CMP ECX,EDI => 0
    '59 207': '1',  # CMP ECX,EDI => 1
    '57 194': '0',  # CMP EDX,EAX => 0
    '59 208': '1',  # CMP EDX,EAX => 1
    '57 218': '0',  # CMP EDX,EBX => 0
    '59 211': '1',  # CMP EDX,EBX => 1
    '57 202': '0',  # CMP EDX,ECX => 0
    '59 209': '1',  # CMP EDX,ECX => 1
    '57 210': '0',  # CMP EDX,EDX => 0
    '59 210': '1',  # CMP EDX,EDX => 1
    '57 226': '0',  # CMP EDX,ESP => 0
    '59 212': '1',  # CMP EDX,ESP => 1
    '57 234': '0',  # CMP EDX,EBP => 0
    '59 213': '1',  # CMP EDX,EBP => 1
    '57 242': '0',  # CMP EDX,ESI => 0
    '59 214': '1',  # CMP EDX,ESI => 1
    '57 250': '0',  # CMP EDX,EDI => 0
    '59 215': '1',  # CMP EDX,EDI => 1
    '57 196': '0',  # CMP ESP,EAX => 0
    '59 224': '1',  # CMP ESP,EAX => 1
    '57 220': '0',  # CMP ESP,EBX => 0
    '59 227': '1',  # CMP ESP,EBX => 1
    '57 204': '0',  # CMP ESP,ECX => 0
    '59 225': '1',  # CMP ESP,ECX => 1
    '57 212': '0',  # CMP ESP,EDX => 0
    '59 226': '1',  # CMP ESP,EDX => 1
    '57 228': '0',  # CMP ESP,ESP => 0
    '59 228': '1',  # CMP ESP,ESP => 1
    '57 236': '0',  # CMP ESP,EBP => 0
    '59 229': '1',  # CMP ESP,EBP => 1
    '57 244': '0',  # CMP ESP,ESI => 0
    '59 230': '1',  # CMP ESP,ESI => 1
    '57 252': '0',  # CMP ESP,EDI => 0
    '59 231': '1',  # CMP ESP,EDI => 1
    '57 197': '0',  # CMP EBP,EAX => 0
    '59 232': '1',  # CMP EBP,EAX => 1
    '57 221': '0',  # CMP EBP,EBX => 0
    '59 235': '1',  # CMP EBP,EBX => 1
    '57 205': '0',  # CMP EBP,ECX => 0
    '59 233': '1',  # CMP EBP,ECX => 1
    '57 213': '0',  # CMP EBP,EDX => 0
    '59 234': '1',  # CMP EBP,EDX => 1
    '57 229': '0',  # CMP EBP,ESP => 0
    '59 236': '1',  # CMP EBP,ESP => 1
    '57 237': '0',  # CMP EBP,EBP => 0
    '59 237': '1',  # CMP EBP,EBP => 1
    '57 245': '0',  # CMP EBP,ESI => 0
    '59 238': '1',  # CMP EBP,ESI => 1
    '57 253': '0',  # CMP EBP,EDI => 0
    '59 239': '1',  # CMP EBP,EDI => 1
    '57 198': '0',  # CMP ESI,EAX => 0
    '59 240': '1',  # CMP ESI,EAX => 1
    '57 222': '0',  # CMP ESI,EBX => 0
    '59 243': '1',  # CMP ESI,EBX => 1
    '57 206': '0',  # CMP ESI,ECX => 0
    '59 241': '1',  # CMP ESI,ECX => 1
    '57 214': '0',  # CMP ESI,EDX => 0
    '59 242': '1',  # CMP ESI,EDX => 1
    '57 230': '0',  # CMP ESI,ESP => 0
    '59 244': '1',  # CMP ESI,ESP => 1
    '57 238': '0',  # CMP ESI,EBP => 0
    '59 245': '1',  # CMP ESI,EBP => 1
    '57 246': '0',  # CMP ESI,ESI => 0
    '59 246': '1',  # CMP ESI,ESI => 1
    '57 254': '0',  # CMP ESI,EDI => 0
    '59 247': '1',  # CMP ESI,EDI => 1
    '57 199': '0',  # CMP EDI,EAX => 0
    '59 248': '1',  # CMP EDI,EAX => 1
    '57 223': '0',  # CMP EDI,EBX => 0
    '59 251': '1',  # CMP EDI,EBX => 1
    '57 207': '0',  # CMP EDI,ECX => 0
    '59 249': '1',  # CMP EDI,ECX => 1
    '57 215': '0',  # CMP EDI,EDX => 0
    '59 250': '1',  # CMP EDI,EDX => 1
    '57 231': '0',  # CMP EDI,ESP => 0
    '59 252': '1',  # CMP EDI,ESP => 1
    '57 239': '0',  # CMP EDI,EBP => 0
    '59 253': '1',  # CMP EDI,EBP => 1
    '57 247': '0',  # CMP EDI,ESI => 0
    '59 254': '1',  # CMP EDI,ESI => 1
    '57 255': '0',  # CMP EDI,EDI => 0
    '59 255': '1',  # CMP EDI,EDI => 1
    '56 228': '0',  # CMP AH,AH => 0
    '58 228': '1',  # CMP AH,AH => 1
    '56 252': '0',  # CMP AH,BH => 0
    '58 231': '1',  # CMP AH,BH => 1
    '56 236': '0',  # CMP AH,CH => 0
    '58 229': '1',  # CMP AH,CH => 1
    '56 244': '0',  # CMP AH,DH => 0
    '58 230': '1',  # CMP AH,DH => 1
    '56 231': '0',  # CMP BH,AH => 0
    '58 252': '1',  # CMP BH,AH => 1
    '56 255': '0',  # CMP BH,BH => 0
    '58 255': '1',  # CMP BH,BH => 1
    '56 239': '0',  # CMP BH,CH => 0
    '58 253': '1',  # CMP BH,CH => 1
    '56 247': '0',  # CMP BH,DH => 0
    '58 254': '1',  # CMP BH,DH => 1
    '56 229': '0',  # CMP CH,AH => 0
    '58 236': '1',  # CMP CH,AH => 1
    '56 253': '0',  # CMP CH,BH => 0
    '58 239': '1',  # CMP CH,BH => 1
    '56 237': '0',  # CMP CH,CH => 0
    '58 237': '1',  # CMP CH,CH => 1
    '56 245': '0',  # CMP CH,DH => 0
    '58 238': '1',  # CMP CH,DH => 1
    '56 230': '0',  # CMP DH,AH => 0
    '58 244': '1',  # CMP DH,AH => 1
    '56 254': '0',  # CMP DH,BH => 0
    '58 247': '1',  # CMP DH,BH => 1
    '56 238': '0',  # CMP DH,CH => 0
    '58 245': '1',  # CMP DH,CH => 1
    '56 246': '0',  # CMP DH,DH => 0
    '58 246': '1',  # CMP DH,DH => 1
    '56 192': '0',  # CMP AL,AL => 0
    '58 192': '1',  # CMP AL,AL => 1
    '56 216': '0',  # CMP AL,BL => 0
    '58 195': '1',  # CMP AL,BL => 1
    '56 200': '0',  # CMP AL,CL => 0
    '58 193': '1',  # CMP AL,CL => 1
    '56 208': '0',  # CMP AL,DL => 0
    '58 194': '1',  # CMP AL,DL => 1
    '56 195': '0',  # CMP BL,AL => 0
    '58 216': '1',  # CMP BL,AL => 1
    '56 219': '0',  # CMP BL,BL => 0
    '58 219': '1',  # CMP BL,BL => 1
    '56 203': '0',  # CMP BL,CL => 0
    '58 217': '1',  # CMP BL,CL => 1
    '56 211': '0',  # CMP BL,DL => 0
    '58 218': '1',  # CMP BL,DL => 1
    '56 193': '0',  # CMP CL,AL => 0
    '58 200': '1',  # CMP CL,AL => 1
    '56 217': '0',  # CMP CL,BL => 0
    '58 203': '1',  # CMP CL,BL => 1
    '56 201': '0',  # CMP CL,CL => 0
    '58 201': '1',  # CMP CL,CL => 1
    '56 209': '0',  # CMP CL,DL => 0
    '58 202': '1',  # CMP CL,DL => 1
    '56 194': '0',  # CMP DL,AL => 0
    '58 208': '1',  # CMP DL,AL => 1
    '56 218': '0',  # CMP DL,BL => 0
    '58 211': '1',  # CMP DL,BL => 1
    '56 202': '0',  # CMP DL,CL => 0
    '58 209': '1',  # CMP DL,CL => 1
    '56 210': '0',  # CMP DL,DL => 0
    '58 210': '1',  # CMP DL,DL => 1
    '133 216': '0',   # TEST EAX,EBX => 0
    '133 195': '1',   # TEST EAX,EBX => 1
    '133 200': '0',   # TEST EAX,ECX => 0
    '133 193': '1',   # TEST EAX,ECX => 1
    '133 208': '0',   # TEST EAX,EDX => 0
    '133 194': '1',   # TEST EAX,EDX => 1
    '133 224': '0',   # TEST EAX,ESP => 0
    '133 196': '1',   # TEST EAX,ESP => 1
    '133 232': '0',   # TEST EAX,EBP => 0
    '133 197': '1',   # TEST EAX,EBP => 1
    '133 240': '0',   # TEST EAX,ESI => 0
    '133 198': '1',   # TEST EAX,ESI => 1
    '133 248': '0',   # TEST EAX,EDI => 0
    '133 199': '1',   # TEST EAX,EDI => 1
    '133 203': '0',   # TEST EBX,ECX => 0
    '133 217': '1',   # TEST EBX,ECX => 1
    '133 211': '0',   # TEST EBX,EDX => 0
    '133 218': '1',   # TEST EBX,EDX => 1
    '133 227': '0',   # TEST EBX,ESP => 0
    '133 220': '1',   # TEST EBX,ESP => 1
    '133 235': '0',   # TEST EBX,EBP => 0
    '133 221': '1',   # TEST EBX,EBP => 1
    '133 243': '0',   # TEST EBX,ESI => 0
    '133 222': '1',   # TEST EBX,ESI => 1
    '133 251': '0',   # TEST EBX,EDI => 0
    '133 223': '1',   # TEST EBX,EDI => 1
    '133 209': '0',   # TEST ECX,EDX => 0
    '133 202': '1',   # TEST ECX,EDX => 1
    '133 225': '0',   # TEST ECX,ESP => 0
    '133 204': '1',   # TEST ECX,ESP => 1
    '133 233': '0',   # TEST ECX,EBP => 0
    '133 205': '1',   # TEST ECX,EBP => 1
    '133 241': '0',   # TEST ECX,ESI => 0
    '133 206': '1',   # TEST ECX,ESI => 1
    '133 249': '0',   # TEST ECX,EDI => 0
    '133 207': '1',   # TEST ECX,EDI => 1
    '133 226': '0',   # TEST EDX,ESP => 0
    '133 212': '1',   # TEST EDX,ESP => 1
    '133 234': '0',   # TEST EDX,EBP => 0
    '133 213': '1',   # TEST EDX,EBP => 1
    '133 242': '0',   # TEST EDX,ESI => 0
    '133 214': '1',   # TEST EDX,ESI => 1
    '133 250': '0',   # TEST EDX,EDI => 0
    '133 215': '1',   # TEST EDX,EDI => 1
    '133 236': '0',   # TEST ESP,EBP => 0
    '133 229': '1',   # TEST ESP,EBP => 1
    '133 244': '0',   # TEST ESP,ESI => 0
    '133 230': '1',   # TEST ESP,ESI => 1
    '133 252': '0',   # TEST ESP,EDI => 0
    '133 231': '1',   # TEST ESP,EDI => 1
    '133 245': '0',   # TEST EBP,ESI => 0
    '133 238': '1',   # TEST EBP,ESI => 1
    '133 253': '0',   # TEST EBP,EDI => 0
    '133 239': '1',   # TEST EBP,EDI => 1
    '133 254': '0',   # TEST ESI,EDI => 0
    '133 247': '1',   # TEST ESI,EDI => 1

}