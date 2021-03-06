#!/usr/bin/python3
from random import randint
import dice
import sys
import os
import time
# Replace RPG starter project with this code when new instructions are live
bestiary = [{'name' : 'goblin', 'health' : 10, 'damage' : '1d5'},
            {'name' : 'orc', 'health' : 15, 'damage' : '1d8'},
            {'name' : 'ogre', 'health' : 20, 'damage' : '1d12'}]
armory = {'knife': {'damage': '1d12'}}
spell_lookup = {'fireball': {'damage': '4d6'}}
player_health = 30
spellbook = []

def combat():
    monster_ID= randint(0,2)

    global player_health, inventory, armory, bestiary
    round = 1
    monster_health = bestiary[monster_ID]['health']   
    print(f"A ferocious {bestiary[monster_ID]['name']} approaches! COMBAT HAS BEGUN!\n")
    while True:
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Monster Health: [" + str(monster_health) + "]")

        print("Type: RUN or USE [weapon]") # gotta write code for cast
        move = input().lower().split() # converts move into a lower-case list to deal with each item in list separately
        monster_damage = sum(dice.roll(bestiary[monster_ID]['damage']))
        print("\n=========================")


        if move[0] == 'use': #
            if move[1] in inventory: # checks if weapon is in your inventory
                player_damage = dice.roll(armory[move[1]]['damage'])
                print(f"You hit a {bestiary[monster_ID]['name']} for {player_damage} damage!")
            if move[1] not in inventory:
                print(f"There is no {move[1]} in your inventory!")

        if move[0] == 'cast': #
            if move[1] in spellbook: # checks if spell is in your spellbook
                if move[1].lower() == 'fireball':
                    player_damage = sum(dice.roll(spell_lookup[move[1]]['damage']))
                    print(f"Summoning eldritch forces, you scorch the {bestiary[monster_ID]['name']} for {player_damage} damage!")
            if move[1] not in spellbook:
                print(f"You don't know the {move[1]} spell!")

        if move[0] == 'run': #
            escape_chance= randint(1,10) #+ player_speed # if I set this variable later, here's where it would work

            if escape_chance >= 10:
                print("You make a flawless escape!")
                break
            if escape_chance >= 5:
                print("You expose your back as you turn and flee- the monster takes advantage.")
                print(f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
                player_health -= int(monster_damage)
                if player_health >= 1:
                    print("You managed to escape.")
                    break
                if player_health < 1:
                    print("You have been slain.")
                    print("\nGAME OVER")
                    sys.exit()
            if escape_chance >= 0:
                print("The monster out-maneuvers you and attacks! You do not escape.")

        try:
            monster_health -= int(player_damage)
        except:
            pass
        if monster_health <= 0:
            print(f"The {bestiary[monster_ID]['name']} lies dead. You are victorious!\n")
            del rooms[currentRoom]['item']
            print("You feel as if there's more to be done before you make a daring escape...")
            break

        print(f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
        print ("=========================\n")
        round += 1
        player_health -= int(monster_damage)

        if player_health <= 0:
            print("You have been vanquished! You are dead.")
            sys.exit()
def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  search
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

answered = False

# A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'west'  : 'Worship Room',
                },
            'Worship Room': {
                  'east'  : 'Hall',
                  'item'  : 'knife',
                },
            'Bedroom': {
                  'west' : 'Dining Room',
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
                  'east' : 'Bedroom',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            },
            "Traproom" : {}
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')


  if move[0] == "search":
      if currentRoom == "Bedroom":
          print("You find a trap door!")
          rooms["Bedroom"]["down"]= "Traproom"
          # adding "down":"Traproom" to the Bedroom dictionary
      else:
          print("You don't find anything")

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

# Worship Room Riddle
  if currentRoom == 'Worship Room' and answered == False:
      answer=["a dorc", "a dork", "dorc", "dork"]
      print('As you enter, a statue on the opposite side of the room speaks.')
      print('\"Your mother is an orc. Your father is a dwarf. What are you?\"')
      reply=input(">")
      if reply in answer:
          print("\"HAH! Your words, not mine. Here, take this since you amused me.\"")
          answered = True
      else:
          print("\"No, that's not it. Now leave this room, only return when you have the answer.\"")
          currentRoom='Hall'

## If a player falls through the trapdoor
  if currentRoom == 'Traproom':
      print('You have fallen through a trapdoor! As you get up from the fall, you hear the trapdoor above shut, followed by a heavy clunk. Your fate is sealed. GAME OVER!')
      break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    combat()
