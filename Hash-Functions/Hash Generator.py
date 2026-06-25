

# Step 1: Take message
msg = input("Enter a message: ")

# Step 2: Convert characters to ASCII and process
hash_val = 0
for ch in msg:
    # Add ASCII value, multiply, and take modulo to keep it small
    hash_val = (hash_val * 31 + ord(ch)) % 1000  

# Step 3: Print final hash
print("Message:", msg)
print("Hash Value:", hash_val)
