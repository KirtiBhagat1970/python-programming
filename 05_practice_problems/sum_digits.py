# num=int(input("enter a number:"))
# sum=0
# while num > 0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)


num=int(input("enter a number:"))
sum=0
n=num
while n >0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
if (num==sum):
    print("number is palindrome")
else:
    print("number is not palindrome")

