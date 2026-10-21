lines=["line1:python\n",
       "line2:java\n",
       "line3:DSA\n",
       "line4:ADBMS"]
with open("demo1.txt","w") as f:
    f.writelines(lines)
with open("demo1.txt","r") as f:
    f.seek(5)
    line=f.readline()
    print(line)