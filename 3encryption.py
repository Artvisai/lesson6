def xor_cipher(str, key):
    crypt = ""
    for letter in str:
        crypt += chr(ord(letter) ^ key)
    return crypt


key = int(input('Input key: '))
with open('str.txt', 'r') as inFile:
    text = inFile.read()
print("original:\t", text)
encr = xor_cipher(text, key)
print("encryption:\t", encr)
print("decryption:\t", xor_cipher(encr, key))
