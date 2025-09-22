#Simple calculator python

print("select operestion ")
print("1 .Add")
print("2 .subtract")
print("3 .multipal")
print("4 .divide")

# user choice

choice = input("Enter choice(1/2/3/4):")

num1 = float(input("Enter frist number :"))
num2 = float(input("Enter second number:"))

if choice == "1":
    print("Result =",num1+num2)

elif choice =="2":
    print("Result =",num1-num2)

elif choice == "3":
    print("Result=",num1*num2)
    
elif choice =="4":
    if num2 !=0:
        
        print("Result=",num1/num2)
    else:
        print("Error! Division by zero not allowed.")
    
else:
    print("invild choice!")

