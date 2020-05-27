#Get data from user and store it in a list
#Then display the most recent three entries nicely

#Set up an empty list...

all_calculations = []

#Get five items of data

get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")
    
    if get_item == "xxx":
        break
    
    all_calculations.append(get_item)

print()

if len(all_calculations) == 0:
    print("Oops - the list is empty")
    
else:
    
    #Show that everything made it to the list...
    print("*** The full list ***")
    print(all_calculations)
    
    #Print items starting at the END of the list
    
    if len (all_calculations) >= 3:
        print("*** Most recent 3 ***")
        for item in range(0,3):
            print(all_calculations[len(all_calculations) - item - 1])
        
        else:
            print("*** Items from Newest to Oldest ***")
            for item in all_calculations:
                print(all_calculations[len(all_calculations) - all_calculations.index(item)])
            