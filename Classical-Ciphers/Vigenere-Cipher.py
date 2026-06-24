
### Vigenere cipher Encryption
text = input("Enter the plain text: ")
key = input("Enter the key: ")
cipher = ""

j = 0  
for char in text:
    if char.isalpha():
        shift = ord(key[j % len(key)].lower()) - 97
        if char.isupper():
            x = (ord(char) - 65 + shift) % 26 + 65
        else:
            x = (ord(char) - 97 + shift) % 26 + 97
        cipher += chr(x)
        j += 1
    else:
        cipher += char  

print("Plain text is: " + text)
print("Key is: " + key)
print("Cipher text is: " + cipher)



### Vigenere cipher Decryption
text = input("Enter the plain text: ")
key = input("Enter the key: ")
cipher = ""

j = 0  
for char in text:
    if char.isalpha():
        shift = ord(key[j % len(key)].lower()) - 97
        if char.isupper():
            x = (ord(char) - 65 + shift) % 26 + 65
        else:
            x = (ord(char) - 97 + shift) % 26 + 97
        cipher += chr(x)
        j += 1
    else:
        cipher += char  

print("Plain text is: " + text)
print("Key is: " + key)
print("Cipher text is: " + cipher)
