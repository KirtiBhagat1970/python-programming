with open("student.txt","r") as f:
    student=f.readlines()
    five_character=[]
    for name in student:
        if len(name)>5:
            five_character.append(name)
with open("filtered_name","w") as f:
    f.writelines(five_character)