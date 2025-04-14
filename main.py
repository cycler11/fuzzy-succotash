
#opcodes -- https://www.keil.com/support/man/docs/is51/is51_opcodes.asp?bhcp=1

opcode_dict = {
    'NOP': '00', 'AJMP': '01', 'LJMP': '02', 'RR A': '03', 'INC A': '04',
    'DEC A': '14', 'ADD A,R0': '28', 'ADD A,R1': '29',
    'JC': '40', 'JZ': '60', 'JNZ': '70', 'SJMP': '80',
    'MUL AB': 'A4', 'DIV AB': '84', 'SUBB A,#data': '94',
    'MOV A,#data': '74', 'MOV A,R0': 'E8', 'MOV A,R1': 'E9',
    'MOV A,R2': 'EA', 'MOV A,R3': 'EB', 'MOV A,R4': 'EC',
    'MOV A,R5': 'ED', 'MOV A,R6': 'EE', 'MOV A,R7': 'EF',
    'MOV @R0,#data': '76', 'MOV @R1,#data': '77',
    'MOV R0,#data': '78', 'MOV R1,#data': '79',
    'MOV DPTR,#data': '90', 'MOVC A,@A+DPTR': '93',
    'CLR A': 'E4', 'SWAP A': 'C4', 'INC DPTR': 'A3'
}

#BIN -> ASM
inverse_dict = {v: k for k, v in opcode_dict.items()}


def assembler_to_binary(asm_code):
    result = ''
    lines = asm_code.strip().split('\n')
    for line in lines:
        cmd = line.strip()
        hexcode = opcode_dict.get(cmd)
        if hexcode:
            result += hexcode
        else:
            print(f'Неизвестная команда: {cmd}')
    return result


def binary_to_assembler(binary_code):
    result = ''
    for i in range(0, len(binary_code), 2):
        byte = binary_code[i:i + 2].upper()
        asm = inverse_dict.get(byte, 'Неизвестная команда')
        result += f'0x{byte} --> {asm}\n'
    return result


asm_code = """\
CLR A
ADD A,R0
MOV A,R1
MOV @R0,#data
"""

binary_output = assembler_to_binary(asm_code)
print('ASM → BIN:')
print(binary_output)

print('\nBIN → ASM:')
print(binary_to_assembler(binary_output))
