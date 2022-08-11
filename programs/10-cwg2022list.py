"""
Common wealth Games 2022
Dashboard
"""
cwg2022=[]
header=["Rank","Country","Gold","Silver","Bronze","Total"]
country1=[1,"Australia",67,57,54,178]
country2=[2,"England",57,66,53,176]
cwg2022.append(header)
cwg2022.append(country1)
cwg2022.append(country2)
print("CWC list")
print(cwg2022)

print("Display header with countries")
for i in cwg2022:
    print(i)

print("Display only country name")
for i in cwg2022:
    print(i[1])
print("Display only gold")
for i in cwg2022:
    print(i[2])
print("total of gold")
totalgold = 0
for i in range(len(cwg2022)):
    #print(i)
    if(i==0):
        continue
    totalgold = totalgold +cwg2022[i][2]
print("total gold won",totalgold)
print("Australia stat")

for i in cwg2022:
    if (i[1]=="Australia"):
        print(i)

