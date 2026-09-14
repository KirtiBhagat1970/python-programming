pin=2005
balance=100000
userpin=int(input("enter your pin:"))
if pin==userpin:
    print('''1.Check Balance
    2.Deposit
    3.Withdraw
    4.Exit''')
    choice=int(input("enter your choice:"))
    match choice:
        case 1:
            print("Balance:",balance)
        case 2:
            deposit=int(input("enter amount to deposit:"))
            balance=balance+deposit
            print("Balance:",balance)
        case 3:
            withdraw=int(input("enter amount to deposit:"))
            if balance>=withdraw:
                balance=balance-withdraw
                print("Balance:",balance)
            else:
                print("insufficient balannce ")
        case 4:
            print("Exit")
            
