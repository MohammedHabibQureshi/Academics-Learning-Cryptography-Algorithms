

# AES Key Generation - Supports 128, 192, 256 bit keys
from Crypto.Cipher import AES

# --- Input Key (in hex) ---
key_hex = input("Enter AES key in hex (32/48/64 hex digits): ").strip()

# Validation of length
if len(key_hex) not in (32, 48, 64):
    print("❌ Key must be 128-bit (32 hex digits), 192-bit (48 hex digits), or 256-bit (64 hex digits)!")
    exit()

# Convert hex key to bytes
key = bytes.fromhex(key_hex)

# Decide rounds based on key length
if len(key) == 16:   # 128-bit
    rounds = 10
elif len(key) == 24: # 192-bit
    rounds = 12
elif len(key) == 32: # 256-bit
    rounds = 14
else:
    print("❌ Invalid key size!")
    exit()

# AES cipher object
cipher = AES.new(key, AES.MODE_ECB)

# Print key info
print(f"\nOriginal Key ({len(key)*8}-bit): {key_hex.upper()}")
print(f"Rounds: {rounds}")

# Print round keys
print("\n--- AES Round Keys ---")
for i, rk in enumerate(cipher._round_keys[:rounds+1]):  # round keys = rounds + 1
    print(f"Round Key {i}: {rk.hex().upper()}")







""" ### Other way to write AES Key Expansion
# AES Key Expansion - Manual Implementation
# Supports 128-bit (10 rounds), 192-bit (12 rounds), 256-bit (14 rounds)

# --- AES S-Box ---
SBOX = [
    # 0     1    2     3    4     5    6     7    8     9    A     B    C     D    E     F
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

# Round constants (Rcon)
RCON = [0x00,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]

# --- Helper Functions ---
def sub_word(word):
    return [SBOX[b] for b in word]

def rot_word(word):
    return word[1:] + word[:1]

def xor_words(a, b):
    return [i ^ j for i, j in zip(a, b)]

# --- AES Key Expansion ---
def key_expansion(key_bytes, rounds):
    Nk = len(key_bytes) // 4  # words in key
    Nb = 4  # words in block
    Nr = rounds

    w = []
    for i in range(Nk):
        w.append(list(key_bytes[4*i:4*(i+1)]))

    for i in range(Nk, Nb*(Nr+1)):
        temp = w[i-1]
        if i % Nk == 0:
            temp = xor_words(sub_word(rot_word(temp)), [RCON[i//Nk], 0, 0, 0])
        elif Nk > 6 and i % Nk == 4:
            temp = sub_word(temp)
        w.append(xor_words(w[i-Nk], temp))

    return w

# --- Main ---
key_hex = input("Enter AES key in hex (32/48/64 hex digits): ").strip()

if len(key_hex) not in (32, 48, 64):
    print("❌ Key must be 128-bit (32 hex), 192-bit (48 hex), or 256-bit (64 hex)!")
    exit()

key_bytes = bytes.fromhex(key_hex)

if len(key_bytes) == 16:
    rounds = 10
elif len(key_bytes) == 24:
    rounds = 12
elif len(key_bytes) == 32:
    rounds = 14
else:
    print("❌ Invalid key size")
    exit()

expanded = key_expansion(key_bytes, rounds)

print(f"\nOriginal Key ({len(key_bytes)*8}-bit): {key_hex.upper()}")
print(f"Rounds: {rounds}")
print("\n--- Round Keys ---")
for i in range(rounds+1):
    round_key = sum(expanded[4*i:4*(i+1)], [])
    print(f"Round {i}: {''.join(format(b,'02X') for b in round_key)}")
"""





""" ### pseudocode for AES Key Expansion
Input: Cipher Key (Nk words = 4, 6, or 8)   // Nk = number of 32-bit words
Output: Expanded Key Schedule (Nb*(Nr+1) words)

Step 1: Initialize parameters
    Nb = 4                               // Block size in words (always 4)
    If Nk = 4 → Nr = 10                  // AES-128 → 10 rounds
    If Nk = 6 → Nr = 12                  // AES-192 → 12 rounds
    If Nk = 8 → Nr = 14                  // AES-256 → 14 rounds

Step 2: Copy the initial key
    For i = 0 to Nk-1
        w[i] = CipherKey[i]              // First Nk words are the original key

Step 3: Generate remaining words
    For i = Nk to (Nb*(Nr+1) - 1)
        temp = w[i - 1]

        If (i mod Nk == 0)               // Every Nk-th word
            temp = RotWord(temp)         // Rotate left by 1 byte
            temp = SubWord(temp)         // Apply S-box to each byte
            temp = temp XOR Rcon[i/Nk]   // XOR with round constant

        Else if (Nk > 6 AND i mod Nk == 4)
            temp = SubWord(temp)         // Extra S-box step (only for AES-256)

        w[i] = w[i - Nk] XOR temp        // Generate new word

Step 4: Output the round keys
    Group w[] into (Nr+1) sets of 4 words each
    Each set = one round key


"""