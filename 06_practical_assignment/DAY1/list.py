# Empty list
my_list=[]
print(my_list)

# with items
fruits=["apple","strawberry","banana","jackfruit","watermelon"]
print(fruits)

#  to access any element use index
# positive number indexs from start negative number indexs from last
# 0 is first index -1 is last index

numbers=[10,20,30,40,50]
print(numbers[3])
print(numbers[-1])

#append item in list
colors=["red","pink","blue","green"]
colors.append("black")
print(colors)


#insert at specific location
colors.insert(1,"purple")
print(colors)

#functions
#length
number=[1,2,3,4,5,6,7,8,9]
print("length of number:",len(number))

#sum
print("sum of all list numbers:",sum(number))

#sorting
print("list in ascending order:",sorted(number))
print("list in descening order:",sorted(number))


# create a list of 10 numbers and display the sum of four elements
num=[10,20,30,40,50,60,88,99,26,56]
sum_of_num=sum(num[-4:])
print(sum_of_num)

#remove elments from the list located at second and fifth position
print("remove element at fifth position:",num.pop(2))
print("remove element at fifth position:",num.pop(5))

#print the difference between highest and smallest number from the list
highest=max(num)
smallest=min(num)
difference=highest-smallest
print(difference)

#append a element in the list which is half of the item located third position in list
num.append(num[2]/2)
print(num)