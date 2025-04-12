#ASM -> BIM

def assembler_to_binary(asm_code):
    opcode_dict = {
        'NOP': '00',
        'AJMP': '01',
        'LJMP': '02',
        'RR A': '03',
        'INC A': '04',
        'INC @R0': '06',
        'INC @R1': '07',
        'INC R0': '08',
        'INC R1': '09',
        'INC R2': '0A',
        'INC R3': '0B',
        'INC R4': '0C',
        'INC R5': '0D',
        'INC R6': '0E',
        'INC R7': '0F',
        'DEC A': '14',
        'DEC @R0': '16',
        'DEC @R1': '17',
        'DEC R0': '18',
        'DEC R1': '19',
        'DEC R2': '1A',
        'DEC R3': '1B',
        'DEC R4': '1C',
        'DEC R5': '1D',
        'DEC R6': '1E',
        'DEC R7': '1F',
        'ADD A,R0': '28',
        'ADD A,R1': '29',
        'ADD A,R2': '2A',
        'ADD A,R3': '2B',
        'ADD A,R4': '2C',
        'ADD A,R5': '2D',
        'ADD A,R6': '2E',
        'ADD A,R7': '2F',
        'JC': '40',
        'ORL A,#data': '44',
        'ANL A,#data': '54',
        'XRL A,#data': '64',
        'MOV A,#data': '74',
        'MOV @R0,#data': '76',
        'MOV @R1,#data': '77',
        'MOV R0,#data': '78',
        'MOV R1,#data': '79',
        'MOV R2,#data': '7A',
        'MOV R3,#data': '7B',
        'MOV R4,#data': '7C',
        'MOV R5,#data': '7D',
        'MOV R6,#data': '7E',
        'MOV R7,#data': '7F',
        'SJMP': '80',
        'DIV AB': '84',
        'MOVC A,@A+DPTR': '93',
        'SUBB A,#data': '94',
        'INC DPTR': 'A3',
        'MUL AB': 'A4',
        'CLR A': 'E4',
        'MOV A,R0': 'E8',
        'MOV A,R1': 'E9',
        'MOV A,R2': 'EA',
        'MOV A,R3': 'EB',
        'MOV A,R4': 'EC',
        'MOV A,R5': 'ED',
        'MOV A,R6': 'EE',
        'MOV A,R7': 'EF',
    }

    result = ''
    lines = asm_code.strip().split('\n')
    for line in lines:
        cmd = line.strip()
        if cmd in opcode_dict:
            result += opcode_dict[cmd]
        else:
            print(f'Неизвестная команда: {cmd}')
    return result


#BIN -> ASM
def binary_to_assembler(binary_code):
    opcode_dict = {
        '00': 'NOP',
        '01': 'AJMP',
        '02': 'LJMP',
        '03': 'RR A',
        '04': 'INC A',
        '06': 'INC @R0',
        '07': 'INC @R1',
        '08': 'INC R0',
        '09': 'INC R1',
        '0A': 'INC R2',
        '0B': 'INC R3',
        '0C': 'INC R4',
        '0D': 'INC R5',
        '0E': 'INC R6',
        '0F': 'INC R7',
        '14': 'DEC A',
        '16': 'DEC @R0',
        '17': 'DEC @R1',
        '18': 'DEC R0',
        '19': 'DEC R1',
        '1A': 'DEC R2',
        '1B': 'DEC R3',
        '1C': 'DEC R4',
        '1D': 'DEC R5',
        '1E': 'DEC R6',
        '1F': 'DEC R7',
        '28': 'ADD A,R0',
        '29': 'ADD A,R1',
        '2A': 'ADD A,R2',
        '2B': 'ADD A,R3',
        '2C': 'ADD A,R4',
        '2D': 'ADD A,R5',
        '2E': 'ADD A,R6',
        '2F': 'ADD A,R7',
        '40': 'JC',
        '44': 'ORL A,#data',
        '54': 'ANL A,#data',
        '64': 'XRL A,#data',
        '74': 'MOV A,#data',
        '76': 'MOV @R0,#data',
        '77': 'MOV @R1,#data',
        '78': 'MOV R0,#data',
        '79': 'MOV R1,#data',
        '7A': 'MOV R2,#data',
        '7B': 'MOV R3,#data',
        '7C': 'MOV R4,#data',
        '7D': 'MOV R5,#data',
        '7E': 'MOV R6,#data',
        '7F': 'MOV R7,#data',
        '80': 'SJMP',
        '84': 'DIV AB',
        '93': 'MOVC A,@A+DPTR',
        '94': 'SUBB A,#data',
        'A3': 'INC DPTR',
        'A4': 'MUL AB',
        'E4': 'CLR A',
        'E8': 'MOV A,R0',
        'E9': 'MOV A,R1',
        'EA': 'MOV A,R2',
        'EB': 'MOV A,R3',
        'EC': 'MOV A,R4',
        'ED': 'MOV A,R5',
        'EE': 'MOV A,R6',
        'EF': 'MOV A,R7',
    }

    result = ''
    for i in range(0, len(binary_code), 2):
        byte = binary_code[i:i+2].upper()
        result += f'0x{byte} --> {opcode_dict.get(byte, "Неизвестная команда")}\n'
    return result


asm_code = """\
CLR A
DEC A
DEC R7
MOV A,R0
INC R1
"""

binary_output = assembler_to_binary(asm_code)
print('ASM → BIN:')
print(binary_output)

print('\BIN → ASM:')
print(binary_to_assembler(binary_output))
