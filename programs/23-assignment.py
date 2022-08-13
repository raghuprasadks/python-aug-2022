"""
1. Write a program to print the prime numbers
between given two numbers. You can use the user
input to get the two numbers
Enter the starting range 10
Enter the ending range 20
11,13,17,19
"""
startrange = int(input("enter starting range"))
endrange = int(input("enter ending range"))
for i in range(startrange,(endrange+1)):
    for num in range(2,i):
        if (i%num ==0):
            #print(i, "is not a prime")
            break
    else:
        print(i, "is  prime")
