        #TuitoriaL-33 (Use of Strip method)
name=input("Enter your name: ")
some=input("Enter something: ")
print(f"{name}{some}")
print(f"{name.lstrip()}{some}")                     #Only Left side space wiLL be removed
print(f"{name.rstrip()}{some}")                    #Only Right side space wiLL be removed
print(f"{name.strip()}{some}")                     #aLL space wiLL be removed but not inside the string
print(name.replace(" ", "")+some)     #aLL space wiLL be removed

       #TuitoriaL-34 (      Use of Replace() method & find() method     )
#===>Use of replace() Method
details=input("Enter the text: ")
#bere=input("Enter the replace text: ")
#willre=input("Enter the text which will be: ")
#print(details.replace(f"{bere},{willre}",2))
print(details.replace("is","was",2))

#===>Use of find() Method
is_pos1=details.find("is")                           #Find the first position of "is"
is_pos2=details.find("is",is_pos1+1)        #Find the Second position of "is"
is_pos3=details.find("is",is_pos2+1)        #Find the Third position of "is"
print(f"First position of \"is\": {is_pos1}")
print(f"Second position of \"is\": {is_pos2}")
print(f"Third position of \"is\": {is_pos3}")



