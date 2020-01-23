n=int(input("Enter an Integer Number: "))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a, b)
else:
    print(a, b, end=" ")
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(b, end=" ")

#---------------------> Another Perfect coding using function <---------------------#
print("\n\n#-----------------> Another Perfect coding using function <-----------------#\n\n")

def febonacci_series(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a, b, end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b, end=" ")
num=int(input("Enter an integer number: "))
febonacci_series(num)
