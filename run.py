""" Functions to control flow of the japanese cube test """
# import tabulate
# tabulate.WIDE_CHARS_MODE = False
import os
from os import system, name

def clear():
    """Clearing function to clear the screen"""

    os.system("cls" if os.name == "nt" else "clear")


def thunder():
    """Function to call fifth object"""

    print('It\'s a storm, more like a thundrstorm!')
    print('Imagine, where is it? ')
    print(r"""                            ________________________
                         __(                        )
                        (                          _)
                        (_                       __))
                          ((                _____)
                            (_    _____)----'
                            _/  /
                          /  _/
                        _/  /
                      / __/
                    _/ /
                   /__/
                  //
                 /
                """)
    print('Is it close or far? Does it affect others?')
    print('How is it related, is it temporary or staying?')
    user_answer_fifth = input('Imagine, write it down\n')
    print('Use as many words as you like, describe the details and press Enter')
    if user_answer_fifth.isalpha() == '':
        clear()
        print('Ooops, nothing is written. Please describe the shape')
        thunder()
    elif not user_answer_fifth.isalpha():
        print('Not even a letter, please enter some description')
        thunder()
    else:
        print('That was the last object, your interpretation is ready!')
    print(f'You wrote {user_answer_fifth}')


def flowers():
    """Function to call fourth object"""

    print('It looks like flowers! Where are they?')
    print('How many do you imagine?')
    print(r"""
        .'`'.'`'.
    .''.`.  :  .`.''.
    '.    '._.'    .'
    .```  .'-'.  ```.
    '..',`  :  `,'..'
        `-'`'-`))
            ((
            \|

                    """)
    print('Are they blooming or wilting?')
    print('Take a moment to imagine, describe...')
    print('Use as many words as you like, describe the details and press Enter')
    user_answer_fourth = input('Write down the details... \n')
    if user_answer_fourth == '':
        clear()
        print('Ooops, nothing is written. Please describe in details')
        flowers()
    elif not user_answer_fourth.isalpha():
        print('Not even a letter, please enter some description')
        flowers()
    else:
        print(f'You wrote: "{user_answer_fourth}"')
        print('There is something else appearing here...')
        thunder()


def horse():
    """Function to call third object"""

    print('Something is coming from out of nowhere,...')
    print('Looks like a horse!')
    print('Imagine his figure, movement, relation to others')
    print(r'''
  >>\.
 /_  )`.
/  _)`^)`.   _.---. _
(_,' \  `^-)""      `.\
      |              | \
        \              / |
        / \  /.___.'\  (\ (_
       < ,"||      \ |`. \`-'
         \\ ()      )|  )/
         |_>|>     /_] //
            /_]       /_]
''')
    print('Take a moment to imagine, what does it look like...')
    print('Is it related to the objects in any way? What way?')
    user_answer_third = input('Write down what you imagine...\n')
    print('Use as many words to describe many details and hit Enter')
    if user_answer_third == '':
        clear()
        print('Ooops, nothing is written. Please describe the shape')
        horse()
    elif not user_answer_third.isalpha():
        print('Not even a letter, please enter some description')
        horse()
    else:
        print(f'You wrote: "{user_answer_third}"')
        print('There seems to be something else appearing...!')
        flowers()


def ladder():
    """Function to use second object"""

    print('From out of nowhere, a ladder shows up...')
    print('What size, position, material of ladder do you imagine?')
    print(r"""
            ╬═╬
            ╬═╬
            ╬═╬
            ╬═╬
            ╬═╬
            ╬═╬
            ╬═╬
    """)
    print('Is there anything related between the cube and ladder?')
    print('Use as many words to describe many details and hit Enter')
    user_answer_second = input('Imagine, write it down...\n')
    if user_answer_second == '':
        clear()
        print('Ooops, nothing is written. Please describe the shape')
        ladder()
    elif not user_answer_second.isalpha():
        print('Not even a letter, please enter some description')
        ladder()
    else:    
        print(f'You wrote: "{user_answer_second}"')
        print('Okay, now... There is something else appearing in here...')
        horse()

def cube():
    """Function to start with first object"""

    print('\x1B[3mYou have chosen a to start the game!\x1B[0m \n')
    print('''Imagine now... You find yourself in the dessert...
        Nothing around you... The objects start to appear...
        There is the first object! It seems to be a cube''')
    print(r"""
         ________
        /\       \
       /  \       \
      /    \_______\
      \    /       /
       \  /       /
        \/_______/""")
    print('Describe the shape, position or movement, volume...\n')
    user_answer_first = input('Take a moment to imagine, write it down\n')
    print('Use as many words to describe many details and hit Enter')
    if user_answer_first == '':
        clear()
        print('You must describe the shape, try again')
        cube()
    elif not user_answer_second.isalpha():
        print('Not even a letter, please enter some description')
        cube()
    else:
        print(f'You wrote: "{user_answer_first}"')
        print('Okay, now... There is something else appearing in here...')
        ladder()


def choice_answer():
    """ Redirect the user input with the answer """

    choice = input('\x1B[3mChoose a(start), b(about), q(quit)\x1B[0m\n')
    if choice.lower() == 'a':
        clear()
        cube()
    elif choice.lower() == 'b':
        information_display()
        ask = input('Wanna try this now? (y/n)')
        if ask.lower() == 'y':
            clear()
            cube()
        elif ask.lower() == 'n':
            clear()
            print('You chose n, thanks for checking this out!')
            exit()
        else:
            clear()
            print('You did not choose valid option, try again')
            choice_answer()
    elif choice.lower() == 'q':
        print('\x1B[3mYou are quitting, thanks for trying it out!\x1B[0m')
        print('Goodbye')
        exit()
    else:
        clear()
        print('Not a recognized letter, starting over')
        choice_answer()


