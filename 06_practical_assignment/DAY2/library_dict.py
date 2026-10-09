#create dictionary for library display if book is available or not
library={
    "The Great Gastsby":True,
    "shamchi aai":False,
    "Mrutyunjay":True,
    "Chhava":False,
    "Yugandhar":True
    
}

#function to display status of books
def display_library_status(books):
    print("Library book Status")
    for title,is_available in books.items():
        status="Available " if is_available else "Not Availble (Checked Out)"
        print(f".{title},{status}")
        
display_library_status(library)
    
