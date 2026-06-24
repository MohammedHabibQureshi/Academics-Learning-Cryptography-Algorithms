
  ### Playfair cipher Encryption
import numpy as np
# --- Input ---
text = input("Enter the plain text: ").upper().replace("J", "I")
key = input("Enter the key: ").upper().replace("J", "I")

# --- Build Key Matrix ---
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
km = []
for c in key+alphabet:
    if c not in km:
        km.append(c)
matrix = np.array(km).reshape(5,5)
print("\nKey Matrix:\n", matrix)

# --- Prepare Plaintext ---
pt = ""
i = 0
while i < len(text):
    a = text[i]
    if i+1 < len(text):
        b = text[i+1]
        if a == b:
            pt += a + "X"
            i += 1
        else:
            pt += a + b
            i += 2
    else:
        pt += a + "X"
        i += 1
print("Prepared Text:", pt)

# --- Encrypt ---
cipher = ""
for i in range(0, len(pt), 2):
    a, b = pt[i], pt[i+1]
    r1,c1 = np.where(matrix==a)
    r2,c2 = np.where(matrix==b)
    r1,c1,r2,c2 = r1[0], c1[0], r2[0], c2[0] 
    if r1==r2:  # same row
        cipher += matrix[r1,(c1+1)%5] + matrix[r2,(c2+1)%5]
    elif c1==c2:  # same column
        cipher += matrix[(r1+1)%5,c1] + matrix[(r2+1)%5,c2]
    else:  # rectangle
        cipher += matrix[r1,c2] + matrix[r2,c1]

print("Cipher Text:", cipher)




### Playfair cipher Decryption
import numpy as np

# --- Input ---
text = input("Enter the plain text: ").upper().replace("J", "I")
key = input("Enter the key: ").upper().replace("J", "I")

# --- Build Key Matrix ---
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
km = []
for c in key+alphabet:
    if c not in km:
        km.append(c)
matrix = np.array(km).reshape(5,5)
print("\nKey Matrix:\n", matrix)

# --- Prepare ciphertext ---
ct = ""
i = 0
while i < len(text):
    a = text[i]
    if i+1 < len(text):
        b = text[i+1]
        if a == b:
            ct += a + "X"
            i += 1
        else:
            ct += a + b
            i += 2
    else:
        ct += a + "X"
        i += 1
print("Prepared Text:", ct)

# --- Decrypt ---
plain = ""
for i in range(0, len(ct), 2):
    a, b = ct[i], ct[i+1]
    r1,c1 = np.where(matrix==a)
    r2,c2 = np.where(matrix==b)
    r1,c1,r2,c2 = r1[0], c1[0], r2[0], c2[0] 
    if r1==r2:  # same row
      plain += matrix[r1,(c1-1)%5] + matrix[r2,(c2-1)%5]
    elif c1==c2:  # same column
      plain += matrix[(r1-1)%5,c1] + matrix[(r2-1)%5,c2]
    else:  # rectangle (same as encryption)
      plain += matrix[r1,c2] + matrix[r2,c1]


print("Cipher Text:", plain)



"""
# --- Input ---
text = input("Enter the plain text: ").upper().replace("J", "I")
key = input("Enter the key: ").upper().replace("J", "I")

# --- Build Key Matrix ---
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
km = []
for c in key + alphabet:
    if c not in km:
        km.append(c)

# Create 5x5 matrix as list of lists
matrix = [km[i:i+5] for i in range(0, 25, 5)]

print("\nKey Matrix:")
for row in matrix:
    print(row)

# --- Prepare Plaintext ---
pt = ""
i = 0
while i < len(text):
    a = text[i]
    if i + 1 < len(text):
        b = text[i+1]
        if a == b:
            pt += a + "X"
            i += 1
        else:
            pt += a + b
            i += 2
    else:
        pt += a + "X"
        i += 1

print("Prepared Text:", pt)

# --- Encrypt ---
cipher = ""
for i in range(0, len(pt), 2):
    a, b = pt[i], pt[i+1]

    # Find positions of a and b
    r1 = c1 = r2 = c2 = -1
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == a:
                r1, c1 = r, c
            if matrix[r][c] == b:
                r2, c2 = r, c

    # Apply Playfair rules
    if r1 == r2:  # same row
        cipher += matrix[r1][(c1+1) % 5] + matrix[r2][(c2+1) % 5]
    elif c1 == c2:  # same column
        cipher += matrix[(r1+1) % 5][c1] + matrix[(r2+1) % 5][c2]
    else:  # rectangle
        cipher += matrix[r1][c2] + matrix[r2][c1]

print("Cipher Text:", cipher)
"""
