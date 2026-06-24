

# --- Input ---
plaintext = input("Enter 8-bit plaintext: ")  # e.g., 10101010
key = input("Enter a 10-bit key: ")

if len(key) != 10 or not set(key).issubset({"0","1"}):
    print("❌ Key must be 10 bits of 0s and 1s!")
    exit()
key = [int(b) for b in key]

# --- Input P10 and P8 ---
P10 = list(map(int, input("Enter P10 permutation (10 numbers): ").split()))
P8  = list(map(int, input("Enter P8 permutation (8 numbers): ").split()))

# --- Apply P10 ---
key_p10 = [key[i-1] for i in P10]

# --- Split into two halves ---
left = key_p10[:5]
right = key_p10[5:]

# --- LS-1 (shift left by 1) ---
left = left[1:] + left[:1]
right = right[1:] + right[:1]

# --- Apply P8 for K1 ---
K1 = [ (left + right)[i-1] for i in P8 ]

# --- LS-2 (shift left by 2 more = total 3 from original) ---
left = left[2:] + left[:2]
right = right[2:] + right[:2]

# --- Apply P8 for K2 ---
K2 = [ (left + right)[i-1] for i in P8 ]

print("K1:", "".join(map(str, K1)))
print("K2:", "".join(map(str, K2)))

# --- Input IP, EP, P4 ---
IP = list(map(int, input("Enter Initial Permutation: ").split()))
EP = list(map(int, input("Enter Expansion Permutation: ").split()))
P4 = list(map(int, input("Enter P4 permutation: ").split()))

# --- S-Boxes ---
print("\n--- Enter S-Boxes ---")
print("S0 (4 rows, space separated values for each row):")
S0 = [list(map(int, input().split())) for _ in range(4)]

print("S1 (4 rows, space separated values for each row):")
S1 = [list(map(int, input().split())) for _ in range(4)]

# --- Helper to permute bits ---
def permute(bits, table):
    return "".join(str(bits[i-1]) for i in table)

# --- Step 1: Initial Permutation ---
ip = permute(plaintext, IP)
L, R = ip[:4], ip[4:]

# --- Round Function ---
for round_key in [K1, K2]:
    # Expansion Permutation
    expanded = permute(R, EP)

    # XOR with round key
    xor_out = "".join(str(int(expanded[i]) ^ round_key[i]) for i in range(8))

    # S-box substitution
    left4, right4 = xor_out[:4], xor_out[4:]

    # S0 lookup
    row = int(left4[0] + left4[3], 2)
    col = int(left4[1] + left4[2], 2)
    s0_val = format(S0[row][col], "02b")

    # S1 lookup
    row = int(right4[0] + right4[3], 2)
    col = int(right4[1] + right4[2], 2)
    s1_val = format(S1[row][col], "02b")

    # Combine & P4 permutation
    s_output = s0_val + s1_val
    p4_out = permute(s_output, P4)

    # XOR with Left half
    L = "".join(str(int(L[i]) ^ int(p4_out[i])) for i in range(4))

    # Swap after first round
    if round_key == K1:
        L, R = R, L

# --- Combine halves ---
pre_output = L + R

# --- Final Permutation (inverse of IP) ---
IP_inv = [IP.index(i)+1 for i in range(1, 9)]
cipher = permute(pre_output, IP_inv)

# --- Output ---
print("\nPlaintext :", plaintext)
print("Ciphertext:", cipher)





