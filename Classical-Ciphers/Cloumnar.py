

# Columnar Transposition Cipher - Encryption
plain = input("Enter the plain text: ").replace(" ", "").upper()
key = input("Enter the key: ").upper()

# Step 1: Sort the key to get column order
order = sorted(list(key))
cipher = ""

# Step 2: Arrange plaintext in rows
rows = (len(plain) + len(key) - 1) // len(key)  # ceiling division
matrix = [['X'] * len(key) for _ in range(rows)]  # fill with 'X'

k = 0
for r in range(rows):
    for c in range(len(key)):
        if k < len(plain):
            matrix[r][c] = plain[k]
            k += 1

# Step 3: Read columns in sorted key order
for ch in order:
    col = key.index(ch)
    for r in range(rows):
        cipher += matrix[r][col]

print("Cipher Text:", cipher)







# Columnar Transposition Cipher - Decryption
cipher = input("Enter the cipher text: ").upper()
key = input("Enter the key: ").upper()

cols = len(key)
rows = (len(cipher) + cols - 1) // cols   # number of rows

# Step 1: Sort the key to know column order
order = sorted(list(key))

# Step 2: Create empty matrix
matrix = [[''] * cols for _ in range(rows)]

# Step 3: Fill columns based on sorted key order
k = 0
for ch in order:
    col = key.index(ch)
    for r in range(rows):
        if k < len(cipher):
            matrix[r][col] = cipher[k]
            k += 1

# Step 4: Read row-wise to get plaintext
plain = ""
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] != '':  
            plain += matrix[r][c]

print("Decrypted Plain Text:", plain)


