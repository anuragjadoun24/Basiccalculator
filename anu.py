# DESIGN A SIMPLE CALCULATOR WITH BASIC ARITHMETIC OPERATION [TASK 1]
a=int(input("Enter your first number"))
operator=input("choose operator(+,-,*,/,%,**):")
b=int(input("Enter your second number"))
if operator=="+": 
    print(a + b)
elif operator=="-":
    print(a - b)
elif operator=="*":
     print(a * b) 
elif operator=="/":
    print(a / b)
elif operator=="%":
    print(a % b)      
elif operator=="**":
    print(a ** b)
else:
    print("This operation is invalid ")
    print("Choose from the given above operator")