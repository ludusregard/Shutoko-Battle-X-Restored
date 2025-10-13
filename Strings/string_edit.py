import os
import struct
import re

# Dictionary for new character glyphs
new_chars = {
    "chars": [
        "Á", "À", "Â", "Ã", "Ä", "Å", "Ā", "Ă", "Ą", "Ǎ", "Ǻ", "á", "à", "â", "ã", "ä", "å", "ā", "ă", "ą",
        "ǎ", "ǻ", "É", "È", "Ê", "Ë", "Ē", "Ĕ", "Ė", "Ę", "Ě", "é", "è", "ê", "ë", "ē", "ĕ", "ė", "ę", "ě",
        "Í", "Ì", "Î", "Ï", "Ī", "Ĭ", "Į", "Ǐ", "í", "ì", "î", "ï", "ī", "ĭ", "į", "ǐ", "Ó", "Ò", "Ô", "Õ",
        "Ö", "Ø", "Ō", "Ŏ", "Ő", "Ǒ", "ó", "ò", "ô", "õ", "ö", "ø", "ō", "ŏ", "ő", "ǒ", "Ú", "Ù", "Û", "Ü",
        "Ū", "Ŭ", "Ů", "Ű", "Ų", "Ǔ", "ú", "ù", "û", "ü", "ū", "ŭ", "ů", "ű", "ų", "ǔ", "Ý", "Ŷ", "Ÿ", "Ỳ",
        "ý", "ŷ", "ÿ", "ỳ", "Ç", "Ć", "Ĉ", "Ċ", "Č", "ç", "ć", "ĉ", "ċ", "č", "Ĝ", "Ğ", "Ġ", "Ģ", "ĝ", "ğ",
        "ġ", "ģ", "Ĥ", "Ħ", "ĥ", "ħ", "Ĵ", "ĵ", "Ķ", "ķ", "Ĺ", "Ļ", "Ľ", "Ŀ", "Ł", "ĺ", "ļ", "ľ", "ŀ", "ł",
        "Ń", "Ņ", "Ň", "Ŋ", "ń", "ņ", "ň", "ŋ", "Ŕ", "Ŗ", "Ř", "ŕ", "ŗ", "ř", "Ś", "Ŝ", "Ş", "Š", "ś", "ŝ",
        "ş", "š", "Ţ", "Ť", "Ŧ", "ţ", "ť", "ŧ", "Ź", "Ż", "Ž", "ź", "ż", "ž", "Ď", "Đ", "ď", "đ", "ð", "Þ",
        "þ", "☺"
    ]
}
# Sacrificial kanji that the above characters will be remapped to
jp_chars = {
    "chars": [
        "訓", "群", "軍", "係", "傾", "兄", "啓", "圭", "型", "契", "形", "恵", "慶", "掲", "携", "景", "渓", "畦", "系", "経",
        "健", "兼", "剣", "堅", "嫌", "建", "憲", "懸", "検", "権", "牽", "犬", "献", "研", "県", "肩", "見", "謙", "賢", "遣",
        "戸", "故", "湖", "虎", "誇", "鼓", "五", "互", "午", "呉", "吾", "後", "御", "悟", "語", "誤", "護", "醐", "交", "候",
        "抗", "拘", "控", "攻", "昂", "晃", "更", "校", "構", "江", "浩", "溝", "甲", "皇", "稿", "紅", "絞", "綱", "耕", "考",
        "酷", "黒", "獄", "腰", "忽", "惚", "骨", "込", "此", "頃", "今", "困", "婚", "懇", "昏", "根", "混", "痕", "魂", "些",
        "犀", "砕", "祭", "斎", "細", "菜", "載", "際", "剤", "在", "材", "冴", "坂", "咲", "崎", "作", "削", "昨", "策", "索",
        "暫", "残", "仕", "使", "刺", "司", "史", "四", "士", "始", "姿", "子", "市", "師", "志", "思", "指", "支", "施", "旨",
        "寺", "持", "時", "次", "治", "示", "耳", "自", "辞", "鹿", "式", "識", "軸", "七", "叱", "執", "失", "室", "湿", "疾",
        "若", "寂", "弱", "主", "取", "守", "手", "殊", "狩", "種", "腫", "趣", "酒", "首", "受", "呪", "寿", "授", "樹", "収",
        "渋", "獣"
    ]
}

