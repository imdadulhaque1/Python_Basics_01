#Query: Ask user input a number containing more than one digit
        #Example: 1234 or 5678
        #Calculate: 1+2+3+4 or 5+6+7+8

s=input("Enter a string more the one digit: ")
i=0
total=0
while i<len(s):             #len(s) --> finding the length
    total+=int(s[i])        #int(s[i]) --> converting integer
    i+=1
print(total)
