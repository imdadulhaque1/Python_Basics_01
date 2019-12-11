#---------------String Indexing-----------------------
print("---------------String Indexing-----------------------")
name="ImdaduL Haque Imdad"
print(f"String Indexing: {name[4]}")
print(f"String Indexing: {name[6]}")

#---------------String slicing/ Sub Sequence-----------------------
print("\n---------------String slicing/ Sub Sequence----------------------- ")
#Syntax:    [Strat argument : Stop argument]
n1=int(input("Enter the Start argument: "))
n2=int(input("Enter the Stop argument: "))
#print(f"String Slicing: {name[0: 3]}")
print(f"String Slicing: {name[n1 : n2]}")

#------another example of String slicing/ Sub Sequence---------- 
s=input("\nEnter the Statement: ")
start=int(input("Enter the Start argument: "))
stop=int(input("Enter the Stop argument: "))

print(f"{s}"[start:stop])

#-------String slicing / Sub Sequence(with sate argument)----------
print("\n-------String slicing / Sub Sequence(with sate argument)----------")
#Syntax:    [Start argument : Stop argument : state]
state=int(input("Enter the State argument: "))
print(f"{s}"[start : stop: state])
print(f"{s}"[start : : state])
print(f"{s}"[ : stop: state])
print("I am in Love with you."[10 : 1: -1])           #result will be Reversed
