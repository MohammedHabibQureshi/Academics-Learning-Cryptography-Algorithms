
import hashlib

# Step 1: Take input message
msg = input("Enter a message: ")

# Step 2: Apply MD5
md5_hash = hashlib.md5(msg.encode()).hexdigest()

# Step 3: Apply SHA-512
sha512_hash = hashlib.sha512(msg.encode()).hexdigest()

# Step 4: Print results
print("Message:", msg)
print("MD5 Hash:    ", md5_hash)
print("SHA-512 Hash:", sha512_hash)
