#use of *args
def my_fun(*args):
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args) 
    print("\n Argument Type is :", type(args))
my_fun("kirti",21,"bhor")