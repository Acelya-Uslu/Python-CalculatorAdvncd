def Sum(a,b):
    return a+b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    return a/b
def  Subtraction(a,b):
    return a-b


print("Please select an operation:")
print("1=Sum")
print("2=Multiply")
print("3=Divide")
print("4=Subtraction")

chosen=input("Your operation:")
num1=int(input("First number"))
num2=int(input("Second number"))

if chosen == "1":
    print("Your result:",Sum(num1,num2))

elif chosen=="2":
    print("Your result:",Multiply(num1,num2))

elif chosen=="3":
    print("Your result:",Divide(num1,num2))

elif chosen=="4":
    print("Your result:",Subtraction(num1,num2))

else:
    print("Incorrect operation")