with open("demo.txt","w") as f:
    f.write("Welcome to the magical world of Python")

with open("demo.txt","r") as f:
    content=f.read()
    print(content)