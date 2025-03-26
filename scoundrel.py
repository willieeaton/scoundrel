# scoundrel.py - attempt to implement the card-game roguelike Scoundrel in Python
import random

def card_name(card):
    name = "The "
    if card % 13 > 1 and card % 13 < 11:
        name += str(card % 13)
    elif card % 13 == 1:
        name += "Ace"
    elif card % 13 == 11:
        name += "Jack"
    elif card % 13 == 12:
        name += "Queen"
    elif card % 13 == 13:
        name += "King"
    name += " of "
    if card < 14:
        name += "Hearts - a health potion"
    elif card < 27:
        name += "Diamonds - a weapon"
    elif card < 40:
        name += "Spades - a monster"
    else:
        name += "Clubs - a monster"
    return name

def room_description():
    # give list of items in room
    print("In this room, are the following objects:")
    i = 1
    for j in room:
        print(str(i) + ") " + card_name(j))
        i += 1
    #TODO print current health and weapon

def interact_object(chosen_card):
    pass
    # TODO if heart, health potion:
        # if not used potion in room, gain health up to 20
        # if has used health or at full, confirm discard
    # TODO if diamond, gain weapon
    # TODO if club/spade, fight
        # if weapon and not degraded, offer weapon choice
        # game over if health hits under 1

def flee_room():
    print("You exit this room before anything or anyone hears you.")
    random.shuffle(room)
    while len(room) > 0:
        dungeon.append(room[0])
        room.pop(0)
    while len(room) < 4:
        room.append(dungeon[0])
        dungeon.pop(0)

def next_room():
    print("You enter the next room, bringing " + cardname(room[0]) + "with you.")
    while(len(dungeon) > 0 and len(room) < 4):
        room.append(dungeon[0])
        dungeon.pop(0)

# introduce global variables and initialize variables for new game
dungeon = []
for i in range(1, 53):
   dungeon.append(i) #ace-through-king of hearts, diamonds, spades, clubs
for i in [1,11,12,13,14,24,25,26]:
    dungeon.remove(i) # remove the ace and face cards from hearts and diamonds
random.shuffle(dungeon)
health = 20
weapon = 0
weapon_degradation = 0
has_fled = False
has_drank_potion = False
room = []
for i in range(0, 4):
    room.append(dungeon[0]) # get the four starter cards and remove from dungeon
    dungeon.pop(0)

# TODO help/credits/play menu

room_description() # display room info
print("Would you like to engage with an object (1-4) or L)eave the room?")

while True:
    response = input()
    try:
        response = int(response)
    except:
        if str.lower(response) == 'l':
            if (has_fled):
                print("You cannot flee, you fled the previous room!")
                continue
            else:
                flee_room()
                break
        else:
            print("Please enter a number or \"L\".")
            continue
    if (response < 1 or response > len(room)):
        print("Please enter a valid object still in the room.")
        continue
    else:
        if interact_object(room[response - 1]):
            break
        else:
            continue

# if 1 object left in room, 'new room' (pop on up to 3 more cards)
# loop until health <= 0 or dungeon and room are empty
# assign player score




