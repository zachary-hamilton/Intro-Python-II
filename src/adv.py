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
'''
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


playing = True
print(f'\nWelcome {player.name}\n')
time.sleep(1)
clear()
while playing:   
    print(player)
    selection = input('    Please select a direction to move.  ')

    if selection == 'n': 
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
    elif selection == 'e':
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
    elif selection == 's':
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
    elif selection == 'w':
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
    elif selection == 'q':
        clear()
        print(f'\nThanks for playing, {player.name}!\n')
        playing = False
    else:
        clear()
        print(f'\n {player.name}! You must be confused, try again\n')
        time.sleep(1)
    
    time.sleep(.5)
    clear()

potato = Item('potato', 'put it in a stew')
blanket = Item('blanket', 'warm')


player.add_item(potato)
player.add_item(blanket)
print(player)
'''
def new_player():
    player_name = str(input('Hello, what is your name?   '))
    player = Player(player_name, room['outside'])
    clear()
    return player

def welcome_message():
    print(f'\nWelcome {player.name}\n')
    time.sleep(1)
    clear()

def main_menu():
    print(f'You are currently in the {player.room.name}')
    print('-------------')
    print(f'{player.room.description}')
    print('-------------')
    print('You have the following options?')
    print('    1: Inspect my location')
    print('    2: Move on')
    print('    3: View my inventory')
    print('    4: Quit')
    choice = input('What would you like to do?    ')
    return choice

def inspect(player):
    if len(player.room.inventory) != 0:
        print(f'You are able to find:')
        for i, p in enumerate(player.room.inventory):
            print(f'    {i + 1}: {p.name} - {p.description}')
        item_to_add = player.room.inventory[int(input('Do you want to add any of these items?    ')) - 1]
        player.room.remove_item(item_to_add)
        player.add_item(item_to_add)
        clear()
        print(f'You have added the {item_to_add.name}')
    else:
        print('There\'s nothing here')
    return 

def move(player):
    print('move tbd')
    return 

def view_inventory(player):
    if len(player.inventory) != 0:
        print(f'You are currently holding:')
        for i, p in enumerate(player.inventory):
            print(f'    {i + 1}: {p.name} - {p.description}')
        print('    Press any other key to go back')
        item_choice = input('Do you want to drop any of these items?    ')
        if (int(item_choice) - 1) >= 0 and (int(item_choice) - 1) < len(player.inventory):
            item_to_drop = player.inventory[int(item_choice) - 1]
            player.remove_item(item_to_drop)
            player.room.add_item(item_to_drop)
            clear()
            print(f'You have dropped the {item_to_drop.name}')
    else:
        print('Inventory currently empty')
    return 

def quit_game():
    global playing
    global player
    print(f'Thanks for playing, {player.name}')
    playing = False
    





player = new_player()
playing = True
welcome_message()

potato = Item('potato', 'put it in a stew')
blanket = Item('blanket', 'warm')


player.add_item(potato)
player.add_item(blanket)


while playing:
    choice = main_menu()
    clear()
    if choice == '1':
        inspect(player)
    if choice == '2':
        move(player)
    if choice == '3':
        view_inventory(player)
    if choice == '4':
        quit_game()
    time.sleep(1)
    clear()