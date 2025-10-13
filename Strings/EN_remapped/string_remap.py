import os

def utf16_be_encode(char_list):
    return [char.encode('utf-16-be') for char in char_list]

# Dictionary for new character glyphs
new_chars = {
    "chars": [
        "Á", "À", "Â", "Ã", "Ä", "Å", "Ā", "Ă", "Ą", "Ǎ", "Ǻ", "á", "à", "â", "ã", "ä", "å", "ā", "ă", "ą",
        "ǎ", "ǻ", "É", "È", "Ê", "Ë", "Ē", "Ĕ", "Ė", "Ę", "Ě", "é", "è", "ê", "ë", "ē", "ĕ", "ė", "ę", "ě",
        "Í", "Ì", "Î", "Ï", "Ī", "Ĭ", "Į", "Ǐ", "í", "ì", "î", "ï", "ī", "ĭ", "į", "ǐ", "Ó", "Ò", "Ô", "Õ",
        "Ö", "Ø", "ō", "Ŏ", "Ő", "Ǒ", "ó", "ò", "ô", "õ", "ö", "ø", "ō", "ŏ", "ő", "ǒ", "Ú", "Ù", "Û", "Ü",
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

new_chars["chars"] = utf16_be_encode(new_chars["chars"])
jp_chars["chars"] = utf16_be_encode(jp_chars["chars"])

def transform_char(text):
    # Ensure we're working with the byte-encoded dictionaries for remapping
    char_map = dict(zip(new_chars["chars"], jp_chars["chars"]))
    transformed = []
    i = 0
    while i < len(text):
        # Check the current 2-byte slice
        byte_pair = text[i:i+2]
        if byte_pair in char_map:
            # If match, append the corresponding transformation
            transformed.append(char_map[byte_pair])
            i += 2  # Move by 2 bytes
        else:
            transformed.append(byte_pair)
            i += 2  # Move by 2 bytes if no transformation
    return b''.join(transformed)

if __name__ == "__main__":
    file_choice = input("Which text file would you like to character remap (type 'all' for all in folder):\n")
    
    # If the user selects "all", loop through all .txt files in the current directory
    if file_choice.lower() == "all":
        for filename in os.listdir("."):
            if filename.endswith(".txt"):
                with open(filename, "rb") as file:  # Read as binary
                    content = file.read()
                transformed_content = transform_char(content)
                with open(filename, "wb") as file:  # Write as binary
                    file.write(transformed_content)
                print(f"Processed file: {filename}")
    else:
        # Process a single file
        if not file_choice.endswith(".txt"):
            file_choice += ".txt"
        if os.path.exists(file_choice):
            with open(file_choice, "rb") as file:  # Read as binary
                content = file.read()
            transformed_content = transform_char(content)
            with open(file_choice, "wb") as file:  # Write as binary
                file.write(transformed_content)
            print(f"Processed file: {file_choice}")
        else:
            print(f"File '{file_choice}' not found.")