with open("count_characters.txt","r") as f:
    content=f.read()
    char_count=len(content)
    print(f"Total characters:{char_count}")
    
