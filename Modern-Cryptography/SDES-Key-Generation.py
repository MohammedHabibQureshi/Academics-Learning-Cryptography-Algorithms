

# --- Input 10-bit Key ---
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

# --- Print Keys ---
print("Subkey K1:", "".join(map(str, K1)))
print("Subkey K2:", "".join(map(str, K2)))





"""
Algorithm SDES_Key_Generation
Input: 10-bit key (K)
Output: Two 8-bit subkeys (K1, K2)

Step 1: Apply P10 permutation on K
        P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        K = Permute(K, P10)

Step 2: Split K into two halves
        Left = first 5 bits
        Right = last 5 bits

Step 3: Perform circular left shift (LS-1) on both halves
        Left = LS1(Left)
        Right = LS1(Right)

Step 4: Combine Left and Right → 10 bits
        Apply P8 permutation to get subkey K1
        P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        K1 = Permute(Left||Right, P8)

Step 5: Perform circular left shift (LS-2) on both halves (from Step 3)
        Left = LS2(Left)
        Right = LS2(Right)

Step 6: Combine Left and Right → 10 bits
        Apply P8 permutation to get subkey K2
        K2 = Permute(Left||Right, P8)

Step 7: Return K1 and K2

"""
