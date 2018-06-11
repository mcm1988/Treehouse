import os
shopping_list = []


def add_to_list(item):
    show_list()
    if shopping_list:
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(item)
    show_list()


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")

    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        print("Couldn't find {} in your list.".format(what_to_remove))
        pass
    show_list()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'LIST' to show your list.
    Enter 'REMOVE' to delete an item from your list
    """)


def show_list():
    clear_screen()
    print("Here's your list:")
    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))
    print("-"*10)


show_help()


while True:
    new_item = input("> ")

    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'LIST':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
        continue
    add_to_list(new_item)


show_list()