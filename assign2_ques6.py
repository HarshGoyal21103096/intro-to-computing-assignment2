#QUESTION6
a=float(input("ENTER FIRST SIDE OF TRIANGLE="))
b=float(input("ENTER SECOND SIDE OF TRIANGLE="))
c=float(input("ENTER THIRD SIDE OF TRIANGLE="))
if(a>=(b+c)):
    print("No")
elif(b>=(a+c)):
    print("No")
elif(c>=(a+b)):
    print("No")
else:
    print("Yes")
