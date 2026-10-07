# nums=[1,2,3,4,5]
# nums.reverse()
# print(nums)

nums=[1,2,3,4,5]
result=[]
for i in range(len(nums)-1,-1,-1):
    result.append(nums[i])
print(result)
