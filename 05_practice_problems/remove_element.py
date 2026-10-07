nums=[3,2,2,3]
target=3
new_list=[]
for num in nums:
        if num == target:
              nums.remove(num)
new_list.append(nums)
print(new_list)