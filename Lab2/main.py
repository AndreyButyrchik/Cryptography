import ShiftDecode
import ShiftEncode
import AffinDecode
import AffinEncode

textFile = open('text.txt', 'r')
text = textFile.read()
keysFile = open('keyShift.txt', 'r')
key = int(keysFile.readline())
textFile.close()
keysFile.close()

encodeText = ShiftEncode.chiperShiftEncode(text, key)
encodeFile = open('chipherShiftEncode.txt', 'w')
encodeFile.write(encodeText)
encodeFile.close()

encodeFile = open('chipherShiftEncode.txt', 'r')
encodeText = encodeFile.read()
decodeText = ShiftDecode.chiperShiftDecode(encodeText, key)
decodeFile = open('chipherShiftDecode.txt', 'w')
decodeFile.write(decodeText)
encodeFile.close()
decodeFile.close()

textFile = open('text.txt', 'r')
text = textFile.read()
keysFile = open('keyAffin.txt', 'r')
key = [int(item) for item in keysFile.readline().split()]
encodeText = AffinEncode.chiperAffineEncode(text, key)
encodeFile = open('chipherAffineEncode.txt', 'w')
encodeFile.write(encodeText)
textFile.close()
encodeFile.close()

encodeFile = open('chipherAffineEncode.txt', 'r')
encodeText = encodeFile.read()
decodeText = AffinDecode.chiperAffinDecode(encodeText, key)
decodeFile = open('chipherAffinDecode.txt', 'w')
decodeFile.write(decodeText)
encodeFile.close()
decodeFile.close()
