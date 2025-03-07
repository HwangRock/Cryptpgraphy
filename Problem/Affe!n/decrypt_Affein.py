class Affine:
    def __init__(self, key1, key2):
        assert isinstance(key1, int) and 1 <= key1 <= 250 # key는 무조건 1~250으로 제한
        assert isinstance(key2, int) and 1 <= key2 <= 250
        self._key1 = key1
        self._key2 = key2

    def encrypt(self, msg):
        msg_enc = b"" # 데이터를 바이트(byte) 단위로 표현
        for b in msg:
            msg_enc = msg_enc + bytes([(self._key1 * b + self._key2) % 251])
        return msg_enc

    def decrypt(self, msg):
        msg_dec = b""
        for b in msg:
            msg_dec = msg_dec + bytes([pow(self._key1, -1, 251) * (b - self._key2) % 251])
        return msg_dec

enc_file=open("output.txt","r")
enc_msg=bytes.fromhex(enc_file.read().split("> ")[1])

fin=False
for k1 in range(1,251):
    for k2 in range(1,251):
        decoder=Affine(k1,k2)
        currentStr=decoder.decrypt(enc_msg)
        print("current key is "+str(k1)+" "+str(k2))
        if b'cryptography' in currentStr:
            print("answer! key is:"+"("+str(k1)+" "+str(k2)+")")
            flag=open("flag.txt","w")
            flag.write(currentStr.decode("utf-8"))
            flag.close()
            fin=True
            break

    if fin:
        break
