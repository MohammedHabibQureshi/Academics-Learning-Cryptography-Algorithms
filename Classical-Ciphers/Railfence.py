
# Rail Fence Cipher Encryption
text = input("Enter the plaintext: ").replace(" ", "").upper()
rails = int(input("Enter number of rails: "))

# Create a list for each rail
fence = [""] * rails
row = 0
direction = 1  # 1 = down, -1 = up

for char in text:
    fence[row] += char
    # Change direction if top or bottom is reached
    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1
    row += direction

# Combine rails to get cipher
cipher = "".join(fence)

print("Cipher Text:", cipher)





# Rail Fence Cipher Decryption
cipher = input("Enter the cipher text: ").replace(" ", "").upper()
rails = int(input("Enter number of rails: "))

# Step 1: Mark zig-zag positions
fence = [["\n"] * len(cipher) for _ in range(rails)]
row, direction = 0, 1

for i in range(len(cipher)):
    fence[row][i] = "*"
    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1
    row += direction

# Step 2: Fill with cipher text
index = 0
for r in range(rails):
    for c in range(len(cipher)):
        if fence[r][c] == "*" and index < len(cipher):
            fence[r][c] = cipher[index]
            index += 1

# Step 3: Read zig-zag to get plaintext
result = []
row, direction = 0, 1
for i in range(len(cipher)):
    result.append(fence[row][i])
    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1
    row += direction

plain = "".join(result)
print("Decrypted Text:", plain)
