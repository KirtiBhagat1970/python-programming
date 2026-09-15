num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
choice=('''1.add 2.sub 3.mul 4.div 5.factorial 6.exit''')
match choice:
    case 1:
        print("result:",num1+num2)
    case 2:
        print("result:",num1-num2)
    case 3:
        print("result:",num1*num2)
    case 4:
            print("result:",num1/num2)
    case 5:
            print("result:",num1+num2)
    case 'exit':
            print("exit")
    case _:
            print("invalid choice")