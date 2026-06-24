
## Ceaser cipher Encryption
text = input("Enter the plain text: ")
key = int(input("Enter the key: "))
cipher = ""
for char in text:
    asscii = ord(char)
    if char.isupper():
        x = (asscii + key - 65) % 26 + 65
    else:
        x = (asscii + key - 97) % 26 + 97
    cipher += chr(x)
print("Plain text is: " + text)
print("Cipher text is: " + cipher)






## Ceaser cipher Decryption
cipher = input("Enter the cipher text: ")   
key = int(input("Enter the key: "))
plain = ""
for char in cipher:
    asscii = ord(char)
    if char.isupper():
        x = (asscii - key - 65) % 26 + 65
    else:
        x = (asscii - key - 97) % 26 + 97
    plain += chr(x)
print("Plain text is: " + plain)
