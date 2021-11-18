""" Functions to control flow of the japanese cube test """


def welcome_choice_user():
    """ Greets the user, instructions and options, about, start and quit """
    print('''   \033[1mWelcome to the Japanese Cube test!\033[0m\n
        Meanwhile in the middle of the dessert...
    . . . .___________________________________________. . . .''')
    name = input('  Your name, please: \n')
    print('This is a game where all answers are right.')
    print(f'Use your imagination, ready {name}?')
    print('Take some time for describing every object...')


def choice_answer():
    """ Redirect the user input with the answer """
    choice = input('\x1B[3mChoose a(start), b(about), q(quit)\x1B[0m\n')
    choice_a = 'a'

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
        choice_b = input('\x1B[3mNext object = y, Restart = n\x1B[0m\n')
        if choice_b == 'n':
            print('You got out of the game, was that your intent?')
            print('Back to Main menu...')
            welcome_choice_user()
            choice_answer()
        elif choice_b != 'y':
            print('Not a recognized letter, starting over')
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
            choice_c = input('\x1B[3mNext = y, Restart = n\x1B[0m\n')
            if choice_c == 'n':
                print('You got out of the game, was that your intent?')
                print('Back to Main menu...')
                welcome_choice_user()
                choice_answer()
            elif choice_c != 'y':
                print('Not a recognized letter, starting over')
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
                choice_d = input('\x1B[3mNext = y, Restart = n\x1B[0m\n')
                if choice_d == 'n':
                    print('You got out of the game, was that your intent?')
                    print('Back to Main menu...')
                    welcome_choice_user()
                    choice_answer()
                elif choice_d != 'y':
                    print('Not a recognized letter, starting over')
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
                    choice_e = input('\x1B[3mNext = y, Restart = n\x1B[0m\n')
                    if choice_b == 'n':
                        print('You got out of the game, was that your intent?')
                        print('Back to Main menu...')
                        welcome_choice_user()
                        choice_answer()
                    elif choice_d != 'y':
                        print('Not a recognized letter, starting over')
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
                        print(40 * '*')
                        print('''\n    Now the explanation...

        The cube is your true self!
        If taller than your own height than
        your confidence is high while a smaller one
        means that you could be shy. If the cube is moving,
        it could symbolize a mind that is open and unconventional
        while a still sitting cube is businesslike, a cube that
        is dug into the sand means that you are a planner.
        A solid cube means you know who you are, while
        a hollow may mean that you are busy
        discovering your true self''')
                        print(f'    You wrote:{user_answer_first}')
                        print(40 * '*')
                        print('''\n
        The ladder represents two aspects of your life;\n
        Your goals and frienships.
        A short ladder represents a small
        circle of friends and realistic goals, while tall
        ladder means you have many friends, and your
        goals are difficult to attain.
        If leaned onto the cube, shows closeness
        towards your friends as well as reliability
        your friends have towrds you,
        and a ladder equal size as cube shows you
        that you see your friends as equals in authorithy
        Lower ladder means you consider yourself
        as alpha leader of the group of friends
        New looking ladder means new friendships are
        present in your life, while an old looking
        ladder would imply long enduring friendships''')
                        print(f'You described ladder: {user_answer_second}')
                        print(40 * '*')
                        # color of the horse - explain
                        print('''\n
        Next, the horse; it represents your
        partner. A horse closely related to cube means
        you strive for close relationships.
        And while brown sturdy horse can mean
        you would like a dependant partner,
        a glamorous looking horse would mean
        that you want a partner that will be
        groomed and approved by others.
        A horse moving towards the cube would signify
        a new relationship, while when horse moves away from
        the cube, means insecurities in relationship.
        Unicorn/Pegasus mean unrealistic expectations.
        A brown sturdy working horse means
        that you want a reliable and stabile partner''')
                        print(40 * '*')
                        print('\n')
                        print('''
        Next, the flowers represent your family/ children or anything
        you created and are taking care of. If the flowers are
        close to the cube, it means you are close to your
        children. A vibrant blossoming flowers would signify the
        healthy strong relationship with your kids, while
        too many flowers could mean you could be overwhelmed with
        too many concerns around your children. When wilting flowers
        would represent that relationships were broken or lost.''')
                        print(40 * '*')
                        print('\n')
                        print('''
        Next, the thunderstorm represents the
        stress and fears in your life and
        how you look at them. A strong storm
        can mean that the stress really gets
        to you, and it might be difficult to
        bounce back. A passing storm in the
        distance means your stress is visible
        to you but manageable, while if the
        storm is affecting any of the objects,
        you might be overwhelmed by the situation
        in your life. Just remember, you are
        bigger than your troubles. If the
        storm passed through and doesn\'t
        cause any change, means that you
        have confidence in resolving your
        stress.
        ''')

    elif choice == 'q':
        print('\x1B[3mYou are quitting, thanks for trying it out!\x1B[0m')
        print('Goodbye')
    elif choice == 'b':
        information_display()
        print('Would you like to try? (y/n)')
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
    print('''   This game derived from the Japanese personality test,
        which helps people discover what their true inner thoughts are about
        their current state of being.\n
        Note; this test could be tried out on your own
        to inspire you to get to know yourself, or in company to discover
        about your friends if they are open to try.\n
        Don\'t overthink it, just let imagination flow.
        It is only as accurate as you are honest with yourself
        Or... It could just be used for fun!\n''')
    print(40 * '*')


def display_users_descriptions():
    """ Displays answers that users gave and clarification of the meaning """


def all_funcs():
    """ Will be used to run all functions accordingly """
    welcome_choice_user()
    choice_answer()
    print('You exited the game')
    print('All functions work properly!')


all_funcs()
