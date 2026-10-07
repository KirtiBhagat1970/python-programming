#print sum of first 10 even numbers
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum=0
for num in numbers:
    if num%2==0:
        sum=sum+num
 
print(sum)

# reverse the accepted string
str=input("enter a number:")
reverse=str[::-1]
print(reverse)
        