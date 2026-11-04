# combining regular arguments with args and kwargs 
def my_function(title, *args, **kwargs):
    print(title)
    print("CR is ",args[0], "\nLR is ",args[1])
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    #my_function("Div B Info", "Vaibhav", "Sonal", age = 25, city = "Pune")
my_function("Div A Info","Chintamani","Bhavya", age = 24, city = "Pune")