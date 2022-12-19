# Justin Burkhalter

print("You have just become a Christian and need to get to the eternal life but satan stands in your way. You need to defeat satan before getting eternal salvation, but before you will need to put on the full armor of God. You will need the breastplate of righteousness to protect you from every spiritual attack, shield of faith to put your personal trust in God, the helmet of salvation to protect your mind, the sword of the Spirit to bring truth and freedom to you, the belt of truth to put your trust in God’s truth, and finally the gospel of peace sandals to take the message of God’s peace to the people around you.")

# Function showing the goal of the game and move commands


def show_instructions():
    # print a main menu and the commands
    # Add later type 'exit' to exit
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


# A dictionary for the eternal life text game
# The dictionary links a room to other rooms.
rooms = {
    "Jerusalem": {'South': 'Cenacle', 'item': 'Sword of the Spirit', 'North': 'Golgotha', 'item': 'Helmet of Salvation', 'West': 'Rome', 'item': 'Shield of Faith', 'East': 'Praetorium', 'item': "Breastplate of Righteousness"},
    'Cenacle': {'North': 'Jerusalem', 'East': 'Nazareth', 'item': 'Gospel of Peace Sandals'},
    'Nazareth': {'West': 'Cenacle', 'item': 'Sword of the Spirit'},
    'Rome': {'East': 'Jerusalem', },
    'Golgotha': {'East': 'Gethsemane', 'item': 'Belt of Truth', 'South': 'Jerusalem'},
    'Gethsemane': {'West': 'Golgotha', 'item': 'Helmet of Salvation'},
    'Praetorium': {'West': 'Jerusalem', 'North': 'Eternal Life', 'item': 'satan'},
    'Eternal Life': {'South': 'Praetorium', 'item': 'Breastplate of Righteousness'}
    # add more rooms and directions here
}


# Show the players status by identifying the room they are currently in
# showing a list of their inventory of items, and displaying the item in their current room.
def show_status(inventory, current_room):
    print("Inventory", inventory)
    print("You are in the", current_room)
    item = rooms[current_room].get('item')
    if item not in inventory:
        print("You see the", item)


def main():
    directions = ('go South', 'go North', 'go East', 'go West')
    inventory = []  # list to add the items
    current_room = "Jerusalem"  # starting room
    show_instructions()  # print main game instructions

    while True:  # unless user enters Exit, the loop will run

        # show instructions and status
        show_status(inventory, current_room)

        # reads user input like go South etc
        user_input = input("\nEnter your move: ")
        if user_input.lower() == 'exit':
            print("Thanks for playing")
            break  # exit

        # breaks the user input to remove word 'go'
        user_input = user_input.strip().split(' ', 1)
        if len(user_input) > 1:  # If statement that checks the length of x
            action = user_input[0]
            object = user_input[1]
        else:
            print("Invalid input")
            continue

        valid_objects = rooms[current_room].keys()
        if action == 'go':
            dir = object.capitalize()
            if dir in valid_objects:  # if the given room has this direction, continue
                # change the start_room after moving
                current_room = rooms[current_room][dir]
                print("You enter the", current_room)

            else:
                # if direction is not present for current_room in rooms dictionary,
                print('Invalid direction!')

        elif action == 'get':
            item = rooms[current_room].get('item')
            if item not in inventory:
                inventory.append(item)  # add the item to the inventory
                # remove it from the current room
                rooms[current_room][item] = None
            else:
                print("You already have the", item)
        else:
            print("Invalid input")

        if current_room == '':
            if len(inventory) == 6:
                print("win")
            else:
                print("lose")
            break  # if you win/lose, then you dont want to ask for input again at the start of the loop


main()  # go!
