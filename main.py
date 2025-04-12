def assembler_to_binary(asm_code):
    # slovar
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
            print(f'Неизвестня команда: {cmd}')
    
    return result

asm_code = """\
CLR A
DEC A
DEC R7
"""

binary_output = assembler_to_binary(asm_code)
print(binary_output)  

