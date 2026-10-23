with open("student.txt","r") as f:
    student=f.readlines()
    for name in student:
        if len(name)>5:
            print(name)