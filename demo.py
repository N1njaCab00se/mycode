#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""

round = 0           # integer round initiated to 0
while True:        # sets up an infinite loop condition
    round = round + 1     # increase the round counter
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    if answer == 'Brian':
        print('Correct!')
        break
    elif answer == 'Shrubbery':
        print('You gave the SUPER SECRET answer! NI!')
        break
    elif round == 3:
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry. Try again!')

