print("Calculator")

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

oper =input("Enter the operation +,-,*,/")
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
result=0
if(oper=="+"):
    result=add(num1,num2)
elif (oper=="-"):
    result = subtract(num1, num2)
elif (oper=="*"):
    result = multiply(num1, num2)
elif (oper=="/"):
    result = divide(num1, num2)
else:
    result="Invalid Operator"

print("result of ",num1,oper,num2,' = ',result)



