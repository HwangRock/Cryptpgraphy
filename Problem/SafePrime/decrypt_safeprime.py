from Crypto.Util.number import long_to_bytes,isPrime
from premise import N1, N2, e, FLAG1_enc, FLAG2_enc,p1

from sympy import mod_inverse

p2=0
while True:
    p2=p1*2+1
    if isPrime(p2):
        break

q1=N1//p1
q2=N2//p2

phi_N1=(p1-1)*(q1-1)
phi_N2=(p2-1)*(q2-1)

d1=mod_inverse(e,phi_N1)
d2=mod_inverse(e,phi_N2)

FLAG1=pow(FLAG1_enc,d1,N1)
FLAG2=pow(FLAG2_enc,d2,N2)

str1=long_to_bytes(FLAG1)
str2=long_to_bytes(FLAG2)

FLAG=str1+str2
print("FLAG:", FLAG.decode('utf-8'))
