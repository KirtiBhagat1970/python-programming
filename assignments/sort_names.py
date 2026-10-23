with open("student.txt","r") as f:
    student=f.read().splitlines()
sorted_names=sorted(student)
print(sorted_names)