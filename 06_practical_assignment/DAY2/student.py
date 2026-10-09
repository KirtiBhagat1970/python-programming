# create dictionary with student details
students={
    101:{"name":"rahul","scores":[20,20,25]},
    102:{"name":"aditi","scores":[40,50,90]},
    103:{"name":"priya","scores":[78,46,63]},
    104:{"name":"karan","scores":[60,70,39]}
}
#  calculate average score and flag pass/fail
for sid,details in students.items():
    avg=sum(details["scores"])/len(details["scores"])
    details["average"]=avg
    details["passed"]=avg >=30 #boolean flag

print("Students who passsed:")
for sid,details in students.items():
    if details["passed"]:
        print(details["name"])