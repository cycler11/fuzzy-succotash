opcode_dict = {
    'NOP': '00', 'AJMP 01': '01', 'LJMP': '02', 'RR A': '03', 'INC A': '04', 'INC data addr': '05', 'INC @R0': '06', 'INC @R1': '07',
    'INC R0': '08', 'INC R1': '09', 'INC R2': '0A', 'INC R3': '0B', 'INC R4': '0C', 'INC R5': '0D', 'INC R6': '0E', 'INC R7': '0F',
    'JBC bit, rel': '10', 'ACALL 11': '11', 'LCALL': '12', 'RRC A': '13', 'DEC A': '14', 'DEC data addr': '15', 'DEC @R0': '16', 'DEC @R1': '17',
    'DEC R0': '18', 'DEC R1': '19', 'DEC R2': '1A', 'DEC R3': '1B', 'DEC R4': '1C', 'DEC R5': '1D', 'DEC R6': '1E', 'DEC R7': '1F',
    'JB bit, rel': '20', 'AJMP 21': '21', 'RET': '22', 'RL A': '23', 'ADD A,#data': '24', 'ADD A,data': '25', 'ADD A,@R0': '26', 'ADD A,@R1': '27',
    'ADD A,R0': '28', 'ADD A,R1': '29', 'ADD A,R2': '2A', 'ADD A,R3': '2B', 'ADD A,R4': '2C', 'ADD A,R5': '2D', 'ADD A,R6': '2E', 'ADD A,R7': '2F',
    'JNB bit, rel': '30', 'ACALL 31': '31', 'RETI': '32', 'RLC A': '33', 'ADDC A,#data': '34', 'ADDC A,data': '35', 'ADDC A,@R0': '36', 'ADDC A,@R1': '37',
    'ADDC A,R0': '38', 'ADDC A,R1': '39', 'ADDC A,R2': '3A', 'ADDC A,R3': '3B', 'ADDC A,R4': '3C', 'ADDC A,R5': '3D', 'ADDC A,R6': '3E', 'ADDC A,R7': '3F',
    'JC rel': '40', 'AJMP 41': '41', 'ORL data,A': '42', 'ORL data,#data': '43', 'ORL A,#data': '44', 'ORL A,data': '45', 'ORL A,@R0': '46', 'ORL A,@R1': '47',
    'ORL A,R0': '48', 'ORL A,R1': '49', 'ORL A,R2': '4A', 'ORL A,R3': '4B', 'ORL A,R4': '4C', 'ORL A,R5': '4D', 'ORL A,R6': '4E', 'ORL A,R7': '4F',
    'JNC rel': '50', 'ACALL 51': '51', 'ANL data,A': '52', 'ANL data,#data': '53', 'ANL A,#data': '54', 'ANL A,data': '55', 'ANL A,@R0': '56', 'ANL A,@R1': '57',
    'ANL A,R0': '58', 'ANL A,R1': '59', 'ANL A,R2': '5A', 'ANL A,R3': '5B', 'ANL A,R4': '5C', 'ANL A,R5': '5D', 'ANL A,R6': '5E', 'ANL A,R7': '5F',
    'JZ rel': '60', 'AJMP 61': '61', 'XRL data,A': '62', 'XRL data,#data': '63', 'XRL A,#data': '64', 'XRL A,data': '65', 'XRL A,@R0': '66', 'XRL A,@R1': '67',
    'XRL A,R0': '68', 'XRL A,R1': '69', 'XRL A,R2': '6A', 'XRL A,R3': '6B', 'XRL A,R4': '6C', 'XRL A,R5': '6D', 'XRL A,R6': '6E', 'XRL A,R7': '6F',
    'JNZ rel': '70', 'ACALL 71': '71', 'ORL C,bit': '72', 'JMP @A+DPTR': '73', 'MOV A,#data': '74', 'MOV data,#data': '75', 'MOV @R0,#data': '76', 'MOV @R1,#data': '77',
    'MOV R0,#data': '78', 'MOV R1,#data': '79', 'MOV R2,#data': '7A', 'MOV R3,#data': '7B', 'MOV R4,#data': '7C', 'MOV R5,#data': '7D', 'MOV R6,#data': '7E', 'MOV R7,#data': '7F',
    'SJMP rel': '80', 'AJMP 81': '81', 'ANL C,bit': '82', 'MOVC A,@A+PC': '83', 'DIV AB': '84', 'MOV data,data': '85', 'MOV data,@R0': '86', 'MOV data,@R1': '87',
    'MOV data,R0': '88', 'MOV data,R1': '89', 'MOV data,R2': '8A', 'MOV data,R3': '8B', 'MOV data,R4': '8C', 'MOV data,R5': '8D', 'MOV data,R6': '8E', 'MOV data,R7': '8F',
    'MOV DPTR,#data16': '90', 'ACALL 91': '91', 'MOV bit,C': '92', 'MOVC A,@A+DPTR': '93', 'SUBB A,#data': '94', 'SUBB A,data': '95', 'SUBB A,@R0': '96', 'SUBB A,@R1': '97',
    'SUBB A,R0': '98', 'SUBB A,R1': '99', 'SUBB A,R2': '9A', 'SUBB A,R3': '9B', 'SUBB A,R4': '9C', 'SUBB A,R5': '9D', 'SUBB A,R6': '9E', 'SUBB A,R7': '9F',
    'ORL C,/bit': 'A0', 'AJMP A1': 'A1', 'MOV C,bit': 'A2', 'INC DPTR': 'A3', 'MUL AB': 'A4', 'Reserved A5': 'A5', 'MOV @R0,data': 'A6', 'MOV @R1,data': 'A7',
    'MOV R0,data': 'A8', 'MOV R1,data': 'A9', 'MOV R2,data': 'AA', 'MOV R3,data': 'AB', 'MOV R4,data': 'AC', 'MOV R5,data': 'AD', 'MOV R6,data': 'AE', 'MOV R7,data': 'AF',
    'ANL C,/bit': 'B0', 'ACALL B1': 'B1', 'CPL bit': 'B2', 'CPL C': 'B3', 'SWAP A': 'C4', 'XCH A,@R0': 'C6', 'XCH A,@R1': 'C7', 'XCH A,R0': 'C8', 'XCH A,R1': 'C9',
    'XCH A,R2': 'CA', 'XCH A,R3': 'CB', 'XCH A,R4': 'CC', 'XCH A,R5': 'CD', 'XCH A,R6': 'CE', 'XCH A,R7': 'CF', 'CLR A': 'E4', 'MOV A,R0': 'E8',
    'MOV A,R1': 'E9', 'MOV A,R2': 'EA', 'MOV A,R3': 'EB', 'MOV A,R4': 'EC', 'MOV A,R5': 'ED', 'MOV A,R6': 'EE', 'MOV A,R7': 'EF', 'MOV R0,A': 'F8',
    'MOV R1,A': 'F9', 'MOV R2,A': 'FA', 'MOV R3,A': 'FB', 'MOV R4,A': 'FC', 'MOV R5,A': 'FD', 'MOV R6,A': 'FE', 'MOV R7,A': 'FF'
}

#ll
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

def check_conversion(hex_input):
    # ASM -> HEX & back
    asm_result = binary_to_assembler(hex_input)
    print("ASM → BIN:")
    print(asm_result)

    
    asm_code = '\n'.join([line.split(' --> ')[1] for line in asm_result.strip().split('\n')])
    hex_result = assembler_to_binary(asm_code)
    print("\nBIN → ASM:")
    print(hex_result)

#sbor
hex_input = input(" Hex-code (ex: '00 00 00 00 01 01 01 01'):\n").replace(" ", "")
check_conversion(hex_input)
