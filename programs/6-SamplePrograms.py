"""
1. Write a program to check a given number
is even or odd. Use user input
"""
number = int(input("Enter a number"))
if (number%2==0):
    print(number," is even")
else:
    print(number," is odd")
"""
2. Calculate Simple interest by
accepting user inputs for principal,rateofinterest
and time
si=p*r*t/100
"""
print("simple interest calculation")
principal = int(input("Enter principal amount"))
roi = float(input("Enter rate of interest"))
time= int(input("Enter time in years"))
si=(principal*roi*time)/100
print("Interest is ",si)

"""
shopping
"""