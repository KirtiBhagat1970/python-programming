nums=[0,1,0,3,12]
result=[]
count=0
for num in nums:
    if num != 0:
        result.append(num)
for num in nums:
    if num == 0:
        result.append(num)
    
print(result)