a =int(input("First Value:"))
b =int(input("Second Value:"))
while a!=b:
    if a>b:
        a-=b
    else: b-=a
print("GCD is:",a)