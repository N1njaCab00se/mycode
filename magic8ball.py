#!/usr/bin/env python3
""" Generic Magic 8 Ball | Travis Karraker """
import random
import time
import sys
import os


answers=["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, please try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.", "Nope.", "Trust me, DON'T ask again.", "Sure, why not?"]

def main():
    """Primary Run-time Code"""
    os.system('clear')
    question=input("Ask a Yes or No question of the Magic 8 Ball.\n>")
    print("Hmmmm....")
    time.sleep(random.randrange(2,6))
    print1by1(random.choice(answers))
    print()



def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def restart():
    """Ask to go again"""
    while True:
        #Ask input to play again
        #If answer is no, break
        #If yes, game() gets run again to restart game.
        answer = input("Would you like to ask something else?\n>").capitalize()
        if answer in ['Yes']:
            main()
        elif answer in ['No']:
            print("Goodbye!")
            break
        else:
            print("Please enter either Yes or No.")

main()
restart()


