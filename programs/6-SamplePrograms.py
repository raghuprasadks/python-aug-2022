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
3-shopping - finding discount

Following advertisement is placed in a news paper
by a eshoppe
purchase <=10000 discount 10 %
purchase >10000 <= 20000 discount 20 %
purchase >20000 <= 30000 discount 30 %
purchase >30000 discount is 35 %
a. Get the user input for the purchaseamount
b. Display the net amount to pay
c. Display discount
purchase_amt = 10000
discount = purchase_amt*10/100
discount = 1000
netamount = purchase_amt-discount
"""
print("Welcome to eshoppe")
purchase_amt=int(input("Enter purchase amount"))
net_amt=0
discount=0
discountrate=0
if (purchase_amt<=10000):
    discountrate=10
elif (purchase_amt>10000 and purchase_amt<=20000):
    discountrate = 20
elif (purchase_amt>20000 and purchase_amt<=30000):
    discountrate = 30
else:
    discountrate = 35
discount =purchase_amt*(discountrate)/100
net_amt=purchase_amt-discount
print("Your purchase amount is ",purchase_amt)
print("discount is ",discount)
print("you have to pay ",net_amt)
"""
4- Electricity bill payment
Find the electricity bill amount based on 
following condition
Ask the end user to enter units cosumed
units<=100 rate/unit = 1 RS
units >100 <=200 rate/unit = 2 RS
units >200 <=300 rate/unit = 3 RS
units >300 rate/unit = 5 RS
Calculation is cumulative
Sample calculation
units = 50
amount = units*rate = 50 *1=50
units = 150
100*1+(150-100)*2=200
units = 250
100*1+(100*2)+50 *3=450
"""




