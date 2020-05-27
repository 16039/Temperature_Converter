#Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

#Get filename, can't be blank/invalid
#Assume valid data for now

filename = input("Enter  a Filename (leave off the extension): ")

#Add .txt to suffix!
filename = filename + ".txt"

#Create file to hold data
f = open(filename, "w+")

#Add new line at end of each item
for item in data:
    f.write(item + "\n")

#Close file
f.close()