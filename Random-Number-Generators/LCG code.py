
x=int(input("Enter a number: "))
a=int(input("Enter a number for a: "))
b=int(input("Enter an number for b: "))
m=int(input("Enter a number for m: "))

for i in range(5):
    x= (a*x + b)%m
    print(x)