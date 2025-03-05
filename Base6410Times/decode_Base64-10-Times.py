import base64

with open("encoded.txt","rb") as f:
    s=f.read()

for i in range(11):
    s = base64.b64decode(s)

s=s.decode("utf-8")


print(s)