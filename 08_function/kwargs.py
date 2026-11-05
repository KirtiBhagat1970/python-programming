#using **kwrgs 
def new_fun(**myvar):
    print("Argument Type is :", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
new_fun(name = "Kirti", age = 21, city = "Bhor")