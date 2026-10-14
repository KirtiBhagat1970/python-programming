with open("data.txt","w") as f:
    f.write("hello world \n ") 
    f.write("Good afternoon \n" )
    f.write("My name is kirt\n" )
    f.write("Currently i am pursuing MCA \n")

with open("data.txt","r") as f:
    text=f.readlines()
    
print(f"Total number of lines:{len(text)}")

if len(text)>=2:
    print(f"2nd line:{text[1].strip()}")
else:
    print("Second line not available")

if len(text)>=4:
    print(f"4nd line:{text[3].strip()}")
else:
    print("fourth line not available")

    

