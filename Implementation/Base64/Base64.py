class Base64:
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def __init__(self, text):
        self.text=text

    def encode(self):
        binary = ''.join(format(ord(char), '08b') for char in self.text)

        mod = len(binary) % 6
        if mod != 0:
            binary += '0' * (6 - mod)

        encodedText = ""
        a = 0
        for i, j in enumerate(binary):
            a += int(j) * (2 ** (5 - i % 6))

            if (i + 1) % 6 == 0:
                encodedText += Base64.table[a]
                a = 0

        padding = (3 - len(self.text) % 3) % 3
        encodedText += "=" * padding

        return encodedText

    def decode(self):
        paddingCount = self.text.count('=')

        binary = ""
        for char in self.text.rstrip('='):
            binary += format(Base64.table.index(char), '06b')

        if paddingCount > 0:
            binary = binary[:-2 * paddingCount]

        decodedText = ""
        for i in range(0, len(binary), 8):
            decodedText += chr(int(binary[i:i + 8], 2))

        return decodedText

#테스트 코드
'''
s=input("인코딩할 문장: ")
enc=Base64(s)
encTxt=enc.encode()
print("인코딩된 문장: "+encTxt)
dec=Base64(encTxt)
decTxt=dec.decode()
print("디코딩된 문장: "+decTxt)
'''