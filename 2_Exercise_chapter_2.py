
num1,num2,num3=int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))
add=num1+num2+num3
avg=add/3
print("---------String formating of Python-03---------")
print("Average Number is: {}".format(avg));

 print("\n---------String formating of Python-3.6---------")
print(f"Average Number is: {avg}")

print("\n---------String formating of Python-3.6---(with Split)---------")
n1,n2,n3=input("Enter three number: ").split(",")
#add1=n1+n2+n3;
#avg1=add1/3
print(f"Average number is: {(int(n1)+int(n2)+int(n3))/3}")
