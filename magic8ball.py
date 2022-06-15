#!/usr/bin/env python3
""" Generic Magic 8 Ball | Travis Karraker """
import random
import time
import sys
import os


answers=["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, please try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.", "Nope.", "Trust me, DON'T ask again.", "Sure, why not?"]

def main():
    """Primary Run-time Code"""
    #A question gets asked by the user.
    os.system('clear')
    question=input("Ask a Yes or No question of the Magic 8 Ball.\n>")
    print("Hmmmm....")
    time.sleep(random.randrange(2,6)) #Force the machine to pause to simulate "thinking".
    print1by1(random.choice(answers)) #Answer chosen at random and printed one character at a time.
    print()



def print1by1(text, delay=0.1):
    """Set parameters for how fast or slow answers get printed"""
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def restart():
    """Ask to go again"""
    while True:
        #Ask input to play again
        answer = input("Would you like to ask something else?\n>").capitalize()
        if answer in ['Yes']: 
            main() #When yes is said, main() gets called on again to restart the program
        elif answer in ['No']: #Simply put, when no is said, program ends
            print("Goodbye!")
            break
        else:
            print("Please enter either Yes or No.")

main()
restart()


