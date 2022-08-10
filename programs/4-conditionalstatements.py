"""
conditional statements
"""
print("if else")
age = 19
if (age>=18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")
print("if elif else")
"""
marks >90 <=100 - A+
marks >80 <=90 - A
marks >70 <=80 - B+
"""
marks = 80
if (marks >90 and marks <=100):
    print("A+")
elif (marks >80 and marks <=90):
    print("A")
elif (marks >70 and marks <=80):
    print("B+")
else:
    print("less than B+")
