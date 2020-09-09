from room import Room
from player import Player
import time
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

room_type = type(room['outside'])
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