def transform_char(text):
    # Uses above dictionaries to remap characters in text
    char_map = dict(zip(new_chars["chars"], jp_chars["chars"]))
    return "".join(char_map.get(c, c) for c in text)

def transform_string(string_data):
    # Transform specific hex sequences in the string data.
    result = []
    i = 0
    while i < len(string_data):
        if string_data[i:i+5] == b"\x00\x20\x00\x00\x00": # Terminator for ticker reels (scrolling menu text)
            result.append("\\\\".encode('utf-16-be'))
            i += 5
        elif string_data[i:i+2] == b"\xff\xfc": # Color/character name text marker end
            result.append("*\\".encode('utf-16-be'))
            i += 2
        elif string_data[i:i+2] == b"\xff\xfe": # Character name marker start
            result.append("$\\".encode('utf-16-be'))
            i += 2
        elif string_data[i:i+2] == b"\xff\xff": # Team name marker start
            result.append("+\\".encode('utf-16-be'))
            i += 2
        elif string_data[i:i+2] == b"\xff\xd6": # Color text marker start
            result.append("\\*".encode('utf-16-be'))
            i += 2
        elif string_data[i:i+2] == b"\xff\xd1": # Next page for conversations
            result.append("\n\\>".encode('utf-16-be'))
            i += 2
        elif string_data[i:i+5] == b"\x00\x2e\x00\x00\x00": # Terminator for character bios
            result.append("\\.\\".encode('utf-16-be'))
            i += 5
        elif string_data[i:i+2] == b"\x00\x30": # The number 0 (needed so below doesnt fuck it up on transform)
            result.append("0".encode('utf-16-be'))
            i += 2
        elif string_data[i:i+4] == b"\x30\x00\x30\x00": #  Float values (i.e. player/car stats)
            result.append("#\\".encode('utf-16-be'))
            i += 4
        else:
            result.append(bytes([string_data[i]]))
            i += 1
    transformed = b"".join(result)
    
    if transformed[-3:] == b"\x00\x00\x00":
        transformed = transformed[:-3]
    if len(transformed) % 2 == 0 and transformed[-2:] == b"\x00\x00":
        transformed = transformed[:-2]     
        
    return transformed

def inverse_transform_string(transformed_data):
    # Inverse transform specific sequences back to hex.
    result = []
    i = 0
    while i < len(transformed_data):
        if transformed_data[i:i+4] == b"\x00\x5C\x00\x5C":  # Transform "\\" to "00 20"
            result.append(b"\x00\x20")
            i += 4
        elif transformed_data[i:i+4] == b"\x00\x2A\x00\x5C":  # Transform "*\" to "FF FC"
            result.append(b"\xff\xfc")
            i += 4
        elif transformed_data[i:i+4] == b"\x00\x24\x00\x5C":  # Transform "$\" to "FF FE"
            result.append(b"\xff\xfe")
            i += 4
        elif transformed_data[i:i+4] == b"\x00\x2B\x00\x5C":  # Transform "+\" to "FF FF"
            result.append(b"\xff\xff")
            i += 4
        elif transformed_data[i:i+4] == b"\x00\x5C\x00\x2A":  # Transform "\*" to "FF D6"
            result.append(b"\xff\xd6")
            i += 4
        elif transformed_data[i:i+6] == b"\x00\x0A\x00\x5C\x00\x3E":  # Transform "\n\>" (to "FF D1"
            result.append(b"\xff\xd1")
            i += 6
        elif transformed_data[i:i+6] == b"\x00\x5C\x00\x2E\x00\x5C":  # Transform "\.\" to "00 2E"
            result.append(b"\x00\x2e")
            i += 6
        elif transformed_data[i:i+4] == b"\x00\x23\x00\x5C":  # Transform "#\" to "30 00 30 00"
            result.append(b"\x30\x00\x30\00")
            i += 4
        else:
            result.append(bytes([transformed_data[i]]))  # Append single byte if no match
            i += 1
    return b"".join(result)

