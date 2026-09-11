num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
choice=input("enter your choice:")
match choice:
    case "add":
        print("addition:",num1+num2) 
    case "sub":
            print("substraction:",num1-num2) 
    case "mult":
            print("multiplcation:",num1*num2)
    case "div":
            if(num2!=0):
                  print("division:",num1/num2)  
            else:
                  print("number cannot divide by zero")
    case _:
            print("invalid choice") 