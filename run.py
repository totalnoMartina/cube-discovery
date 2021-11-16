""" Functions to control flow of the japanese cube test """


def welcome_choice_user():
    """ Greets the user, instructions and options, about, start and quit """
    print('''   Welcome to the Japanese Cube test!\n
        Meanwhile in the middle of the dessert...
    . . . .___________________________________________. . . .''')
    name = input('    Your name, please: \n')
    print('This is a game where all answers are right.')
    print(f'Use your imagination, ready {name}?')
    print('Take some time for describing every object...')


def choice_answer():
    """ Redirect the user input with the answer """
    choice = input('\x1B[3mChoose a(start), b (about), q(quit)\x1B[0m\n')
    choice_a = 'a'
    choice_b = 'y'

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
        print('Describe the shape, position or movement, volume...\n')
        user_answer_first = input('Take a moment to imagine, write it down\n')
        print(f'You wrote: "{user_answer_first}"')
        print('Okay, now... There is something else appearing in here...')
        choice_b = input('\x1B[3mReady for the next object?(y/n)\x1B[0m\n')
        if choice_b != 'y':
            print('You got out of the game, was that your intent?')
            print('Back to Main menu...')
            welcome_choice_user()
            choice_answer()
        elif choice_b == 'y':
            print('From out of nowhere, a ladder shows up...')
            print('What size, position, material of ladder do you imagine?')
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
            user_answer_second = input('Imagine, write it down...\n')
            print(f'You wrote: "{user_answer_second}"')
            print('Okay, now... There is something else appearing in here...')
            choice_c = input('\x1B[3mReady for the next object?(y/n)\x1B[0m\n')
            if choice_c != 'y':
                print('You got out of the game, was that your intent?')
                print('Back to Main menu...')
                welcome_choice_user()
                choice_answer()
            elif choice_c == 'y':
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
'''
                      )
                print('Take a moment to imagine, what does it look like...')
                print('Is it related to the objects in any way? What way?')
                user_answer_third = input('Write down what you imagine...\n')
                print(f'You wrote: "{user_answer_third}"')
                print('There seems to be something else appearing...!')
                choice_d = input('\x1B[3mReady for the next object?(y/n)\x1B[0m\n')
                if choice_b != 'y':
                    print('You got out of the game, was that your intent?')
                    print('Back to Main menu...')
                    welcome_choice_user()
                    choice_answer()
                elif choice_d == 'y':
                    print('It looks like flowers!')
                    print('How many do you imagine?')
                    print('Are they blooming or wilting?')
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
                    print('Take a moment to imagine, describe...')
                    user_answer_fourth = input('Write down the details... \n')
                    print(f'You wrote: "{user_answer_fourth}"')
                    choice_e = input('\x1B[3mReady for the next object?(y/n)\x1B[0m\n')
                    if choice_b != 'y':
                        print('You got out of the game, was that your intent?')
                        print('Back to Main menu...')
                        welcome_choice_user()
                        choice_answer()
                    elif choice_e == 'y':
                        print('There is something else! Thunderstorm')
                        print(r"""                                  ________________________
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
                        print('Is it close or far? Does it affect others?')
                        print('How is it related, is it temporary or staying?')
                        user_answer_fifth = input('Imagine, write it down\n')
                        print(f'You wrote: "{user_answer_fifth}"')
                
            print(20 * '*')
            print('The cube is your true self!')
            print('If taller than your own height than')
            print('your confidence is high while a smaller one')
            print('means that you could be shy. If the cube is moving, ')
            print('it could symbolize a mind that is open and unconventional')
            print('while a still sitting cube is businesslike, a cube that')
            print('is dug into the sand means that you are a planner.')
            print('A solid cube means you know who you are, while')
            print('a hollow may mean that you are busy')
            print('discovering your true self')
            print(f'This is what you wrote down: {user_answer_first}')
            print(20 * '*')
            print('The ladder represents your friends/ relatives;')
            print('A short ladder represents a small ')
            print('circle of friends, while tall means you have many')
            print('friends. If leaned onto the cube, ladder shows dependancy')
            print('and a ladder equal size as cube shows you')
            print('that you see your friends as equals in authorithy')
            print('Lower ladder means you consider yourself')
            print('as alpha leader of the group of friends')
            print('New looking ladder means new friendships are')
            print('present in your life, while an old looking')
            print('ladder would imply long enduring friendships')
            print(f'This is how you described ladder: {user_answer_second}')
            print(20 * '*')
            print('Next, the horse; it represents your')
            print('partner. A horse closely related to cube means')
            print('you strive for close relationships.')
            print('And while brown sturdy horse can mean')
            print('you would like a dependant partner,')
            print('a glamorous looking horse would mean')
            print('that you want a partner that will be')
            print('groomed and approved by others.')
            print('A horse moving towards the cube would signify')
            print('a new relationship, while when horse moves away from')
            print('the cube, means insecurities in relationship.')
            print('Unicorn/Pegasus mean unrealistic expectations.')
            print('A brown sturdy working horse means')
            print('that you want a reliable and stabile partner')
            print(20 * '*')

    elif choice == 'q':
        print('\x1B[3mYou are quitting, thanks for trying it out!\x1B[0m')
        print('Goodbye')
        
    elif choice == 'b':
        information_display()
        print('Want to try this out? (y/n)')
        about_choice = input('Enter y or n\n')
        if about_choice == 'y':
            welcome_choice_user()
            choice_answer()
        else:
            print('Thanks for checking this out!')
    elif choice == 'n':
        print('You want to stop the game?')
        print('Thanks for playing!')
    else:
        print('You did not enter a valid letter, let\'s try again')
        welcome_choice_user()
        choice_answer()


def information_display():
    """ Gives information of this game - activate imagination and inspire """
    print('This game derived from the Japanese personality test,')
    print('which by definition helps people discover what their')
    print('true inner thoughts are about their current state of being.\n')
    print('Note; this test could be tried out on your own')
    print('to inspire you to get to know yourself, or in company to discover')
    print('about your friends if they are open to try.\n')
    print('Don\'t overthink it, just let imagination flow.')
    print('It is only as accurate as you are honest with yourself')
    print('Or... It could just be used for fun!\n')
    print(20 * '*')
    

def display_users_descriptions():
    """ Displays answers that users gave and clarification of the meaning """
    pass





def all_funcs():
    """ Will be used to run all functions accordingly """
    welcome_choice_user()
    choice_answer()
    # if choice_answer() == "return"[None]:
    #    print('You exited the game')
    print('All functions work properly!')


all_funcs()
