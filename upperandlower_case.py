#Program to find the number of upper and lower case characters found in given string

upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'           # Initializing all the Upper case alphabets
lower_case = 'abcdefghijklmnopqrstuvwxyz'           # Initializing all the Lower case alphabets

x = input("Enter any string :")                     # Get the input from the input(It can be combination of upper and lower case alphabets)

up = 0                                              # Initializing variable up <- 0. up is incremented when it meets a Uppercase character in the input string
low = 0                                             # Initializing variable low <- 0. low is incremented when it meets a Lowercase character in the input string

for i in x:                                         # Using for loop to traverse through the string   
    if i in upper_case:                             # If condition to check wether it is a Uppercase character(you can also use lower case here)
        up+=1
    else:
        low +=1
        
print("Upper case :",up)
print("Lower case :",low)