def next_or_restart():
    """Function to use for iterating through objects and call it"""

    ask_user = input('\x1B[3mNext = y, Restart = n\x1B[0m\n')
    if ask_user.isalpha() == 'n':
        clear()
        print('You got out of the game,...')
        print('Restarting... Back to Main menu...')
        welcome_choice_user()
        choice_answer()
    elif ask_user.isalpha == '':
        clear()
        print('You entered invalid value, Back to Main menu')
        welcome_choice_user()
        choice_answer()


def welcome_choice_user():
    """ Greets the user, instructions and options, about, start and quit"""

    print('''   \033[1mWelcome to the Japanese Cube test!\033[0m\n
    Meanwhile in the middle of the dessert
    . . . .___________________________________________. . . .''')
    name = input('Nice to have you here, your name, please:\n')
    if not name.isalpha() or name == '':
        print('You entered invalid value, please try again')
        welcome_choice_user()
    else:
        print('This is a game where all answers are right.')
        print(f'Use your imagination, ready {name}?')
        print('Take some time for describing every object...\n')
        choice_answer()


def information_display():
    """ Gives information of this test - activate imagination and inspire """

    print('''            ____________________________
            /                           \.
         / \     This is an ancient     |.
        |  | Japanese personality test, |.
        \_ | which helps people discover|.
           | what their true inner      |.
           | thoughts are about their   |.
           | current state of being.Just|.
           | close your eyes and imagine|.
           | you are in a dessert,      |.
           | nothing around, just sand &|.
           | sky. Objects will appear to|.
           | inspire you and you can    |.
           | write your description.    |.
           |      Have fun with this!   |.
           |   _________________________|___
           |  /                            /.
           \_/____________________________/.''')


def display_users_descriptions():
    """ Displays interpretations """

    def cube_intepret():
        print('''
    The cube is your true self! If
    taller than cube, your confidence
    is high while a shorter one means
    that you could be shy. If the
    cube is moving, it could symbolize
    a open-minded person while a
    still sitting cube is businesslike, a
    cube that is dug into the sand means
    that you are a planner. A solid cube
    means you know who you are, while
    a hollow may mean that you are busy
    discovering your true self''')
    def ladder_interpret():
        print('''
    The ladder represents two aspects of
    your life; Your goals and frienships.
    A short ladder represents a small
    circle of friends and realistic goals,
    while tall one means you
    have many friends, and your goals
    are difficult to attain. If leaned
    onto the cube, shows closeness
    towards your friends as well as
    reliability your friends have towards
    you, and if equal size as
    cube shows you that you see your
    friends as equals in authorithy.
    If lower, it means you consider
    yourself as a leader of the group.
    Brand new looking ladder
    means new friendships, while an
    old looking one would imply
    long enduring friendships''')
    
    def horse_interpret():
        print('''
    Next, the horse; it represents your
    partner. A horse closely related to
    cube means you strive for close
    relationships. And while brown sturdy
    horse can mean you would like a
    dependant partner, a glamorous looking
    horse would mean that you want a
    partner that will be groomed and
    approved by others. A horse moving
    towards the cube would signify
    a new relationship, while when horse
    moves away from the cube, means
    insecurities in relationship.
    Unicorn/Pegasus mean unrealistic
    expectations. A brown sturdy working
    horse means that you want a reliable
    and stabile partner''')
    
    def flowers_interpret():
        print('''
    The flowers represent your family or
    children or anything you created and are
    taking care of. If the flowers are
    close to the cube, it means you are
    close to your children. A vibrant
    blossoming flowers would signify the
    healthy strong relationship with your
    kids/relatives, while too many flowers could
    mean you could be overwhelmed with
    too many concerns around your family.
    When wilting flowers would represent
    that relationships are broken or lost.''')
    
    def thunderstorm_interpret():
        print('''
    The thunderstorm represents the
    stress and fears in your life and
    how you look at them. A strong storm
    can mean that the stress really gets
    to you, and it might be difficult to
    bounce back. A passing storm in the
    distance means your stress is visible
    to you but manageable, while if the
    storm is affecting any of the objects,
    you might be overwhelmed by the
    situation in your life. Just remember,
    you are bigger than your troubles.
    If the storm passed through and doesn\'t
    cause any change, means that you
    have confidence in resolving your
    stress.''')
    list_of_functions = [cube_intepret, ladder_interpret, horse_interpret, flowers_interpret, thunderstorm_interpret]
    for i in range(len(list_of_functions)): 
        list_of_functions[i]()
        input('Press enter to proceed')
        clear()


def interpretation():
    """ Ask user to check the interpretation"""

    ask_explain = input('Would you like to see your interpretation? (y/n)')
    ask_explain = ask_explain.lower()
    if ask_explain.isalpha():
        if ask_explain.lower() == 'n':
            print('You choose n! Thanks for trying this out!')
            exit()
        elif ask_explain.lower() == 'y':
            display_users_descriptions()
            another_try = input('Press y to start the test again or Enter to exit!')
            if another_try.lower() == 'y':
                clear()
                print('You have chosen y to try this test again!')
                welcome_choice_user()
                choice_answer()
            elif another_try != 'y':
                print('Hope you enjoyed! Thanks for trying it out!')
                exit()
        else:
            print('Wrong letter, try again!')
            interpretation()
    else:
        print('You did not enter recognized character')
        interpretation()
        exit()


def all_funcs():
    """ Run all functions accordingly """

    # welcome_choice_user()
    # next_or_restart()
    # ladder()
    # next_or_restart()
    # horse()
    # next_or_restart()
    flowers()
    # next_or_restart()
    # thunder()
    interpretation()
    print('You exited the game')
    print('All functions work properly!')


all_funcs()
