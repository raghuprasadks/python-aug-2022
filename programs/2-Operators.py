"""
Operators - Arithmetic,Comparision,logical operator
"""

# Arithmetic operators - +,-,*,/,//,%,**
print("Arithmetic operators")
num1=100
num2=200
result = num1 + num2
print(" + ",result)
print(num1 , " + " , num2," = ",result)
num3=9
num4=2
print(" / ",num3/num4)
print(" // ",num3//num4)
print(" % - remainder",num3%num4)
print(" **-exponent ",2**3)
# Comparision or Relational operators - >,<,>=,<=,==,!=
num1=100
num2=200
print("Comparison operators")
result = num1>num2
print(" num1>num2 ",result)
result = num1==num2
print(" num1==num2 ",result)
result = num1!=num2
print(" num1!=num2 ",result)
# Logical operators and,or,not
num1=100
num2=200
num3=75
result = (num2>num1) and (num1>num3)
print("(num2>num1) and (num1>num3) ",result)
result = (num1>num2) or (num1>num3)
print("(num1>num2) or (num1>num3) ",result)
result = not ((num1>num2) or (num1>num3))
print("not ((num1>num2) or (num1>num3)) ",result)






