## Description

Scripts to modify the strings for both ITC and SBX. Put these scripts in the same folder as the .bin/.txt files you are editing.
"string_edit.py" script dumps and builds string packs to/from .bin/.txt files.
"string_remap.py" uses a python dictionary to substitute unused Kanji with accented Latin in a given .txt.

## String information

In groups of 4 bytes are pointers to text string within bin file via decimal. In an example,
byte 34 01 would point to decimal offset 308 (from file start) because endian reorder would
be 01 34 which is 308 in decimal. Text is in UTF-16 Big Endian while in the .bin file.
While most normal strings terminate in 00 00 00, some don't. These exceptions are denoted
in the guide below. The "string_edit.py" script handles the triple null terminator automatically.

## Writing new game text

After dumping a string .bin into a .text you can simply edit any of the strings in your text
editor of choice. Once you have saved your changes, build the txt back into a bin using the
same "string_edit.py" script. For special instances like important text (i.e. character names)
you might want to refer to the guide below for writing "special" text.

# Guide for writing new strings "special" text

```
$\ Colored text starter 1 (tends to be used for character names)
*\ Colored text starter 2 (tends to be used for emphasis)
\* Colored text terminator (same terminator for both colors)
newline\> Next page for conversations (any of the P.A. conversations that are more than one sentence should have these)
\\ Required terminator for ticker reels (the horizontally scrolling text in the garage menu)
\.\ Terminator for character bios
?\ Unknown terminator
#\ Float values (i.e. time attack time or car stats)
```

# Example of a string using all of the above "special" text

```
$\Matterhorn\*, who hangs out at the Shibuya Parking Area,
comes by his fondness for the Fairlady Z honestly: his father
was also fond of them. 
\>Apparently, this is why he only races against other drivers who 
also appreciate similar *\Z-series\* cars.
```

# General information about the string bins below (Y/N are for if string counts match between ITC vs SBX):

00022638.bin/00022637.bin - |Y| Car names and descriptions NOTE:JP TEXT GOES MAX ~2176 bytes
00022639.bin/00022638.bin - |N| Menu dialog i.e. "Would you like to enter a Storage Device where game data is saved?" or shop item descriptions
00022640.bin/00022639.bin - |Y| Menu dialog related to the map i.e. "You will return to garage, is that okay?"
00022641.bin/00022640.bin - |Y| NPC names, rival list description, and some dialog.
00022642.bin/00022641.bin - |N| Japanese city names
00022643.bin/00022642.bin - |N| B.A.D. Names
00022644.bin/00022643.bin - |Y| dialog
00022645.bin/00022644.bin - |Y| dialog
00022646.bin/00022645.bin - |Y| dialog
00022647.bin/00022646.bin - |Y| dialog Camper angle
00022648.bin/00022647.bin - |Y| dialog Nissan 70 Supra
00022649.bin/00022648.bin - |Y| dialog Nissan 80 Supra
00022650.bin/00022649.bin - |Y| dialog
00022651.bin/00022650.bin - |Y| dialog
00022652.bin/00022651.bin - |Y| dialog Camper angle
00022653.bin/00022652.bin - |Y| online system messages? i.e. "Your opponent has stopped responding."
00022654.bin/00022653.bin - |Y| garage notifications i.e. "BRAKE LEVEL 5 has become available"

# Below is the snippet from the python script of all of the character glyphs that get converted, edit if needed for new languages

