
import math

"""   def gcd(i,phi):
        while phi:
           i, phi = phi, i % phi
        return i     """


msg = int(input("Enter a message (as an integer): "))
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
n = p * q             
phi = (p - 1) * (q - 1)  

e = []             # e=0
for i in range(2, phi):
    if math.gcd(i,phi)==1:
        if 1 < i < phi:
            e.append(i)      # e = i  break
            
e=e[0]            
d = 0
for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break

print("Public Key:", (e, n))
print("Private Key:", (d, n))
print()

c = (msg ** e) % n   # c= pow(msg,e)%n

m = (c ** d) % n    # m= pow(c,d)%n

print("Original Message =", msg)
print("Encrypted Message =", c)
print("Decrypted Message =", m)
