"""
markssheet dictionary
"""
marksdict={100:["ranga",20,23,18],
           101:["ravi",22,17,21],
           102:["rashmi",24,18,23]
           }
print("marksdict ",marksdict)
print("Total marks of every student")
toppermarks=0
topper=""
for k,v in marksdict.items():
    print("key ",k," value ",v)
    name = v[0]
    total = v[1]+v[2]+v[3]
    print(name,total)
    if (total>toppermarks):
        toppermarks=total
        topper=name

print("topper ",topper, "topper marks ",toppermarks)
"""
Display - topper
subjectwise topper
"""
lst=[20,30,40,50]
lst1 =lst[1:3]
print("lst 1",lst1)