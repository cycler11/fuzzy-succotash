# ASM -> BIN

def assembler_to_binary(asm_code):
    opcode_dict = {
        # Простые команды
        'NOP': '00', 'AJMP': '01', 'LJMP': '02', 'RR A': '03', 'INC A': '04',
        'DEC A': '14', 'ADD A,R0': '28', 'ADD A,R1': '29', 'JC': '40', 'MOV A,#data': '74',

        # Команды с прямыми значениями
        'MOV A,R0': 'E8', 'MOV A,R1': 'E9', 'MOV A,R2': 'EA', 'MOV A,R3': 'EB', 
        'MOV A,R4': 'EC', 'MOV A,R5': 'ED', 'MOV A,R6': 'EE', 'MOV A,R7': 'EF',

        # Работа с памятью
        'MOV @R0,#data': '76', 'MOV @R1,#data': '77', 'MOV R0,#data': '78', 'MOV R1,#data': '79',
        'MOV DPTR,#data': 'A3', 'MOVC A,@A+DPTR': '93', 

        # Условные переходы и флаги
        'JZ': '50', 'JNZ': '51', 'JC': '40', 'SJMP': '80', 'AJMP': '01', 'LJMP': '02',

        # Арифметика
        'MUL AB': 'A4', 'DIV AB': '84', 'SUBB A,#data': '94', 'ADD A,R0': '28',

        # Управляющие команды
        'CLR A': 'E4', 'SWAP A': '12', 'ANL A,B': '32', 'ORL A,B': '44', 'XRL A,B': '64', 
        'INC DPTR': 'A3', 'MOV DPTR,#data': 'A3', 'MOV R0,#data': '78', 
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



# BIN -> ASM

def binary_to_assembler(binary_code):
    opcode_dict = {
        '00': 'NOP', '01': 'AJMP', '02': 'LJMP', '03': 'RR A', '04': 'INC A',
        '14': 'DEC A', '28': 'ADD A,R0', '29': 'ADD A,R1', '40': 'JC', '74': 'MOV A,#data',

        # Команды с регистрами
        'E8': 'MOV A,R0', 'E9': 'MOV A,R1', 'EA': 'MOV A,R2', 'EB': 'MOV A,R3',
        'EC': 'MOV A,R4', 'ED': 'MOV A,R5', 'EE': 'MOV A,R6', 'EF': 'MOV A,R7',

        # Работа с памятью
        '76': 'MOV @R0,#data', '77': 'MOV @R1,#data', '78': 'MOV R0,#data', '79': 'MOV R1,#data',
        'A3': 'MOV DPTR,#data', '93': 'MOVC A,@A+DPTR',

        # Условные переходы и флаги
        '50': 'JZ', '51': 'JNZ', '40': 'JC', '80': 'SJMP', '01': 'AJMP', '02': 'LJMP',

        # Арифметика
        'A4': 'MUL AB', '84': 'DIV AB', '94': 'SUBB A,#data', '28': 'ADD A,R0',

        # Управляющие команды
        'E4': 'CLR A', '12': 'SWAP A', '32': 'ANL A,B', '44': 'ORL A,B', '64': 'XRL A,B',
        'A3': 'INC DPTR', 'A3': 'MOV DPTR,#data', '78': 'MOV R0,#data',
    }

    result = ''
    for i in range(0, len(binary_code), 2):
        byte = binary_code[i:i+2].upper()
        result += f'0x{byte} --> {opcode_dict.get(byte, "Неизвестная команда")}\n'
    return result


asm_code = """\
CLR A
ADD A,R0
MOV A,R1
MOV @R0,#data
JZ
MOVC A,@A+DPTR
DIV AB
"""

binary_output = assembler_to_binary(asm_code)
print('ASM → BIN:')
print(binary_output)

print('\nBIN → ASM:')
print(binary_to_assembler(binary_output))
