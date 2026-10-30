def  display(n):
    if n==0:
        return
    print(n,end=" ")
    display(n-1)
    print(n,end=" ")
display(3)
# in this question recursion function is used 
# recursion means stack is used
# 3 3!=0 print(3) display(3-1)=2 
# 2!=0 print(2)   display(2-1)=1
# 1!=0 print(2)   display(1-1)=0
# 0==0 print(n) means it print all numbers 1 2 3 in stack