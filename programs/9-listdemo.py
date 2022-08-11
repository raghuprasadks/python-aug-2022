"""
List demo
"""
print("list demo -create- append")
marks=[]
marks.append(20)
marks.append(18)
marks.append(21)
marks.append(23)
marks.append(15)
"""
check for other built-in functions
https://www.w3schools.com/python/python_lists_methods.asp
"""
print("marks list ",marks)
print("list demo -get 0th element value")
print(marks[0])
print("list demo -update 0th element value")
marks[0]=22
print(marks[0])
print("list demo -delete 0th element ")
del marks[0]
print("updated marks list ",marks)
print("looping")
for i in marks:
    print(i)
print("built-in functions")
print("maximum ",max(marks))
print("minimum ",min(marks))
print("sum ",sum(marks))
length =len(marks)
avg = sum(marks)/length
print("Average ",avg)
print("list marks >20")

for i in marks:
    if(i>20):
        print(i)
marks.sort()
print("sorting in ascending order ",marks)
marks.sort(reverse=True)
print("sorting in descending order ",marks)
