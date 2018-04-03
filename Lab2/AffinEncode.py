import string

ALPHABET = list(string.ascii_lowercase)

def chiperAffineEncode(text, key):
    encodeText = ''
    for i in range(len(text)):
        if (text[i] in ALPHABET):
            encodeText += ALPHABET[(key[0] * ALPHABET.index(text[i]) + key[1]) % len(ALPHABET)]
        else:
            encodeText += text[i]
    return encodeText