drinks = ["Pepsi", "Cherry Coke Zero", "Sprite"]
crisps = ["Doritos", "Walkers"]
sweets = ["Snickers", "M&Ms", "Skittles"]

while True:
    choice = input("Would you like a DRINK, some CRISPS or some SWEETS?\n> ").lower()

    try:
        if choice == 'drink':
            snack = drinks.pop()
        elif choice == 'crisps':
            snack = crisps.pop()
        elif choice == 'sweets':
            snack = sweets.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print("We're all out of {}! Sorry".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))

