#BIN -> ASM 
def assembler_to_binary(asm_code):

    opcode_dict = {
        'CLR A': 'E4',
        'DEC A': '14',
        'DEC R7': '1F',
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





#ASM -> BIN
def binary_to_assembler(binary_code):
    
    opcode_dict = {
        'E4': 'CLR A',
        '14': 'DEC A',
        '1F': 'DEC R7',
        
    }
    
    result = ''

    for i in range(0, len(binary_code), 2):
        byte = binary_code[i:i+2].upper()
        if byte in opcode_dict:
            result += f'0x{byte} --> {opcode_dict[byte]}\n'
        else:
            result += f'0x{byte} --> Неизвестная команда\n'
    
    return result

asm_code = """\
CLR A
DEC A
DEC R7
"""

binary_output = assembler_to_binary(asm_code)
print('ASM -> BIN:')
print(binary_output)  # E4141F

print('\nBIN -> ASM:')
binary_code = "E4141F"
asm_output = binary_to_assembler(binary_code)
print(asm_output)