# Dictionary for new character glyphs
```
new_chars = {
    'chars': [
        'Á', 'À', 'Â', 'Ã', 'Ä', 'Å', 'Ā', 'Ă', 'Ą', 'Ǎ', 'Ǻ', 'á', 'à', 'â', 'ã', 'ä', 'å', 'ā', 'ă', 'ą',
        'ǎ', 'ǻ', 'É', 'È', 'Ê', 'Ë', 'Ē', 'Ĕ', 'Ė', 'Ę', 'Ě', 'é', 'è', 'ê', 'ë', 'ē', 'ĕ', 'ė', 'ę', 'ě',
        'Í', 'Ì', 'Î', 'Ï', 'Ī', 'Ĭ', 'Į', 'Ǐ', 'í', 'ì', 'î', 'ï', 'ī', 'ĭ', 'į', 'ǐ', 'Ó', 'Ò', 'Ô', 'Õ',
        'Ö', 'Ø', 'Ō', 'Ŏ', 'Ő', 'Ǒ', 'ó', 'ò', 'ô', 'õ', 'ö', 'ø', 'ō', 'ŏ', 'ő', 'ǒ', 'Ú', 'Ù', 'Û', 'Ü',
        'Ū', 'Ŭ', 'Ů', 'Ű', 'Ų', 'Ǔ', 'ú', 'ù', 'û', 'ü', 'ū', 'ŭ', 'ů', 'ű', 'ų', 'ǔ', 'Ý', 'Ŷ', 'Ÿ', 'Ỳ',
        'ý', 'ŷ', 'ÿ', 'ỳ', 'Ç', 'Ć', 'Ĉ', 'Ċ', 'Č', 'ç', 'ć', 'ĉ', 'ċ', 'č', 'Ĝ', 'Ğ', 'Ġ', 'Ģ', 'ĝ', 'ğ',
        'ġ', 'ģ', 'Ĥ', 'Ħ', 'ĥ', 'ħ', 'Ĵ', 'ĵ', 'Ķ', 'ķ', 'Ĺ', 'Ļ', 'Ľ', 'Ŀ', 'Ł', 'ĺ', 'ļ', 'ľ', 'ŀ', 'ł',
        'Ń', 'Ņ', 'Ň', 'Ŋ', 'ń', 'ņ', 'ň', 'ŋ', 'Ŕ', 'Ŗ', 'Ř', 'ŕ', 'ŗ', 'ř', 'Ś', 'Ŝ', 'Ş', 'Š', 'ś', 'ŝ',
        'ş', 'š', 'Ţ', 'Ť', 'Ŧ', 'ţ', 'ť', 'ŧ', 'Ź', 'Ż', 'Ž', 'ź', 'ż', 'ž', 'Ď', 'Đ', 'ď', 'đ', 'ð', 'Þ',
        'þ', '☺'
    ]
}
# Sacrificial kanji that the above characters will be remapped to
jp_chars = {
    'chars': [
        '訓', '群', '軍', '係', '傾', '兄', '啓', '圭', '型', '契', '形', '恵', '慶', '掲', '携', '景', '渓', '畦', '系', '経',
        '健', '兼', '剣', '堅', '嫌', '建', '憲', '懸', '検', '権', '牽', '犬', '献', '研', '県', '肩', '見', '謙', '賢', '遣',
        '戸', '故', '湖', '虎', '誇', '鼓', '五', '互', '午', '呉', '吾', '後', '御', '悟', '語', '誤', '護', '醐', '交', '候',
        '抗', '拘', '控', '攻', '昂', '晃', '更', '校', '構', '江', '浩', '溝', '甲', '皇', '稿', '紅', '絞', '綱', '耕', '考',
        '酷', '黒', '獄', '腰', '忽', '惚', '骨', '込', '此', '頃', '今', '困', '婚', '懇', '昏', '根', '混', '痕', '魂', '些',
        '犀', '砕', '祭', '斎', '細', '菜', '載', '際', '剤', '在', '材', '冴', '坂', '咲', '崎', '作', '削', '昨', '策', '索',
        '暫', '残', '仕', '使', '刺', '司', '史', '四', '士', '始', '姿', '子', '市', '師', '志', '思', '指', '支', '施', '旨',
        '寺', '持', '時', '次', '治', '示', '耳', '自', '辞', '鹿', '式', '識', '軸', '七', '叱', '執', '失', '室', '湿', '疾',
        '若', '寂', '弱', '主', '取', '守', '手', '殊', '狩', '種', '腫', '趣', '酒', '首', '受', '呪', '寿', '授', '樹', '収',
        '渋', '獣'
    ]
}
```