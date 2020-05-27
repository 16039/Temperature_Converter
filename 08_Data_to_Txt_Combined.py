#Checks if file is valid

import re

#Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a filename: ")
    has_error ="no"
    
    valid_char = "[A-Za-z0-9_]" #These are all valid expressions A-Z, a-z, 0-9, _
    for letter in filename:
        if re.match(valid_char, letter):
            continue
        
        elif letter == " ":
            problem = "(no spaces allowed)"
        else:
            problem = ("(no {}'s allowed)".format(letter))
        
        has_errror = "yes"
        
        
    if filename == "":
        problem = "can't be blank"
        has_error = "yes"
    
    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
        
    else:
        print("You have entered a valid filename.")

#Everything is good....

#Add .txt to suffix!
filename = filename + ".txt"

#Create file to hold data
f = open(filename, "w+")

#Add new line at end of each item
for item in data:
    f.write(item + "\n")

#Close file
f.close()

        