## Anthony Krenek
## Different Ciphers

import base64


def caesar_cipher(char, shift):
    if char.isupper():
        return chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
        return chr((ord(char) + shift - 97) % 26 + 97)
    else:
        return char


def decode(encoded, shift):
    return "".join([caesar_cipher(char, shift) for char in encoded])


def main():
    encoded = "ghopbkcibrg"
    shift = 3
    print(decode(encoded, shift))


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
        return "".join(key)
