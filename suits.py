#!/usr/bin/env python3
import random
def game():
    #Game chooses the suit 
    x = random.choice(['Spade', 'Club', 'Diamond', 'Heart'])

    turn = 0

    print("DEBUG:", x)

    while turn < 3:

        guess = input("Predict the card suit! You have three guesses!\n").capitalize()
        if guess not in ['Spade', 'Club', 'Diamond', 'Heart']:
            print("Please put in a valid suit.")
            continue
        turn += 1
        if guess == x:
            print("You guessed it! Good job!")
            break
        elif turn == 3:
            print("Sorry! The correct suit is", x)
            break
        else:
            print("That's not it! Try again!")
game()

def main():
    while True:
        #Ask input to play again
        #If answer is no, break
        #If yes, game() gets run again to restart game.
        answer = input("Would you like to play again?\n").capitalize()
        if answer in ['Yes']:
            game()
        elif answer in ['No']:
            print("Goodbye!")
            break
        else:
            print("Please enter either Yes or No.")
main()
