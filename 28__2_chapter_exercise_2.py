user_name=input("Enter the User Name: ")
print(f"{user_name}"[-1: :-1])                       #Reverse name
 
        #TuitoriaL-31 chapter-02 exercise-03
user,ch=input("Enter the two input by using seperated comma: ").split(",")
print("User name Length: ",len(user))
#print(f"Count the character: {user.count(ch)}")                              #acts as case sensitive
print(f"Count the character: {user.lower().count(ch.lower())}")     #acts as case Insensitive
#user=user.lower()
#count(ch)=count(ch.lower())

        #TuitoriaL-33 (Use of Strip method)
name=input("Enter your name: ")
some=input("Enter something: ")
print(f"{name}{some}")
print(f"{name.lstrip()}{some}")                     #Only Left side space wiLL be removed
print(f"{name.rstrip()}{some}")                    #Only Right side space wiLL be removed
print(f"{name.strip()}{some}")                     #aLL space wiLL be removed but not inside the string
print(f"{name.replace(" ","")} {some}")     #aLL space wiLL be removed
