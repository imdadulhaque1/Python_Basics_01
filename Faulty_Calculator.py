#Fault ResuLt : 45 * 3==555 & 56 + 9==77 & 56 / 6==4 
while True:
    print("\n\n+ for addition")
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
            
            again = input("Do you want to calculate again 'Yes \ No' ? ")
            if again == 'Yes':
                continue
            else:
                break
        else:
            add = n1 + n2
            print(f"{n1} + {n2} = {add}")
            
            again = input("Do you want to calculate again 'Yes \ No' ? ")
            if again == 'Yes':
                continue
            else:
                break
    elif op=='-':
        n1 = int(input("Enter first Number: "))
        n2 = int(input("Enter second Number: "))
        sub = n1 - n2
        print(f"{n1} - {n2} = {sub}")
        
        again = input("Do you want to calculate again 'Yes \ No' ? ")
        if again == 'Yes':
            continue
        else:
            break

    elif op=='*':
        n1 = int(input("Enter first Number: "))
        n2 = int(input("Enter second Number: "))
        if n1==45 and n2==3:
            print(f"{n1} + {n2} = 555")
            
            again = input("Do you want to calculate again 'Yes \ No' ? ")
            if again == 'Yes':
                continue
            else:
                break
        else:
            multi = n1 * n2
            print(f"{n1} * {n2} = {multi}")
            
            again = input("Do you want to calculate again 'Yes \ No' ? ")
            if again == 'Yes':
                continue
            else:
                break

    elif op=='/':
        n1 = int(input("Enter first Number: "))
        n2 = int(input("Enter second Number: "))
        if n1==56 and n2==6:
            print(f"{n1} / {n2} = 4")
            
            again = input("Do you want to calculate again 'Yes \ No' ? ")
            if again == 'Yes':
                continue
            else:
                break
        else:
            div = n1 / n2
            print(f"{n1} / {n2} = {div}")
            
            again = input("Do you want to calculate again 'Yes \ No' ? ")
            if again == 'Yes':
                continue
            else:
                break

    elif op=='**':
        n1 = int(input("Enter first Number: "))
        n2 = int(input("Enter second Number: "))
        po = n1 ** n2
        print(f"{n1} ** {n2} = {po}")
        
        again = input("Do you want to calculate again 'Yes \ No' ? ")
        if again == 'Yes':
            continue
        else:
            break

    elif op=='%':
        n1 = int(input("Enter first Number: "))
        n2 = int(input("Enter second Number: "))
        po = n1 % n2
        print(f"{n1} % {n2} = {po}")
        
        again = input("Do you want to calculate again 'Yes \ No' ? ")
        if again == 'Yes':
            continue
        else:
            break
