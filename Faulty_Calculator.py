
#Fault ResuLt : 45 * 3==555 & 56 + 9==77 & 56 / 6==4
print("Fault ResuLt : 45 * 3==555 & 56 + 9==77 & 56 / 6==4")

print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
print("** for power")
print("% for modulus")

op = input("\nEnter your choice: ")
if op =='+':
    n1 = int(input("\nEnter first Number: "))
    n2 = int(input("Enter second Number: "))
    if n1==56 and n2==9:
        print(f"{n1} + {n2} = 77")
    else:
        add = n1 + n2
        print(f"{n1} + {n2} = {add}")
elif op=='-':
    n1 = int(input("Enter first Number: "))
    n2 = int(input("Enter second Number: "))
    sub = n1 - n2
    print(f"{n1} - {n2} = {sub}")
    
elif op=='*':
    n1 = int(input("Enter first Number: "))
    n2 = int(input("Enter second Number: "))
    if n1==45 and n2==3:
        print(f"{n1} + {n2} = 555")
    else:
        multi = n1 * n2
        print(f"{n1} * {n2} = {multi}")

elif op=='/':
    n1 = int(input("Enter first Number: "))
    n2 = int(input("Enter second Number: "))
    if n1==56 and n2==6:
        print(f"{n1} / {n2} = 4")
    else:
        div = n1 / n2
        print(f"{n1} / {n2} = {div}")
    
elif op=='**':
    n1 = int(input("Enter first Number: "))
    n2 = int(input("Enter second Number: "))
    po = n1 ** n2
    print(f"{n1} ** {n2} = {po}")

elif op=='%':
    n1 = int(input("Enter first Number: "))
    n2 = int(input("Enter second Number: "))
    po = n1 % n2
    print(f"{n1} % {n2} = {po}")
