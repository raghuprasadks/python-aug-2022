"""
markssheet dictionary
"""
marksdict={100:["ranga",20,23,18],
           101:["ravi",22,17,21],
           102:["rashmi",24,18,23]
           }
print("marksdict ",marksdict)
print("Total marks of every student")

for k,v in marksdict.items():
    print("key ",k," value ",v)
    name = v[0]
    total = v[1]+v[2]+v[3]

    """
    for m in v:
        name=v[0]
        total = v[1]+v[2]+v[3]
    """
    print(name,total)