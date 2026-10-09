# print pattern in triangle with * and #
n=int(input("enter a number:"))
for i in range(1,n):
    for j in range(1,i+1):
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
    print()