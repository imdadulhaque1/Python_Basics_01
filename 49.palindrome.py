def is_palindrome(name):
    reversed_name = name[::-1]
    if name == reversed_name:
        #return True
        print("\nThis is Palindrome !")
    else:
        print("\nThis is NOT Palindrome !")
    #return False
n=input("Enter a String: ")
is_palindrome(n)


#---------------------> Another Perfect <---------------------#
print("\n\n#-----------------> Another Perfect <-----------------#\n\n")


def is_palindromee(nam):
    return nam == nam[::-1]

na=input("Enter a String: ")
print(is_palindromee(na))
