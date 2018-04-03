import string

ALPHABET = list(string.ascii_lowercase)

def chiperShiftEncode(text, key):
    encodeText = ''
    for i in range(len(text)):
        if (text[i] in ALPHABET):
            encodeText += ALPHABET[(ALPHABET.index(text[i]) + key) % len(ALPHABET)]
        else:
            encodeText += text[i]
    return encodeText