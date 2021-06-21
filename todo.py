# CREATE A TO-DO List app within Terminal
# This App will store all the items in an array and display it everytime we
# add an item to the list and delete an item from the list

# Application needs to allow the user to ADD an item to the list
# Application needs to allow the user to DELETE an item from the list
# Application needs to allow the user to print out the current to-do list
u_array = []
print("\n")
print("Welcome to ToDo! Please add to your list :)")
print("""
            *Commands*
    done / close = exit application
    print = print out your list
    remove = prompt list to remove an item
""")

while True:
    userin = input(">: ")
    if userin == 'done' or userin == 'close':
        exit()
    elif userin == 'print' or userin == 'Print':
        print("Here is your list", u_array)
    elif userin == 'remove' or userin == 'Remove':
        print("What would you like remove?")
        print(u_array)
        delete = input("rm*: ")
        try:
            u_array.remove(delete)
            print("*",delete, "has been removed *")
        except:
            print("Sorry, invalid input")
    try:
        u_array.append(userin)
        if userin == 'remove' or userin == 'Remove' or userin == 'print' or userin == 'Print':
            del u_array[-1]
    except:
        print("Sorry, invalid input.")



