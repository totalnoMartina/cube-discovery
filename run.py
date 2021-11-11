
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import time


def welcome_choice_user():
    """ Greets the user, instructions and options, about, start and quit """
    print('Meanwhile in the middle of the dessert...')
    print('Welcome!')
    name = input('Your name, please: \n')
    print('This is a game of revelation, it will expand as you describe and')
    print(f'reveal what really hides behind imagination, ready {name}?')
    print('Take 20 seconds for describing every object and how it relates')
    print('Choose "a" to start, "b" to learn more or "q" to exit')
    

def choice_answer():
    """ Redirect the user input with the answer """
    choice = input('Choose a to start, b to know more about, q to quit... \n')
    choice_a = 'a'
    if choice == choice_a:
        print('You have chosen a')
        print('You started the game... You find yourself in the dessert... ')
        print('Nothing around you... The objects start to appear...')
        print('There is the first object! It is a cube')
        print(r"""\n
        _______            
      /\       \           
     /  \       \          
    /    \_______\         
    \    /       /         
     \  /       /          
      \/______/

            """)
        print('Describe the shape, position or movement, volume, color or no color...')
        print('Take a moment to imagine the cube...')


def questions():
    """ Asks user to describe objects and how they relate to one another """
    pass


def information_display():
    """ Gives information of this game - activate imagination and inspire """
    pass


def display_users_descriptions():
    """ Displays answers that users gave and clarification of the meaning """


def end_game():
    """ To play again or quit """
    pass


def all_funcs():
    """ Will be used to run all functions accordingly """
    welcome_choice_user()
    choice_answer()
    print('All functions work properly!')


all_funcs()