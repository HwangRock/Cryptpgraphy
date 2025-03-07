class Caesar:
    def __init__(self, key):
        assert isinstance(key, int) and 1 <= key <= 255
        self._key = key

    def encrypt(self, msg):
        msg_enc = b""
        for b in msg:
            msg_enc = msg_enc + bytes([(b + self._key) % 256])
        return msg_enc

    def decrypt(self, msg):
        msg_dec = b""
        for b in msg:
            msg_dec = msg_dec + bytes([(b - self._key) % 256])
        return msg_dec


with open("want.txt", "r") as f:
    enc = f.read()

enc=bytes.fromhex(enc)
print(enc)

for i in range(1,255):
    cipher=Caesar(i)
    dec=cipher.decrypt(enc)
    if b'DH' in dec:
        print(dec)