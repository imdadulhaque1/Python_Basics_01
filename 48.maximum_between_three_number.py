def is_greater(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"\n{num1} is greater than {num2} & {num3}")
        
    elif num1 < num2 and num2 > num3: 
            print(f"\n{num2} is greater than {num1} & {num3}") 
            
    else:
        print(f"\n{num3} is greater than {num1} & {num2}") 
        
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the second number: "))
is_greater(n1,n2,n3)

#---------------------> Another Perfect coding with max()method <---------------------#
print("\n\n#-----------------> Another Perfect coding with max()method <-----------------#\n\n")

def greatest(num11,num22,num33):
    bigger = max(num11 , num22)
    biggest = max(bigger , num33)
    print(f"\n{biggest} is Greater than both numbers !")

n11 = int(input("Enter the first number: "))
n22 = int(input("Enter the second number: "))
n33 = int(input("Enter the second number: "))
greatest(n11,n22,n33)
