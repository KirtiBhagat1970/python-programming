score =int(input("enter a score:"))
if 100 > score > 90:
    print("grade A ")
elif score > 80:
    print("grade B ")
elif score > 65:
    print("grade C ")
elif score > 35 :
    print("grade C ")
elif score <35 and score >0:
    print("Fail")
else:
    print("invalid marks")
