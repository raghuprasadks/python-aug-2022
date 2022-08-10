"""
While loop
"""
print(" 1's table 1 to 10 ")
print(1)
print(2)
print(3)
print("Above one with out a loop")
start =1
end = 10
# : indentation
while(start <=end):
    print(start)
    start = start +1
    #start +=1 - assignment operator

"""
for loop
range - number generator
"""
print("1's table using for loop and range 0 to 9")
for i in range (10):
    print(i)
print(" 1's table using for loop 1 to 10 ")
for i in range(1,11):
    print(i)
print(" 2's table using for loop 2 to 20 ")
for i in range(2,21,2):
    print(i)
print(" 2's table using for loop in reverse order 20 to 2 ")
for i in range(20,1,-2):
    print(i)
