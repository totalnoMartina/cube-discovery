
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


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
    choice_b = 'y'
    if choice == choice_a:
        print('You have chosen a')
        print('You started the game... You find yourself in the dessert... ')
        print('Nothing around you... The objects start to appear...')
        print('There is the first object! It is a cube')
        print(r"""
        _______            
      /\       \           
     /  \       \          
    /    \_______\         
    \    /       /         
     \  /       /          
      \/______/

            """)
        print('Describe the shape, position or movement, volume, etc...')
        print('Take a moment to imagine the cube...')
    choice_b = input('...ready for the next object...?(y/n)\n')
    if choice_b == 'y':
        print('From out of nowhere, a ladder shows up...')
        print('What size, shape, material of ladder do you imagine?')
        print('Is there anything related between the cube and ladder?')
        print(r"""
        ╬═╬
        ╬═╬
        ╬═╬
        ╬═╬
        ╬═╬
        ╬═╬
        ╬═╬
        ╬═╬
        ╬═╬
        """)
    choice_bb = input()


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