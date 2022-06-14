#!/usr/bin/env python3
import random

answers=["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, please try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.", "Nope.", "Trust me, DON'T ask again.", "Sure, why not?"]

def main():
    question=input("Ask a Yes or No question of the Magic 8 Ball.\n")
    print(random.choice(answers))


main()

def restart():
    while True:
        #Ask input to play again
        #If answer is no, break
        #If yes, game() gets run again to restart game.
        answer = input("Would you like to play again?\n").capitalize()
        if answer in ['Yes']:
            main()
        elif answer in ['No']:
            print("Goodbye!")
            break
        else:
            print("Please enter either Yes or No.")
restart()
