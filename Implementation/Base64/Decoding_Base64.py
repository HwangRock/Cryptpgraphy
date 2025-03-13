table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

s=input("Base64로 인코딩된 문자열 입력:")

paddingCount=s.count('=')

binary=""
for char in s.rstrip('='):
    binary+=format(table.index(char), '06b')

if paddingCount>0:
    binary=binary[:-2*paddingCount]

decodedText = ""
for i in range(0, len(binary), 8):
    decodedText+=chr(int(binary[i:i+8], 2))

print("디코딩된 문장: "+decodedText)