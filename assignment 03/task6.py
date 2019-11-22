
test_string = input("Enter sentence with number: ")
print("The original string : " + test_string) 
res = [int(i) for i in test_string.split() if i.isdigit()] 
print("The numbers list is : " + str(res))