MORSE_EN = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '/': '-..-.', '@': '.--.-.', ' ': '/'
}
MORSE_FA = {
    'ا': '.-', 'ب': '-...', 'پ': '.--.', 'ت': '-',
    'ث': '-.-.', 'ج': '.---', 'چ': '---.', 'ح': '....',
    'خ': '-..-', 'د': '-..', 'ذ': '...-', 'ر': '.-.',
    'ز': '--..', 'ژ': '--.', 'س': '...', 'ش': '----',
    'ص': '.-.-', 'ض': '..-..', 'ط': '..-', 'ظ': '-.--',
    'ع': '---', 'غ': '..--', 'ف': '..-.', 'ق': '---.',
    'ک': '-.-', 'گ': '--..-', 'ل': '.-..', 'م': '--',
    'ن': '-.', 'و': '.--', 'ه': '..--..', 'ی': '..',
    '،': '-.-.--', '؛': '-.-.-.', '؟': '..-.-', ' ': '/'
}
MORSE = {**MORSE_EN, **MORSE_FA}
REVERSE_EN = {v: k for k, v in MORSE_EN.items()}
REVERSE_FA = {v: k for k, v in MORSE_FA.items()}

def encode(text):
    result = []
    for char in text.upper():
        if char in MORSE:
            result.append(MORSE[char])
        else:
            result.append('?')
    return ' '.join(result)


def decode(morse, lang='en'):
    result = []
    codes = morse.split(' ')
    for code in codes:
        if lang == 'en' and code in REVERSE_EN:
            result.append(REVERSE_EN[code])
        elif lang == 'fa' and code in REVERSE_FA:
            result.append(REVERSE_FA[code])
        else:
            result.append('?')
    return ''.join(result)
while True :
    choose = input("1.encode \n2.decode\n3.Exit\n-----\n")
    if choose == "1" :
        text = input("-----\nenter a word :")
        print("result: ",encode(text),"\n-----")
    elif choose == "2" :
        lang = input("-----\nfa\nen\n-----\n")
        morse = input("-----\nenter a morse :")
        print("result: ",decode(morse,lang),"\n-----")
    elif choose == "3" :
        print("\n-----\nGood bye!")
        break
    else :
        print("-----\nplease choose 1 , 2 or 3 !\n-----")