"""  ## Other way write SDES algorithm
# --- Input ---
plaintext = input("Enter 8-bit plaintext: ")
key10 = input("Enter 10-bit key: ")

# --- Step 1: P10 ---
p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
key = "".join(key10[i-1] for i in p10)

# Split into left and right
left, right = key[:5], key[5:]

# --- Step 2: LS-1 ---
left = left[1:] + left[0]
right = right[1:] + right[0]

# --- Step 3: P8 -> K1 ---
p8 = [6, 3, 7, 4, 8, 5, 10, 9]
K1 = "".join((left + right)[i-1] for i in p8)

# --- Step 4: LS-2 ---
left = left[2:] + left[:2]
right = right[2:] + right[:2]

# --- Step 5: P8 -> K2 ---
K2 = "".join((left + right)[i-1] for i in p8)

print("K1:", K1)
print("K2:", K2)

# --- Step 6: Initial Permutation (IP) ---
ip = [2,6,3,1,4,8,5,7]
bits = "".join(plaintext[i-1] for i in ip)

# Split
L, R = bits[:4], bits[4:]

# --- Step 7: Round 1 (Fk with K1) ---
# Expansion/Permutation (EP)
ep = [4,1,2,3,2,3,4,1]
R_exp = "".join(R[i-1] for i in ep)

# XOR with K1
xor_out = format(int(R_exp,2) ^ int(K1,2), "08b")

# S-box S0
S0 = [[1,0,3,2],
      [3,2,1,0],
      [0,2,1,3],
      [3,1,3,2]]

row = int(xor_out[0] + xor_out[3], 2)
col = int(xor_out[1] + xor_out[2], 2)
s0_val = format(S0[row][col], "02b")

# S-box S1
S1 = [[0,1,2,3],
      [2,0,1,3],
      [3,0,1,0],
      [2,1,0,3]]

row = int(xor_out[4] + xor_out[7], 2)
col = int(xor_out[5] + xor_out[6], 2)
s1_val = format(S1[row][col], "02b")

# P4
p4 = [2,4,3,1]
p4_out = "".join((s0_val+s1_val)[i-1] for i in p4)

# XOR with L
L = format(int(L,2) ^ int(p4_out,2), "04b")

# Combine
bits = L + R

# --- Step 8: Swap halves ---
bits = bits[4:] + bits[:4]

# --- Step 9: Round 2 (Fk with K2) ---
L, R = bits[:4], bits[4:]
R_exp = "".join(R[i-1] for i in ep)
xor_out = format(int(R_exp,2) ^ int(K2,2), "08b")

# S0 again
row = int(xor_out[0] + xor_out[3], 2)
col = int(xor_out[1] + xor_out[2], 2)
s0_val = format(S0[row][col], "02b")

# S1 again
row = int(xor_out[4] + xor_out[7], 2)
col = int(xor_out[5] + xor_out[6], 2)
s1_val = format(S1[row][col], "02b")

# P4
p4_out = "".join((s0_val+s1_val)[i-1] for i in p4)

# XOR with L
L = format(int(L,2) ^ int(p4_out,2), "04b")

# Combine
bits = L + R

# --- Step 10: Inverse IP ---
ip_inv = [4,1,3,5,7,2,8,6]
ciphertext = "".join(bits[i-1] for i in ip_inv)

print("Ciphertext:", ciphertext)

"""






"""  ### pseudocode for SDES
1. Key Generation (K1, K2)
Input: 10-bit key

1. Apply permutation P10 to the key → result = 10-bit permuted key
2. Split into two halves: Left (5 bits), Right (5 bits)
3. Perform circular left shift (LS-1) on both halves
4. Combine halves and apply P8 permutation → K1 (8-bit subkey)
5. Perform circular left shift (LS-2) on both halves (from step 2)
6. Combine halves and apply P8 permutation → K2 (8-bit subkey)

Output: Subkeys K1, K2

2. Encryption
Input: 8-bit plaintext, K1, K2
fv 
1. Apply Initial Permutation (IP) on plaintext
2. Split into L (left 4 bits) and R (right 4 bits)

--- Round 1 ---
3. Expand R (4 bits) → 8 bits using Expansion/Permutation (EP)
4. XOR result with K1
5. Divide into two halves (4 bits each)
6. Pass left 4 bits into S-box S0, right 4 bits into S-box S1
   → Output = 4 bits
7. Apply permutation P4 on result
8. XOR with left half L
9. Swap halves (L ↔ R)

--- Round 2 ---
10. Repeat steps 3–7 using K2
11. Do NOT swap after this round

12. Combine L and R
13. Apply Inverse Initial Permutation (IP⁻¹)

Output: 8-bit ciphertext

3. Decryption
Input: 8-bit ciphertext, K1, K2

1. Same as encryption, but use subkeys in reverse order:
   - Round 1 uses K2
   - Round 2 uses K1
"""
