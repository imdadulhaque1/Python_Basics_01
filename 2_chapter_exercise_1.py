n1=int(input("enter  the   first   number: "))
n2=int(input("enter the second number: "))
n3=int(input("enter  the  third  number: "))
avg=(n1+n2+n3)/3
print("---------------String formatting---------------")
print("Average : {}".format(avg))                           #the rules of "pyhton 3"
print(f"Average: {avg}")                                          #the rules of "pyhton 3.6"

print("----------------Use of \"Split\"----------------")
num1,num2,num3=input("Enter three numbers: ").split(",")
#avg1=(int(num1)+int(num2)+int(num3))/3
print(f"Average: {(int(num1)+int(num2)+int(num3))/3}")        #the rules of "pyhton 3.6"

#From tuitoriaL-25(String Indexing)
print("--------From tuitoriaL-25\(String Indexing\)-------------")
name="ImdaduL Haque Imdad"
print(name[4])
print(name[6])
