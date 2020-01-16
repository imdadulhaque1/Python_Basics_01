name=input("Enter a String: ")
temp_var=""
i=0
while i < len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]}: {name.count(name[i])}")
    i=i+1

#I=name.count('I')          #Easiest Way without loop 
#print(f"I : {I}")

#a=name.count('a')
#print(f"a : {a}")

#d=name.count('d')
#print(f"d : {d}")

#e=name.count('e')
#print(f"e : {e}")

#H=name.count('H')
#print(f"H : {H}")

#m=name.count('m')
#print(f"m : {m}")

#l=name.count('l')
#print(f"l : {l}")

#u=name.count('u')
#print(f"u : {u}")

#sp=name.count(' ')
#print(f"  : {sp}")

#q=name.count('q')
#print(f"q : {q}")
