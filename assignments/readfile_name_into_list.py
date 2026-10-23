with open("student.txt","r") as f:
    list=[]
    student=f.readlines()
    for name in student:
        clean_name=name.strip()
        list.append(clean_name)
    print(list)