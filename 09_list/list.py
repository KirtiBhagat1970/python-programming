li=[1,2,4,8,10,22,56,47,19]
filtered_list=[x for x in li if x%3==0]      
print("Numbers divisible by 3:",filtered_list)

for num in range(1,10):
    if num==4:
        print("encountered 4,skipping using continue.")
        continue 
    if num==8:
        print("encountered 8,skipping using continue.")
        break 
    print(f"current number:{num}")
        