"""
class and object
class - Calculator
add - method
"""
class Calculator():
    def add(self,num1,num2):
        return num1+num2
    def subtract(self,num1,num2):
        return num1-num2

mycalci = Calculator()
result = mycalci.add(100,150)
print("result of addition is ",result)
result = mycalci.subtract(200,150)
print("result of subtraction is ",result)
print("another object")
myfriendcalci = Calculator()
result = myfriendcalci.add(100,150)
print("result of addition is ",result)
result = myfriendcalci.subtract(200,150)
print("result of subtraction is ",result)
