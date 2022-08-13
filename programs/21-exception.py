"""
Exception management
"""
"""
print("Exception scenario 1 - division by zero")
num = int(input("enter a number"))
result = 100/num
print(result)
"""
"""
print("Exception scenario 2 - unsupported operand type(s)")
num = input("enter a number")
result = 100/num
print(result)
"""
"""
print("Exception scenario 3 - list index out of range")

marks = [20,39,49,55]
print(marks[4])
"""
"""
print("Exception scenario 1 - division by zero - error handling")
num = int(input("enter a number"))
try:
    result = 100/num
    print(result)
#except:
except Exception as e:
    print("Error has occured",e)
print("After error")
"""
"""
try:
    #a=10/0
    a=10/'raghu'
    print(a)
#except ArithmeticError,NameError: - 3.6 does not support
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except Exception as e:
    print("Generic Error",e)
else:
    print("Successfully Done")
"""
#Finally Block

try:
    a=10/0;
    a=10/2;
    print(a)
except ZeroDivisionError:
    print(ZeroDivisionError)
finally:
    print("Finally block is always called")
