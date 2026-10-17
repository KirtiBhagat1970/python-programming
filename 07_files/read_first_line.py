with open("sample.txt","w") as f:
    f.write("First line of text file\n")
    f.write("Second line of text file\n")
    f.write("Third line of text file\n")
with open("sample.txt","r") as f:
    first_line=f.readline()
    print(first_line.strip())
    