marks=int(input("Enter your marks: "))
if marks>=80 and marks<=100:
    print("A+")
elif marks>=70 and marks<=79:
    print("A")
elif marks>=60 and marks<=69:
    print("A-")
elif marks>=50 and marks<=59:
    print("B")
elif marks>=40 and marks<=49:
    print("C")
elif marks>=33 and marks<=39:
    print("D")
elif marks<33:
    print("FaiL")
else:
    print("Out of range")

