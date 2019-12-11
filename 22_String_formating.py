name,age,ID=input("Enter your name: "), float(input("Enter your age: ")), int(input("Enter your ID: "))
print("\n-----------NormaL format of String------(Worst Syntax)-----")                              #Worst Syntax
print("Name is: "+name+"\nAge is: "+str(age)+"\nID Number is: "+str(ID))

print("\n-----------Python-03 format of String------(Good Syntax)-----")                              #Good Syntax--Python-03
print("Name is: {}.\nAge is: {} .\nID Number is: {}.".format(name, age, ID))

print("\n-----------Python-3.6 format of String------(Best Syntax)-----")                              #Best Syntax--Python-3.6
print(f"Name is: {name}.\nAge is: {age} .\nID Number is: {ID}.")
