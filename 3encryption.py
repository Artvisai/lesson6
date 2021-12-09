def xor_cipher(s, k):
    """XOR шифрование/расшифрование"""
    crypt = ""
    for letter in s:
        crypt += chr(ord(letter) ^ k)
    return crypt


key = int(input('Input key: '))
with open('strInput.txt', 'r') as inFile:
    text = inFile.read()
encr = xor_cipher(text, key)
with open('strOutput.txt', 'w') as outFile:
    outFile.write(f'encryption:\t{encr}\n')
    outFile.write(f'decryption:\t{xor_cipher(encr, key)}')