def build_bin_file(input_txt):
    if not os.path.isfile(input_txt):
        print(f"File {input_txt} not found.")
        return

    with open(input_txt, "rb") as f:
        f.seek(38)  # Skip the first 38 bytes "### String 1 ###\n\n"
        data = f.read()

    # Define binary string markers
    string_marker_start = "\n\n### String ".encode("utf-16-be")
    string_marker_end = " ###\n\n".encode("utf-16-be")

    # Split the binary content using markers
    marker_pattern = re.escape(string_marker_start) + b".*?" + re.escape(string_marker_end)
    string_data_list = re.split(marker_pattern, data)

    num_strings = len(string_data_list)
    print(f"Number of strings: {num_strings}")
    
    binary_data = bytearray()
    binary_data.extend(struct.pack("<I", num_strings))
    
    pointers = []
    current_pointer = 6 + (4 * num_strings)
    transformed_strings = []

    for string_data in string_data_list:
        transformed_string = inverse_transform_string(string_data) + b"\x00\x00\x00"
        transformed_strings.append(transformed_string)
        pointers.append(current_pointer)
        current_pointer += len(transformed_string)
        
    for pointer in pointers:
        binary_data.extend(struct.pack("<I", pointer))
        
    binary_data.extend(b'\x00\x00')
    
    for transformed_string in transformed_strings:
        binary_data.extend(transformed_string)

    output_bin = os.path.splitext(input_txt)[0] + ".bin"
    with open(output_bin, "wb") as f:
        f.write(binary_data)

    print(f"Packed all strings to {output_bin}")

def dump_bin_file(input_bin):
    # Dump strings from the binary file to a readable text file.
    if not os.path.isfile(input_bin):
        print(f"File {input_bin} not found.")
        return

    with open(input_bin, "rb") as f:
        data = f.read()

    num_strings = struct.unpack("<I", data[:4])[0]
    print(f"Number of strings: {num_strings}")

    pointer_table_start = 4
    pointer_table_end = pointer_table_start + (num_strings * 4)
    
    pointers = [
        struct.unpack_from("<I", data, pointer_table_start + i * 4)[0]
        for i in range(num_strings)
    ]

    output_file = os.path.splitext(input_bin)[0] + ".txt"

    # Write extracted strings
    with open(output_file, "wb") as f_out:
        # UTF-16 BE BOM
        f_out.write(b"\xFE\xFF")

        for i, start in enumerate(pointers):
            end = pointers[i + 1] if i + 1 < num_strings else len(data)
            string_data = data[start:end]

            transformed = transform_string(string_data)

            section_header = (
                f"\n\n### String {i + 1} ###\n\n" if i > 0 else "### String 1 ###\n\n"
            )
            f_out.write(section_header.encode("utf-16-be"))
            f_out.write(transformed)

    print(f"Dumped {num_strings} strings to '{output_file}'.")
    
def dump_all_bin_files():
    folder = input("Enter the folder to dump .bin files from: ").strip()
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' does not exist.")
        return

    for file in os.listdir(folder):
        if file.endswith(".bin"):
            file_path = os.path.join(folder, file)
            print(f"Dumping {file_path}...")
            dump_bin_file(file_path)

def build_all_txt_files():
    folder = input("Enter the folder to build .txt files from: ").strip()
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' does not exist.")
        return

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            file_path = os.path.join(folder, file)
            print(f"Building {file_path}...")
            build_bin_file(file_path)

if __name__ == "__main__":
    prompter = input("Enter [1] to dump strings, [2] to build strings, or [3] to process all: \n")
    if prompter == "1":
        input_bin = input("Enter the .bin strings to dump: ")
        if input_bin.lower() == "all":
            dump_all_bin_files()
        else:
            if not input_bin.endswith(".bin"):
                input_bin += ".bin"
            dump_bin_file(input_bin)
    elif prompter == "2":
        input_txt = input("Enter the .txt strings to build: ")
        if input_txt.lower() == "all":
            build_all_txt_files()
        else:
            if not input_txt.endswith(".txt"):
                input_txt += ".txt"
            build_bin_file(input_txt)
    elif prompter.lower() == "3":
        action = input("Enter [1] to dump all or [2] to build all: ")
        if action == "1":
            dump_all_bin_files()
        elif action == "2":
            build_all_txt_files()
        else:
            print("Invalid action. Exiting.")
    else:
        print("Invalid choice. Exiting.")