""" Functions to control flow of the japanese cube test """

import sys
import os
from os import system, name


def display_users_descriptions():
    """ Displays interpretations """

    def cube_intepret():
        """ Description of the cube """

        print(r'''
                                                               .---.
                                                              /  .  \
                                                             |\_/|   |
                                                             |   |  /|
  .----------------------------------------------------------------' |
 /  .-.                    THE CUBE                                  |
|  /   \   The cube is your true self! If taller than cube, your     |
| |\_.  |  confidence is high while a shorter one means that you     |
|\|  | /|  could be shy. If the cube is moving, it could symbolize   |
| `---' |  an open-minded person while a still sitting cube is more  |
|       |  logical and businesslike, a cube that is dug into the     |
|       |  sand means you are a planner. A solid cube means you know |
|       |  who you are, while a hollow may mean that you are busy   /
\       |  discovering your true self.                             /
 \     /---------------------------------------------------------''
  `---'
    ''')

    def ladder_interpret():
        """ Description of the ladder """

        print(r'''
                                                               .---.
                                                              /  .  \
                                                             |\_/|   |
                                                             |   |  /|
  .----------------------------------------------------------------' |
 /  .-.                    THE LADDER                                |
|  /   \  The ladder represents two aspects of your life; Your goals |
| |\_.  | and frienships. A short ladder represents a small circle   |
|\|  | /| of friends and realistic goals, while a tall one means you |
| `---' | have many friends, and your goals are difficult to attain. |
|       | If leaned onto the cube, shows closeness towards your      |
|       | friends as well as reliability your friends have towards   |
|       | you. Equal size as cube shows that you see your friends as |
\       | equals in authorithy. Small ladder - you are the leader!  /
 \     /----------------------------------------------------------''
  `---'
    ''')

    def horse_interpret():
        """ Description of the horse """

        print(r'''
                                                               .---.
                                                              /  .  \
                                                             |\_/|   |
                                                             |   |  /|
  .----------------------------------------------------------------' |
 /  .-.                    THE  HORSE                                |
|  /   \   The horse represents your partner. If a horse is closely  |
| |\_.  |  related to the cube, means you strive in close and warm   |
|\|  | /|  relationships. And while brown sturdy horse can mean you  |
| `---' |  want a reliable and stabile partner, a shiny, well-kept   |
|       |  horse means that you want a partner that will be groomed  |
|       |  and approved by others. A horse moving towards the cube   |
|       |  would signify a new relationship, while if horse goes     |
\       |  away from the cube, symbolizes insecurities.             /
 \     /----------------------------------------------------------''
  `---'
    ''')

    def flowers_interpret():
        """ Description of the flowers """

        print(r'''
                                                               .---.
                                                              /  .  \
                                                             |\_/|   |
                                                             |   |  /|
  .----------------------------------------------------------------' |
 /  .-.                    THE FLOWERS                               |
|  /   \  The flowers represent your family/children/anything you    |
| |\_.  | created and are taking care of. If the flowers are close to|
|\|  | /| the cube, it means you have deep connection with your loved|
| `---' | ones. A vibrant blossoming flowers would signify a strong  |
|       | and healthy relationship, while too many flowers might be  |
|       | showing overwhelment with concerns around your family/kids |
|       | Wilting flowers could represent a relationship that is     |
\       | broken or lost.                                           /
 \     /----------------------------------------------------------''
  `---'
    ''')

    def thunderstorm_interpret():
        """ Description of the thunder """

        print(r'''
                                                               .---.
                                                              /  .  \
                                                             |\_/|   |
                                                             |   |  /|
  .----------------------------------------------------------------' |
 /  .-.                    THE THUNDERSTORM                          |
|  /   \   The thunderstorm represents the stress and fears in your  |
| |\_.  |  life and how you look at them. A strong storm can mean    |
|\|  | /|  that the stress really gets to you, and it mightbe hard   |
| `---' |  to bounce back. A passing storm far away means stress     |
|       |  gets to you but it's manageable, while if the storm is    |
|       |  affecting the objects, you might be overwhelmed by the    |
|       |  events in your life. If the storm passes by and there is /
\       |  no change, means you have confidence in solving issues ./
 \     /---------------------------------------------------------''
  `---'
  ''')

    list_of_functions = [
        cube_intepret,
        ladder_interpret,
        horse_interpret,
        flowers_interpret,
        thunderstorm_interpret]

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
            print('RUN PROGRAM for starting over! Have fun!')
            sys.exit()
        elif ask_explain.lower() == 'y':
            display_users_descriptions()
            another_try = input('Press y to start again or Enter to exit!')
            if another_try.lower() == 'y':
                clear()
                print('You have chosen y to try this test again!')
                welcome_choice_user()
                choice_answer()
            elif another_try != 'y':
                print('Hope you enjoyed! Thanks for trying it out!')
                print('RUN PROGRAM to start over! Hope you had fun! Goodbye!')
                sys.exit()
        else:
            print('Wrong letter, try again!')
            interpretation()
    else:
        print('You did not enter recognized character. Try again')
        interpretation()
        sys.exit()


