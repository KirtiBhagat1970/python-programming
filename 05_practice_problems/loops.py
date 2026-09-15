correct_pass="some_pass"
not_found=True
while not_found:
    string=input("enterr a string:")
    if string == correct_pass:
        not_found =False
    else:
        print("wrong password try again")
    print("password matchded!")

