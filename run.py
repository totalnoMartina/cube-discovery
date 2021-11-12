

def welcome_choice_user():
    """ Greets the user, instructions and options, about, start and quit """
    print('Meanwhile in the middle of the dessert...')
    print('. . . .___________________________________________. . . .')
    print('Welcome!')
    name = input('Your name, please: \n')
    print('This is a game where all answers are right, and is here to inspire you.')
    print(f'The answers will be explained at the end of the test, ready {name}?')
    print('Take some time for describing every object...')


def choice_answer():
    """ Redirect the user input with the answer """
    choice = input('\x1B[3mChoose a to start, b to know more about, q to quit... \x1B[0m\n')
    choice_a = 'a'
    choice_b = 'y'
    choice_q = 'q'
    if choice == choice_a:
        print('\x1B[3mYou have chosen a to start the game!\x1B[0m \n')
        print('Imagine now... You find yourself in the dessert... ')
        print('Nothing around you... The objects start to appear...')
        print('There is the first object! It seems to be a cube')
        print(r"""
          _______            
        /\       \           
       /  \       \          
      /    \_______\         
      \    /       /         
       \  /       /          
        \/_______/

            """)
        print('Describe the shape, position or movement, volume, etc...')
        print()
        user_answer_first = input('Take a moment to imagine the cube... Write it down...\n')
        print('Okay, now... There is something else appearing in here...')
        choice_b = input('\x1B[3m...ready for the next object...?(y/n)\x1B[0m\n')
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
     
            """)
            user_answer_second = input('Take a moment to imagine the ladder... Write this down...')
            choice_c = input('\x1B[3m...ready for the next object...?(y/n)\x1B[0m\n')
            if choice_c == 'y':
                print('Something is coming towards the ladder and the cube,... looks like...')
                print('Looks like a horse! Imagine the horse, fitness, movement, relation to the rest of the objects')
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
'''
                )
                print('Take a moment to imagine where is the horse, what does it look like...')
                print('Is it related to the objects in any way? What way?')
                user_answer_third = input('Write down describing the horse...\n')
                print(f'There seems to be something else appearing in this scenery!')
                choice_d = input('\x1B[3m...ready for the next object...?(y/n)\x1B[0m\n')
                if choice_d == 'y':
                    print('From nowhere, flower or more of them appears...! How many in your imagination?')
                    print('Are they just blooming or wilting, are they close to the scene or far?')
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
                    print('Take a moment to create your flower or more of them ,describe them')
                    user_answer_fourth = input('Write down a few asociations to the idea of a flower/s... \n')
                    print('There is something appearing and becoming more vivid... What can it be?')
                    print('Looks like a thunderstorm... Now, imagine the strom related to the objects...')
                    print(r"""                          ________________________
                      ___(                        )
                     (                          _)
                     (_                       __))
                       ((                _____)
                         (__   _____)----'
                          _/  /
                         /  _/
                       _/  /
                     / __/
                  _/ /
                /__/
               //
              /'
                    """)
    elif choice == 'q':
      print('\x1B[3mYou are quitting the game, thanks for trying it out!\x1B[0m')
      


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