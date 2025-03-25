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

#initialize variables for new game
dungeon = []
for i in range(1, 53):
   dungeon.append(i) #ace-through-king of hearts, diamonds, spades, clubs
for i in [1,11,12,13,14,24,25,26]:
    dungeon.remove(i) # remove the ace and face cards from hearts and diamonds
random.shuffle(dungeon)
health = 20
weapon = 0
can_flee = True

room = []
for i in range(0, 4):
    room.append(dungeon[0])
    dungeon.pop(0)

print("In this room, are the following objects:")
i = 1
for j in room:
    print(str(i) + ") " + card_name(j))
    i += 1

print("Would you like to engage with an object (1-4) or L)eave the room?")
while True:
    response = input()
    try:
        response = int(response)
    except:
        if  lower(response) == 'l':
            #tryleaveroom
            break
        else:
            print("Please enter a number or \"L\".")
            continue
    if (response < 1 or response > length(room)):
        print("Please enter a valid object still in the room.")
        continue
    else:
        #tryinteractobject

# loop until 1 object left in room
# loop until health <= 0 or dungeon and room are empty
# assign player score




