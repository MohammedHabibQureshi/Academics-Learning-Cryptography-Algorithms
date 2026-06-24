
## Diffie-hellman Key Exchange Algorithm
p=int(input("Enter a large prime number (p): "))
g=int(input("Enter a primitive root of p (g): "))
a=int(input("Enter a private key for user A (a): "))
b=int(input("Enter a private key for user B (b): "))

A = (g**a) % p      # pow(g,a)%p
B = (g**b) % p      # pow(g,b)%p

ka = (B**a) % p     # pow(B,a)%p
kb = (A**b) % p     # pow(A,b)%p

print("Secret key for user A:", ka)
print("Secret key for user B:", kb)
