nums=[8,3,12,10,9]
smallest=nums[0]
for i in range(len(nums)):
    if nums[i] < smallest:
        smallest=nums[i]
print(smallest)

# dryrun
# i =8 3 12 10 9
#    0 1 2  3  4

# smallest=8

# 8 < 3 False
# 3 < 8 true   smallest=3
# 12 < 3 False
# 10 < 3 False
# 9 < 3 false