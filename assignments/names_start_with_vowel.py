vowel_set=('a','i','o','u','e')
count=0
with open("student.txt","r") as f:
    for line in f:
        name=line.strip().lower()
        if name and name[0] in vowel_set:
            count+=1
            print(f"found:{name}")
            
print(count)
            