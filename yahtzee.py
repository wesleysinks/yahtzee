#!/usr/bin/env python

"""
Classic Yahtzee game via terminal.

Rolls dice randomly, allows users to reroll dice selectively
and tracks a scorecard based on user options.
"""


import os
import sys
import random


# list of random dice face values
hand = []
cp_hand = []
key_index = ['a', 's', 'd', 'f', 'g']

def init_roll(fhand):
    while len(fhand) < 5:
        fhand.append(random.randint(1, 6))

def clear_screen():
    if os.name == 'nt':
        os.system('clr')
    else:
        os.system('clear')

# index for use key inputs
def show_dice_index():
    for key in key_index:
        print('  {}  '.format(key.upper()), end='')

# show the contents of the current hand
def show_dice(fhand):
    i = 0
    dice_1 = ''
    dice_2 = ''
    dice_3 = ''
    for dice_value in fhand:
        if dice_value == 1:
                dice_1 += '|   |'
                dice_3 += '|   |'
        elif dice_value == 2 or dice_value == 3:
                dice_1 += '|  *|'
                dice_3 += '|*  |'
        else:
                dice_1 += '|* *|'

        if dice_value == 1 or dice_value == 3 or dice_value == 5:
                dice_2 += '| * |'
        elif dice_value == 6:
                dice_2 += '|* *|'
        else:
                dice_2 += '|   |'
        
        if dice_value > 3:
                dice_3 += '|* *|'
        i += 1
    print('-'*25)
    print(dice_1)
    print(dice_2)
    print(dice_3)
    print('-'*25)

def reroll(fhand, user_input, key_index):
    for item in user_input:
        count = 0
        for key in key_index:
            if item == key:
                fhand[count] = random.randint(1, 6)
            count += 1

def title_art():
    print(r"""
__     __   _     _                
\ \   / /  | |   | |               
 \ \_/ /_ _| |__ | |_ _______  ___ 
  \   / _` | '_ \| __|_  / _ \/ _ \
   | | (_| | | | | |_ / /  __/  __/
   |_|\__,_|_| |_|\__/___\___|\___|
                                                                   
""")

def show_both():
    clear_screen()
    print("COMPUTER")
    show_dice(cp_hand)
    print("YOU")
    show_dice(hand)
    

def main():
    clear_screen()
    title_art()
    while True:
        start = input("Press Enter to play. Press Q to quit: ")
        if start.lower() == 'q':
            clear_screen()
            sys.exit()
        else:
            init_roll(cp_hand)
            init_roll(hand)
            show_both()
            show_dice_index()
            user_options = input("""\n\nHit the index for each dice you'd like 
to re-roll and press Enter: """)
            reroll(hand, user_options, key_index)
            show_both()
main()

# TODO
# make initial roll for computer player. work on logic for computer hand rerolls
# create scorecard table to be shown and rolls added per user aside rolls or between turns
