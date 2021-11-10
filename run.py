
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
    print(r"""\
        _______            
      /\       \           
     /  \       \          
    /    \_______\         
    \    /       /         
     \  /       /          
      \/______/

            """)


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
    print('All functions work properly!')


all_funcs()