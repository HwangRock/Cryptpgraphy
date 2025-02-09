with open('encfile', 'r', encoding='utf-8') as f:
    encrypt = f.read()

encrypt = [encrypt[i:i+2] for i in range(0, len(encrypt), 2)]

hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

length = len(encrypt)

plainText = list(range(length))

for i in range(length):
    hex_val = encrypt[i]
    dec = hex_list.index(hex_val)
    plainText[i] = (dec - 128 + 256) % 256

plainText = bytes(plainText)

with open('decoded_flag.png', 'wb') as f:
    f.write(plainText)

