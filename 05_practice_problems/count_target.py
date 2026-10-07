nums=[2,5,2,8,2,9]
target=2
count=0
for i in range(len(nums)):
    if nums[i]==target:
        count+=1
print(count)