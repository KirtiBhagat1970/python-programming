#string functions
text="welcome to IMCC"

#1 strips spaces from both ends
print("Remove spaces:",text.strip())

#2 convert to lower case
print("lower case:",text.lower())

#3 convert to upper case
print("Upper case:",text.upper())

#4 Capitilize first letter
print("Capitilize first letter:",text.capitalize())

#5 Title case(Capitilize each word)
print(text.title)

#6 count occurances of substring
print("letter c occurences:",text.count('c'),"times in text")

#7 find position of substring(-1 if not found)
print("position of IMCC in text is  ",text.find("IMCC"))

#8 replace a string
print("replace a substring:",text.replace("IMCC","Python Magic!"))

#9 check if string starts or ends with certain substring
print(text.startswith("We"))
print(text.startswith("!"))

#10 split string into list by a delimeter
print("Simple split:",text.split())

#11 join a list of strings with a separator
words=["python","is","fun"]
print(".join(words)")


#12 count the vowels
text="hello world"
count=0
set_vowel="aioueAIOUE"
for char in text:
    if char in set_vowel:
        count+=1
        
print(count)

#13 print string multiple times
txt="ha"
print(txt*3)
    
#14 name find the occurences of letter i in your name
name="kirti bhagat"
print("letter of occus",name.count('i'),"times in name")

#15 replace name with a
print(name.replace('i','a'))

#16 split your name into two parts
print(name.split())

#17 sorting
print(sorted(name))

