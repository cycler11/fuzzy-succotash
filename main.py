import re

def parse_address(addr_str):
    """Парсит строку адреса вида 'C:0x0804' или '0x0804' и возвращает целое число."""
    m = re.search(r'0x([0-9A-Fa-f]+)', addr_str)
    if m:
        return int(m.group(0), 16)
    return None

def int_to_hex8(val):
    """Преобразует число в двухсимвольное шестнадцатиричное представление."""
    return format(val & 0xFF, '02X')

def translate_line(line, current_address):
    """
    Обрабатывает строку ассемблерного кода и возвращает строку с бинарным кодом.
    Если в строке присутствует адрес (например, 'C:0x0804'), обновляет current_address.
    """
    line = line.strip()
    if not line:
        return "", current_address


#1




    # Если строка начинается с адреса (например, "C:0x0800"), извлекаем его
    addr_match = re.match(r'(C:0x[0-9A-Fa-f]+)', line)
    if addr_match:
        addr_str = addr_match.group(1)
        current_address = parse_address(addr_str)
        # После адреса строка содержит бинарный код, затем мнемонику.
        # Отсекаем адрес и бинарный код еслио н есть
        # Пример строки: "C:0x0804    D8FD     DJNZ     R0,C:0803"
        # Оставляем часть с инструкцией:
        parts = line.split()

        # Найдём позицию, где начинается мнемоника (обычно это 3-й или 4-й элемен)
        # Здесь предполагается, что бинарный код всегда состоит из одного элемента (D8FD)

        if len(parts) >= 3:
            instr_parts = parts[2:]
            instr_line = " ".join(instr_parts)
        else:
            instr_line = line
    else:
        instr_line = line

    # Обрабатываем инструкции

    # 1. CLR A
    if instr_line.upper().startswith("CLR A"):
        opcode = "E4"
        instr_len = 1
        return opcode, current_address

    # 2. DEC A
    if instr_line.upper().startswith("DEC A"):
        opcode = "14"
        instr_len = 1
        return opcode, current_address

    # 3. DEC Rn  (например, DEC R7)
    m = re.match(r"DEC\s+R(\d)", instr_line, re.IGNORECASE)
    if m:
        reg = int(m.group(1))
        # Для 8051: DEC R0 имеет код 0x18, DEC R1 – 0x19, ..., DEC R7 – 0x1F.
        opcode = format(0x18 + reg, '02X')
        instr_len = 1
        return opcode, current_address

    # 4. MOV Rn,#data (например, MOV R0,#0x7F)
    m = re.match(r"MOV\s+R(\d),\s*#(0x[0-9A-Fa-f]+|\d+)", instr_line, re.IGNORECASE)
    if m:
        reg = int(m.group(1))
        data_str = m.group(2)
        # поддержка шестнадцатиричного и десятичного литералов
        if data_str.startswith("0x") or data_str.startswith("0X"):
            data = int(data_str, 16)
        else:
            data = int(data_str)
        opcode = format(0x78 + reg, '02X')  # базовый код MOV Rn,#data для 8051: 0x78 + регистр
        data_hex = int_to_hex8(data)
        instr_len = 2
        return opcode + data_hex, current_address

    # 5. MOV @R0,A
    if re.match(r"MOV\s+@R0,\s*A", instr_line, re.IGNORECASE):
        opcode = "F6"
        instr_len = 1
        return opcode, current_address

    # 6. MOV SP(0x..) ,#data   (например, MOV SP(0x81),#0x21)
    m = re.match(r"MOV\s+SP\(\s*(0x[0-9A-Fa-f]+|\d+)\s*\),\s*#(0x[0-9A-Fa-f]+|\d+)", instr_line, re.IGNORECASE) #фильтр
    if m:
        direct_str = m.group(1)
        imm_str = m.group(2)
        if direct_str.startswith("0x") or direct_str.startswith("0X"):
            direct = int(direct_str, 16)
        else:
            direct = int(direct_str)
        if imm_str.startswith("0x") or imm_str.startswith("0X"):
            imm = int(imm_str, 16)
        else:
            imm = int(imm_str)
        
        opcode = "75"         # для MOV SP,#data инструкция имеет вид: 75 direct imm
        direct_hex = int_to_hex8(direct)
        imm_hex = int_to_hex8(imm)
        instr_len = 3
        return opcode + direct_hex + imm_hex, current_address

    # 7. DJNZ Rn,C:target
    m = re.match(r"DJNZ\s+R(\d),\s*C:([0-9A-Fa-fx]+)", instr_line, re.IGNORECASE)
    if m:
        reg = int(m.group(1))
        target_str = m.group(2)
        if not target_str.startswith("0x") and not target_str.startswith("0X"):
            target_str = "0x" + target_str
        target_addr = int(target_str, 16)
        # Инструкция занимает 2 байта. Относительный адрес вычисляется как:
        # offset = target_addr - (current_address + instr_length)
        # В нашем примере current_address = 0x0804, instr_len = 2, target = 0x0803, offset = -3 => 0xFD.
        instr_len = 2
        if current_address is None:
            raise ValueError("Неизвестен адрес инструкции для DJNZ")
        offset = target_addr - (current_address + instr_len)
        offset_hex = int_to_hex8(offset)
        opcode = format(0xD8 + reg, '02X')
        return opcode + offset_hex, current_address

    # 8. LJMP C:address
    m = re.search(r"LJMP(?:\s+\w+)?(?:\s*\(\s*C:([0-9A-Fa-fx]+)\s*\)|\s+C:([0-9A-Fa-fx]+))", instr_line, re.IGNORECASE)
    if m:
        addr = m.group(1) if m.group(1) is not None else m.group(2)
        if not addr.startswith("0x") and not addr.startswith("0X"):
            addr = "0x" + addr
        target_addr = int(addr, 16)
        opcode = "02"
        hi = (target_addr >> 8) & 0xFF
        lo = target_addr & 0xFF
        instr_len = 3
        return opcode + format(hi, '02X') + format(lo, '02X'), current_address

def translate_asm_to_bin(asm_lines):
    """
    Принимает список строк ассемблерного кода и возвращает строку,
    содержащую бинарный код в шестнадцатиричном представлении.
    """
    output = ""
    current_address = None
    for line in asm_lines:
        code, current_address = translate_line(line, current_address)
        # Если строка не содержит комментария, добавляем бинарный код
        if not code.startswith("/*"):
            output += code
        else:
            # Для отладки можно выводить сообщения об ошибках
            print(code)
    return output

# Пример использования:
if __name__ == "__main__":
    asm_code = """
C:0x0800    787F     MOV      R0,#0x7F
C:0x0802    E4       CLR      A
C:0x0803    F6       MOV      @R0,A
C:0x0804    D8FD     DJNZ     R0,C:0803
C:0x0806    758121   MOV      SP(0x81),#0x21
C:0x0809    020847   LJMP     C:0847
C:0x080C    0208F1   LJMP     main(C:08F1)
"""
    asm_lines = asm_code.strip().splitlines()
    bin_output = translate_asm_to_bin(asm_lines)
    print("Результат трансляции:")
    print(bin_output)
