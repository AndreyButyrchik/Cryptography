import string

ALPHABET = list(string.ascii_lowercase)

def chiperShiftDecode(text, key):
    decodeText = ''
    for i in range(len(text)):
        if (text[i] in ALPHABET):
            decodeText += ALPHABET[(ALPHABET.index(text[i]) - key) % len(ALPHABET)]
        else:
            decodeText += text[i]
    return decodeText