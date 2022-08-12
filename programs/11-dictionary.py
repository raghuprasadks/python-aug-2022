"""
Dictionary
"""
bca2reg={100:"ravi",101:"rashmi",102:"Akash"}
print("bca2reg",bca2reg)
print("value associated with key 100 ",bca2reg[100])
bca2reg[100]="Ravi Kumar"
print("updated value ",bca2reg[100])
print("keys ",bca2reg.keys())
print("values ",bca2reg.values())
print("keys and values")
for k,v in bca2reg.items():
    print("key ",k,"value ",v)

bca2reg={100:"ravi",101:"rashmi",102:"Akash",101:"rashmi nagaraj"}
print(bca2reg)