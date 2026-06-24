

# One-Time Pad Cipher - Encryption
text = input("Enter the plain text: ").upper()
key = input("Enter the key (same length as text): ").upper()

cipher = ""

for t, k in zip(text, key):
    if t.isalpha():
        x = ((ord(t) - 65) + (ord(k) - 65)) % 26 # XOR operation
        cipher += chr(x + 65)
    else:
        cipher += t

print("Plain Text :", text)
print("Key        :", key)
print("Cipher Text:", cipher)







# One-Time Pad Cipher - Decryption

cipher = input("Enter the cipher text: ").upper()
key = input("Enter the key (same length as text): ").upper()

plain = ""

for c, k in zip(cipher, key):
    if c.isalpha():
        x = ((ord(c) - 65) - (ord(k) - 65)) % 26  # XOR again
        plain += chr(x + 65)
    else:
        plain += c

print("Cipher Text:", cipher)
print("Key        :", key)
print("Plain Text :", plain)
