from room import Room
from player import Player
import time
from item import Item
from os import system, name

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = str(input('Hello, what is your name?   '))
player = Player(player_name, room['outside'])
clear()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
potato = Item('potato', 'put it in a stew')
cheese = Item('cheese', 'its cheese')
room['outside'].inventory.append(potato)
room['foyer'].inventory.append(cheese)
print(room['outside'].inventory[0].name)
print(room['foyer'].inventory[0].name)

playing = True
print(f'\nWelcome {player.name}\n')
time.sleep(1)
clear()
while playing:   
    print(player)
    selection = input(f'    What would you like to do {player.name}.  ')
    selection = selection.split()
    if len(selection) == 1:
        if selection[0] == 'n': 
            if player.room.n_to != 'The way is blocked.':
                player.room = player.room.n_to
                clear()
                print(f'You move into the {player.room.name}')
                time.sleep(1)
            else:
                clear()
                print(player.room.n_to)
                time.sleep(1)
                clear()
                print('Try a different direction.')
                time.sleep(1)
        elif selection[0] == 'e':
            if player.room.e_to != 'The way is blocked.':
                player.room = player.room.e_to
                clear()
                print(f'You move into the {player.room.name}')
                time.sleep(1)
            else:
                clear()
                print(player.room.e_to)
                time.sleep(1)
                clear()
                print('Try a different direction.')
                time.sleep(1)
        elif selection[0] == 's':
            if player.room.s_to != 'The way is blocked.':
                player.room = player.room.s_to
                clear()
                print(f'You move into the {player.room.name}')
                time.sleep(1)
            else:
                clear()
                print(player.room.s_to)
                time.sleep(1)
                clear()
                print('Try a different direction.')
                time.sleep(1)
        elif selection[0] == 'w':
            if player.room.w_to != 'The way is blocked.':
                player.room = player.room.w_to
                clear()
                print(f'You move into the {player.room.name}')
                time.sleep(1)
            else:
                clear()
                print(player.room.w_to)
                time.sleep(1)
                clear()
                print('Try a different direction.')
                time.sleep(1)
        elif selection[0] == 'i' or selection[0] == 'inventory':
            clear()
            if len(player.inventory) != 0:
                print(f'\n You are currently holding:')
                for i, p in enumerate(player.inventory):
                    print(f'    {i + 1}: {p.name} - {p.description}\n')
                input('Press enter to continue.')
            else:
                print('Inventory currently empty')
                input('Press enter to continue')
        elif selection[0] == 'q':
            clear()
            print(f'\nThanks for playing, {player.name}!\n')
            playing = False
        else:
            clear()
            print(f'\n {player.name}! You must be confused, please enter a valid action.\n')
            time.sleep(1)
    else:
        if selection[0] == 'get' or selection[0] == 'take':
            if len(player.room.inventory) == 0:
                    clear()
                    print('There is nothing here')
                    time.sleep(1)
            else:
                for each in player.room.inventory:
                    if each.name == selection[1]:
                        player.add_item(each)
                        player.room.remove_item(each)
                        clear()
                        each.on_take()
                    else:
                        clear()
                        print(f'Unable to find {selection[1]}')
                        time.sleep(1)
        elif selection[0] == 'drop':
            if len(player.inventory) == 0:
                    clear()
                    print('You aren\'t holding anything.')
                    time.sleep(1)
            else:
                for each in player.inventory:
                    if each.name == selection[1]:
                        player.remove_item(each)
                        player.room.add_item(each)
                        clear()
                        each.on_drop()
                    else:
                        clear()
                        print(f'You don\'t have {selection[1]}')
                        time.sleep(1)
        else:
            clear()
            print(f'\n {player.name}! You must be confused, please enter a valid action.\n')
            time.sleep(1)
    time.sleep(.5)
    clear()