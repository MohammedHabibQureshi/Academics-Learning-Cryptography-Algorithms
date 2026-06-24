p=int(input("Enter a number for p: "))
q=int(input("Enter a number for q: "))
x=int(input("Enter a number: "))
m=p*q
print("m =", p * q )

for i in range(5):
    x=(x*x) % m
    b= x% 2
    print(x, b)