

### Hill cipher Encryption
import numpy as np

# --- Input ---
plain = input("Enter the plaintext: ").upper().replace(" ", "")
key_ele = input("Enter numbers for key matrix (space-separated): ").split()
n = int(len(key_ele) ** 0.5)   # matrix size = sqrt of key length

# --- Check if valid ---
if n * n != len(key_ele):
    print("❌ Invalid key length! Must be a perfect square (4, 9, 16, ...)")
    exit()

# --- Build key matrix ---
key = np.array(list(map(int, key_ele))).reshape(n, n)
print("Key Matrix:\n", key)

# --- Pad Plaintext ---
while len(plain) % n != 0:
    plain += "X"

# --- Encryption ---
cipher = ""
for i in range(0, len(plain), n):
    block = [ord(ch) - 65 for ch in plain[i:i+n]]
    block_vec = np.array(block).reshape(n, 1)
    c = np.dot(key, block_vec) % 26
    cipher += "".join(chr(val[0] + 65) for val in c)

print("Plaintext:", plain)
print("Ciphertext:", cipher)






### Hill cipher Decryption
import numpy as np

# --- Modular inverse function ---
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# --- Input ---
cipher = input("Enter the ciphertext: ").upper().replace(" ", "")
key_elements = input("Enter numbers for key matrix (space-separated): ").split()
n = int(len(key_elements) ** 0.5)

# --- Check if valid ---
if n * n != len(key_elements):
    print("❌ Invalid key length! Must be a perfect square (4, 9, 16, ...)")
    exit()

# --- Build key matrix ---
key = np.array(list(map(int, key_elements))).reshape(n, n)
print("Key Matrix:\n", key)

# --- Find determinant ---
det = int(round(np.linalg.det(key))) % 26
det_inv = mod_inverse(det, 26)

if det_inv is None:
    print("❌ Key matrix is not invertible under mod 26!")
    exit()

# --- Find adjoint matrix ---
key_inv = (det_inv * np.round(det * np.linalg.inv(key)).astype(int)) % 26
print("Inverse Key Matrix (mod 26):\n", key_inv)

# --- Decryption ---
plain = ""
for i in range(0, len(cipher), n):
    block = [ord(ch) - 65 for ch in cipher[i:i+n]]
    block_vec = np.array(block).reshape(n, 1)
    p = np.dot(key_inv, block_vec) % 26
    plain += "".join(chr(val[0] + 65) for val in p)

print("Ciphertext:", cipher)
print("Decrypted Plaintext:", plain)

