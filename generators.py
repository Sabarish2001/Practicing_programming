# Program using Generators to create a list and assign values to list 

def create_string(x):
    for i in range(x):
        name = input("Enter names :")
        yield name
        
stringlist = []
for x in create_string(10):
    stringlist.append(x)
print(stringlist)
