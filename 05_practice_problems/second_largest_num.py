nums = [10,5,20,8,15]
largest=nums[0]
result=[]
for i in range(len(nums)):
    if nums[i] > largest:
        largest=nums[i]
result.append(largest)
print(result[0])