def clear():
    """Clearing function to clear the screen"""

    os.system("cls" if os.name == "nt" else "clear")


def thunder():
    """Function to call fifth object"""

    print('It\'s a storm, more like a thunderstorm!')
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
    print('Use as many words as you like to describe and press Enter')
    user_answer_fifth = input('Imagine, write it down\n')
    # Check for empty space as user input
    if user_answer_fifth == '':
        clear()
        print('Ooops, nothing is written. Please describe the shape')
        thunder()
    else:
        clear()
        print(f'About the thunder, you wrote "{user_answer_fifth}" \n')
        print('That was the last object, your interpretation is ready!')
        interpretation()


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
    print('Use as many words as you like to describe, then press Enter')
    user_answer_fourth = input('Write down the details... \n')
    # Check empty space for user input
    if user_answer_fourth == '':
        clear()
        print('Ooops, nothing is written. Please describe in details')
        flowers()
    elif user_answer_fourth:
        clear()
        print(f'About the flowers, you wrote: "{user_answer_fourth}" \n')
        print('There is something else appearing here...')
        thunder()


def horse():
    """Function to call third object"""

    print('Looks like a horse!')
    print('Imagine his figure, movement, relation to others')
    print(r'''


    >>\.
   /_  )`.
  /  _)`^)`.   _.---. _
 (_,' \  `^-)""      `.\
       |               | \
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
    # Check empty space for user input
    if user_answer_third == '':
        clear()
        print('Ooops, nothing is written. Please describe the shape')
        horse()
    else:
        clear()
        print(f'About the horse, you wrote: "{user_answer_third}"\n')
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
    print('Use as many words to describe many details and press Enter')
    user_answer_second = input('Imagine, write it down...\n')
    # Check empty space for user input
    if user_answer_second == '':
        clear()
        print('Ooops, nothing is written. Please describe the shape')
        ladder()
    else:
        clear()
        print(f'About the ladder, you wrote: "{user_answer_second}" \n')
        print('Okay, now... There is something else appearing in here...')
        horse()


def cube():
    """Function to start with first object"""

    print('\x1B[3mYou have chosen a to start the game!\x1B[0m \n')
    print('''Imagine now... You find yourself in the dessert...
Nothing around you... The objects start to appear...
There is the first object! Looks like a cube''')
    print(r"""

         ________
        /\       \
       /  \       \
      /    \_______\
      \    /       /
       \  /       /
        \/_______/

        """)
    print('Describe the shape, position or movement, volume...\n')
    print('Use as many words to describe the details and press Enter')
    user_answer_first = input('Take a moment to imagine, write it down\n')
    # Check empty space as user input
    if user_answer_first == '':
        clear()
        print('No description, try again')
        cube()
    else:
        clear()
        print(f'About the cube, you wrote: "{user_answer_first}" \n')
        print('Okay, now... There is something else appearing in here...')
        ladder()


def choice_answer():
    """ Redirect the user input with the answer """

    choice = input('\x1B[3mChoose a(start), b(about), q(quit)\x1B[0m\n')
    # Check user input for specific letters
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
            print('You chose n, thanks for checking this out! Bye!')
            sys.exit()
        else:
            clear()
            print('You did not choose valid option, try again')
            choice_answer()
    elif choice.lower() == 'q':
        print('\x1B[3mYou are quitting, thanks for trying it out!\x1B[0m')
        print('Goodbye')
        sys.exit()
    else:
        clear()
        print('Not a recognized letter, starting over')
        choice_answer()


def welcome_choice_user():
    """ Greets the user, instructions and options, about, start and quit"""

    print('''   \033[1mWelcome to the Japanese Cube test!\033[0m\n
    Meanwhile in the middle of the dessert
    . . . .___________________________________________. . . .''')
    name = input('Nice to have you here, your name in one word, please:\n')
    # Check empty or special characters for users name
    if not name.isalpha() or name == '':
        print('You entered invalid value, please try again')
        welcome_choice_user()
    else:
        clear()
        print('This is a test where all answers are right.')
        print(f'Use your imagination, ready {name}?')
        print('Take some time for describing every object...\n')
        # Start with test questions
        choice_answer()


def information_display():
    """ Gives information of this test - activate imagination and inspire """

    print(r'''            ____________________________
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


# Calling first function to start the game
welcome_choice_user()
