# at two numbers at third position of a list and
# append one name in the list and split it
li=[1,"Ajay",2,3,5,"Seema","Anita"]
a=[]
for i in li:
    if type(i)==int:
        a.append(i)

a.sort()
highest=a[-1]
print(highest)

