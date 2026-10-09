#Accept the name and check if its palindrome
name=input("enter a string:")
palindrome=name[::-1]
if name==palindrome:
    print(palindrome,"is a palindrome")
else:
    print(palindrome,"is  not a palindrome")