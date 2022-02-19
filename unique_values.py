# Program to return a list containing unique values

def unique_fun(l):        # Unique function will return you the unique values given a list of numbers
    x = []                # Creating a empty list x which will store the unique values from the given list of numbers
    for i in l:           # Using for loop to iterate my list of numbers
        if i not in x:    # Using if condition to check wether i is already present in list x
            x.append(i)   # If i not present in x then add i to list x and if already present it is not added to list x
    return x              # Return statement to return the list x

print(unique_fun([1,1,2,3,4,4,4,5,6,6,7]))
