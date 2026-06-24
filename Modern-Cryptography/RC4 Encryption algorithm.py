
import numpy as np


pt=np.array(input("Enter the plain text: "))
key=np.array(input("Enter the key: "))
s=np.array([0,1,2,3,4,5,6,7])
t=np.array([key[i] for i in range(len(key))])
cipher=[]

j=0
for i in range(s):
    j= (j+s[i]+t[i])%8
    s[i],s[j]=s[j],s[i]
    print(s)
print("Updated state vector:", s)

j=0
for i in range(len(pt)):
    j= (j+s[i+1])%8
    s[i],s[j]=s[j],s[i]
    print(s)
    t=(s[i]+s[j])%8
    k=s[t] 
    print("Key:", k)
    cipher.append(k)
    print("Cipher text at a time:", cipher)
print(" Cipher text:", cipher)

for i in range(len(pt)):
    cipher[i] ^= pt[i] 
    print("Cipher text at a time:", cipher)
print("Final cipher text:", cipher)