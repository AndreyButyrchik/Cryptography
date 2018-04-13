from encription import encrypt
from decription import decrypt


with open('text.txt', 'rb') as textFile:
    text = textFile.read()
textFile.close()

with open('key.txt', 'rb') as keyFile:
    key = keyFile.read()
keyFile.close()

if len(key) <= 16:
    with open('encriptText.txt', 'wb') as encFile:
        for i in range(0, len(text), 16):
            encFile.write(encrypt(text[i:i + 16], key))
    encFile.close()

    with open('encriptText.txt', 'rb') as encFile:
        encriptText = encFile.read()
    encFile.close()

    with open('decriptText.txt', 'wb') as decFile:
        for i in range(0, len(encriptText), 16):
            decFile.write(decrypt(encriptText[i:i + 16], key))
    decFile.close()
else:
    print('Invalid key')
