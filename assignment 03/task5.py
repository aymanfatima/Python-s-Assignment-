print("Welcome to my first PYTHON BATCH-4 online class assignment # 3 calculator")
print("Press 1 for Addition")
print("Press 2 for Substraction")
print("Press 3 Multiplication")
print("Press 4 Division")

selection_is=int(input("Please select your operation you want to perform by entering number accordingly mentioned above: "))

if selection_is==1:
    num1=int(input("Enter Your First Number: "))
    num2=int(input("Enter Your Second Number: "))
    result=num1+num2
    print("Addition of two numbers is: ",result)
elif selection_is==2:
    num1=int(input("Enter Your First Number: "))
    num2=int(input("Enter Your Second Number: "))
    result=num1-num2
    print("Substraction of two numbers is: ",result)
elif  selection_is==3:
    num1=int(input("Enter Your First Number: "))
    num2=int(input("Enter Your Second Number: "))
    result=num1*num2
    print("Multiplication of two numbers is: ",result)
elif selection_is==4:
    num1=int(input("Enter Your First Number: "))
    num2=int(input("Enter Your Second Number: "))
    result=num1/num2
    print("Division of two numbers is: ",result)
else:
    print("Sorry You Entered invalid Number or Wrong input")