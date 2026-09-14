a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))

if a==b == c:
    print("a ,b and c are equal numbers")
elif a==b :
    print("a and b are equal")
    print("largest number:", a if a > c else c)
elif a==c :
    print("a and c are equal")
    print("largest number:", a if a > b else b)
elif b==c :
    print("a and c are equal")
    print("largest number:", b if b > a else a)
else:
    if a >b and a > c:
        print("a is largest")
    elif b >a  and b > c:
            print("b is largest")
    else :
            print("c is largest")
    




