def is_greater(num1,num2):
    if num1 > num2:
        print(f"\n{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"\n{num2} is greater than {num1}")
    else:
        print(f"{num1} = {num2} !")
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
is_greater(n1,n2)
