units=int(input("enter units of electricity:"))
if units>0 and units<100:
    bill=units*5
elif units >101 and units<200:
    bill=units*7
elif units >200 :
    bill=units*10

print("total elctricity bill=","\u20B9",bill) 