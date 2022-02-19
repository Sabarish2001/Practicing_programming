# Program to mutate the character in the specified position

def mutate(string,position,character):                    # Function mutate will change or mutate the character in the specified position 
    convert_me = list(string)
    convert_me[position] = character
    con_me_back = ''.join(convert_me)
    return con_me_back
    

    
s = input("Enter any string :")                          # Get the input string from the user
pos = int(input("Enter the position :"))                 # Get the input position from the user at which the character has to be mutated
char = input("Enter the character :")                    # Get the input character from the user to be placed at the specified position 

res = mutate(s,pos,char)                                 # Call the function mutate and pass the parameters (String,Position,Character)
print(res)
