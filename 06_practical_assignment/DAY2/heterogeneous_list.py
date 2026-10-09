#create list with heterogeneous elements
# print highest number in the list 
li=[1,"Ajay",2,3,5,"Seema","Anita"]
a=[]
for i in li:
    if type(i)==int:
        a.append(i)

a.sort()
highest=a[-1]
print(highest)