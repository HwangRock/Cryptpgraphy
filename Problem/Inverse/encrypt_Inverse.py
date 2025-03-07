import urllib.parse


key = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O',
    'J': 'P', 'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G', 'P': 'H', 'Q': 'J', 'R': 'K',
    'S': 'L', 'T': 'Z', 'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M',
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o',
    'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k',
    's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm',
}

def change(data, key):
    return ''.join(key.get(char, char) for char in data)

def encoding(data):
    return urllib.parse.quote(data)

def encrypt(plaintext):
    substituted = change(plaintext, key)
    final_encrypted = encoding(substituted)
    return final_encrypted

if __name__ == "__main__":
    plaintext = "0xH0P3{Fake_Flag}"
    encrypted = encrypt(plaintext)
    with open("encrypted.txt", "w") as f:
        f.write(encrypted)
