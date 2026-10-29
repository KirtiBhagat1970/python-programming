count=0
for i in range(1,4):
    for j in range(i):
        count+=1
print(count)

# output 6
# dryrun
# i=1 j=0,1 j runs 1 time count=1
# i=2 j=0,1,2 j runs 2 time count=3
# i=3 j=0,1,2,3 j runs 3 time count=6

