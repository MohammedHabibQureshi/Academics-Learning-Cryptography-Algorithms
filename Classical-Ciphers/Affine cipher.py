
### Affine cipher Encryption
"""
text = input("Enter the plain text: ")
a = int(input("Enter key a: "))
b = int(input("Enter key b: "))
cipher = ""

for char in text:
    if char.isalpha():
        if char.isupper():
            x = (a * (ord(char) - 65) + b) % 26 + 65
            cipher += chr(x)
        else:
            x = (a * (ord(char) - 97) + b) % 26 + 97
            cipher += chr(x)
    else:
        cipher += char

print("Plain text is:", text)
print("Cipher text is:", cipher)

"""




### Affine cipher Decryption
text = input("Enter your name (plaintext): ")
a = int(input("Enter key a: "))
b = int(input("Enter key b: "))
cipher = ""

a_inv = pow(a, -1, 26)
for char in text:
    if char.isalpha():
        if char.isupper():
            x = (a_inv * (ord(char) - 65) - b) % 26
            cipher += chr(x + 65)
        else:
            x = (a_inv * (ord(char) - 97) - b) % 26 + 97
            cipher += chr(x + 97)
    else:
        cipher += char  

print("Plain text is:", text)
print("Cipher text is:", cipher)

