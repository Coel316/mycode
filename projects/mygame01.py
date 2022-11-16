#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [key]
      get [potion]
      get [fruit]
      drink [water]
      sleep_in [bed]
      read [Bible]
      play [riddle]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('----------------------------------')
    print('You are in the ' + currentRoom)
    print('')
    print(' -- Commands: get [key], get [potion], get [fruit], \n drink [water], sleep_in [bed], read [bible], play [riddle] --')   
    # print what the player is carrying
    print('')
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see ' + rooms[currentRoom]['item'])
    # added item2 to accomodate numerous items in room
    if "item2" in rooms[currentRoom]:
        print('You see ' + rooms[currentRoom]['item2'])
    print("----------------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'west'  : 'Bedroom',
                  'item'  : 'water'
                },

            'Bedroom' : {
                   'east' : 'Kitchen',
                   'item' : 'bed'
                },

            'Dining Room' : {
                  'west' : 'Hall',
                  'east' : 'Study Room',
                  'south': 'Garden',
                  'item' : 'potion'
               },

            'Study Room' : {
                   'west' : 'Kitchen',
                   'item' : 'bible'
                },

            'Garden' : {
                  'north' : 'Dining Room',
                  'south' : 'Riddle Room',
                  'item'  : 'fruit'
            },

            'Riddle Room' : {
                   'north': 'Garden',
                   'item' : 'riddle',
                   'item2' : '$500'
            }
         }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over,
# getting the wrong answer means the game is over
while True:
    """Question user on their knowledge by asking questions,
    if user gets both riddles right, user gets $500 in inventory"""
    def riddle():
        print("Riddle me these ???")
        print("")
        user_first_input = input("Which animal in Noah's Ark could Noah not trust ?\n")
        user_first_input = user_first_input.lower()
        if user_first_input == 'cheetah':
            print('Nice work.  Let\'s move onto the FINAL Riddle')
            print("")
            user_second_input = input('Out of the eater came forth meat, and out of the strong came forth sweetness\n'
            'Fill in the blank -> What is sweeter than honey? and what is stronger than a ____________ ?\n'
            'Please input your answer: ')
            if (user_second_input == 'lion' and "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']
            and "item2" in rooms[currentRoom]):
                inventory.append(rooms[currentRoom]['item2'])
                print("")
                print('You just won $500.')
                # display a helpful message
                print('Congrats! You got the ' + move[1] + ".  $500 added to inventory")
                # delete the item key:value pair from the room's dictionary
                del rooms[currentRoom]['item']
                del rooms[currentRoom]['item2']
                    
            else:
                print("")
                print('Sorry, wrong answer.  You won NO $$$.  GAME OVER !!!')
                quit()
        else:
            print("")
            print('Sorry, wrong answer.  GAME OVER !!! ')
            quit()

    showStatus()

    # the player MUST type something in,
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    # if the user types 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if the user types 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and move[1] in ['key', 'potion', 'fruit']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if the user types 'drink'
    if move[0] == 'drink' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to drink
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and move[1] in ['water']:
            # display a helpful message
            print('Drink up. ' + move[1] + ' is essential !')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell user that there is no more water
            print('Can\'t get any more ' + move[1])

    # if the user types 'sleep_in'
    if move[0] == 'sleep_in' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches bed
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and move[1] in ['bed']:
            #display a helpful message
            print('Comfy ' + move[1] + '.  Enjoy your rest !')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1])

    #if the user wants to 'read'
    if move[0] == 'read' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to drink
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and move[1] in ['bible']:
            #display a useful message
            print('Read your ' + move[1] + ' and pray everyday and you will grow')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '.  Forget to pray and you will shrink')

# if the user wants to play a riddle, 
# check for items, and call the riddle function to test their knowledge
    if move[0] == 'play' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and move[1] in ['riddle']:
            # call riddle function here
            riddle() 
        # if there's no item in the room or the item doesn't match
        else:
            print("Can\'t get " + move[1])

# Define other ways a player can win
    if currentRoom == 'Garden' and 'fruit' in inventory and 'key' in inventory:
        print("")
        print('YOU WIN!!!, The key to life is to eat lots of Fruits and Veges.')
        break
