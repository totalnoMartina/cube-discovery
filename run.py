

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
        user_answer_first = input('Take a moment to imagine and write it down\n')
        print('Okay, now... There is something else appearing in here...')
        choice_b = input('\x1B[3mReady for the next object...?(y/n)\x1B[0m\n')
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
            user_answer_second = input('Take a moment to imagine the ladder... Write this down...\n')
            choice_c = input('\x1B[3mReady for the next object...?(y/n)\x1B[0m\n')
            if choice_c == 'y':
                print('Something is coming towards the ladder and the cube,... looks like...')
                print('Looks like a horse! Imagine his figure, movement, relation to other objects')
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
                print('There seems to be something else appearing in this scenery!')
                choice_d = input('\x1B[3mReady for the next object...?(y/n)\x1B[0m\n')
                if choice_d == 'y':
                    print('From nowhere, flower or more of them appears...! How many in your imagination?')
                    print('Are they just blooming or wilting, are they related to others?')
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
                    user_answer_fourth = input('Write down the details... \n')
                    print('There is something else appearing... What can it be?')
                    print('Looks like a thunderstorm... Is it related to others?')
                    print(r"""                              ________________________
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
                    print('How is it related, and is it temporary or staying?')
                    user_answer_fifth = input('Write down what do you imagine')

    elif choice == 'q':
      print('\x1B[3mYou are quitting, thanks for trying it out!\x1B[0m')
    elif choice == 'b':
      print('This game derived from the Japanese personality test,')
      print('which by definition helps people discover what their')
      print('true inner thoughts are about their current state of being.\n')
      print('Note; this test could be tried out on your own to')
      print('help you get to know you, or in company to discover')
      print('about your friends if they are open to try.\n')
      print('It is only as accurate as you are honest with yourself')
      print('Or... It could just be used for fun!')
      while True:
        choice_answer()
 

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