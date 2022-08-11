"""
Functions
"""
print("function - define")
def greeting():
    print("Welcome to python certification course")

print("Calling the function")
greeting()
greeting()

def evenOrOdd(number):
    if (number%2==0):
        print(number," is even")
    else:
        print(number, " is odd")

#evenOrOdd(10)

number = int(input("Enter a number"))
evenOrOdd(number)

def add(num1,num2):
    result = num1+num2
    return result

total = add(100,50)
print("total is ",total)