import string
import InverseMod

ALPHABET = list(string.ascii_lowercase)

def chiperAffinDecode(text, key):
    decodeText = ''
    for i in range(len(text)):
        if (text[i] in ALPHABET):
            decodeText += ALPHABET[(InverseMod.modinv(key[0], len(ALPHABET)) * (ALPHABET.index(text[i]) - key[1])) % len(ALPHABET)]
        else:
            decodeText += text[i]
    return decodeText