
            #Counting the Character into the String
temp_var=""
name=input("Enter a String: ")
for i in range(0,len(name)):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
