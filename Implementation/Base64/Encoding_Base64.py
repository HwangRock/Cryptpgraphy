
s = input("인코딩할 문자열을 입력: ")

binary = ''.join(format(ord(char), '08b') for char in s)

mod = len(binary) % 6
if mod != 0:
    binary += '0' * (6 - mod)

table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

encodedText = ""
a = 0
for i, j in enumerate(binary):
    a += int(j) * (2 ** (5 - i % 6))

    if (i + 1) % 6 == 0:
        encodedText += table[a]
        a = 0

padding = (3 - len(s) % 3) % 3
encodedText += "=" * padding


print("인코딩된 문자열: "+encodedText)
