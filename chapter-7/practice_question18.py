#create a program using global keyword to modify a variable froma function
name="kaushik"#global variable
print("originalstring",name)
def hello(name):
    name="shubham"
    print("after modify",name)
hello(name)