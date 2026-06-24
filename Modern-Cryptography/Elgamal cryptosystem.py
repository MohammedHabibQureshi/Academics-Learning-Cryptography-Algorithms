

p=int(input("Enter a large prime number (p): "))
g=int(input("Enter a primitive root of p (g): "))
x=int(input("Enter a private key (x): "))
m=int(input("Enter a message: "))
k=int(input("Enter a number (k): "))

h=(g**x) % p      # pow(g,x)%p
print("Shared public key :(",h,",",g,",",p,")")

# Encryption
c1=(g**k) % p       # pow(g,k)%p
c2=(m*(h**k))%p       #  (m*pow(h,k))%p
print("Ciphertext : (",c1,",",c2,")")

#Decryption
s_inv=0
s =(c1**x)%p          #  pow(c1,x)%p
for i in range(1,p):
    if (s*i)%p==1:
        s_inv=i
        break

M=(c2*s_inv)%p
print("Decrypted message :",s_inv,",",M)




"""
# ElGamal Cryptosystem

p = int(input("Enter a large prime number (p): "))
g = int(input("Enter a primitive root of p (g): "))
x = int(input("Enter a private key (x): "))
m = int(input("Enter a message (m): "))
k = int(input("Enter a random number (k): "))

# Public key generation
h = pow(g, x, p)
print("Public key : (", h, ",", g, ",", p, ")")

# Encryption
c1 = pow(g, k, p)
c2 = (m * pow(h, k, p)) % p
print("Ciphertext : (", c1, ",", c2, ")")

# Decryption
s = pow(c1, x, p)
s_inv = pow(s, -1, p)   # Modular inverse
M = (c2 * s_inv) % p
print("Decrypted message :", M)
"""