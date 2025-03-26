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
    elif card % 13 == 0:
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
    print("\nIn this room, are the following objects:")
    i = 1
    for j in room:
        print(str(i) + ") " + card_name(j))
        i += 1
    #print current health and weapon
    print("Your current health is " + str(health) + " out of a maximum 20.")
    print(weapon_status())

def weapon_status():
    if weapon == 0:
        return("You are currently bare-handed.")
    elif weapon_degradation == 0:
        return("You possess a brand-new level " + str(weapon) + " weapon.")
    else:
        return("You have a used level " + str(weapon) + " weapon that can fight an enemy up to level " + str(weapon_degradation) + ".")

def interact_object(chosen_card):
    global health, has_drank_potion, weapon, weapon_degradation
    if chosen_card < 14: # if heart, health potion:
        if has_drank_potion: 
            print("You've already used a potion in this chamber!  Sure you want to discard the " + str(chosen_card) + " of Hearts?")
            response = input()
            if str.lower(response) in ['yes', 'y']:
                print("You have no choice but to pour out this potion.")
                return True
            else:
                print("You change your mind.")
                return False
        else: 
            print ("You drink the level " + str(chosen_card) + " health potion.")
            health_gained = min(chosen_card, 20 - health)
            health += health_gained
            if health == 20:
                print("You're back to a maximum 20 health!")
            else:
                print("You regain " + str(health_gained) + " life points!")
            has_drank_potion = True
            return True
    elif chosen_card < 27: # if diamond, gain weapon
        if weapon > 0:
            print("You discard your level " + str(weapon) + " weapon and equip the " + str(chosen_card - 13) + "of Diamonds.")
        else:
            print("You arm yourself with a " + str(chosen_card - 13) + " of Diamonds and ready yourself to fight!")
        weapon = chosen_card - 13
        weapon_degradation = 0
        return True
    else: # if club/spade, fight
        monster_level = chosen_card % 13
        if monster_level < 2:
            monster_level += 13
        if weapon == 0:
            print("You bravely battle the foe unarmed, suffering " + str(monster_level) + " damage!")
            health -= monster_level
            return True
        elif weapon_degradation > 0 and weapon_degradation < monster_level:
            print("Your weapon is too damaged to harm this foe!  Do you want to fight it barehanded?")
            response = input()
            if str.lower(response) in ['yes', 'y']:
                print("With a battle cry, you use not your sword but your fists to ambush the foe, taking " + str(monster_level) + " damage!")
                health -= monster_level
                return True
            else:
                print("You reconsider the matchup.")
                return False
        else:
            print("Would you like to use your level " + str(weapon) + " weapon on the enemy?")
            response = input()
            if response in ['yes', 'y']:
                #battle enemy
                if weapon >= monster_level:
                    print("You slice the monster down with ease!")
                else:
                    damage = monster_level - weapon
                    print("You defeat the enemy in a grueling fight, taking " + str(damage) + " damage.")
                    health -= damage
                #damage weapon
                weapon_degradation = monster_level - 1
                if weapon_degradation < 2:
                    print("Your weapon shatters upon defeating the foe!  You are now unarmed.")
                    weapon = 0
                    weapon_degradation = 0
                else:
                    print("Your weapon, battered by the stress of combat, can now be used on monsters up to level " + str(weapon_degradation) + ".")
                return True
            else:
                print("In that case, would you like to battle this level " + str(monster_level) + " monster unarmed?")
                if response in ['yes,' 'y']:
                    print ("Spirits blazing, you challenge the foe to a fierce fist-to-fist faceoff!  You take " + monster_level + " damage.")
                    health -= monster_level
                    return True
                else:
                    print ("You back up to regroup, pondering your strategy.")
                    return False
    return True

def flee_room():
    global has_fled, has_drank_potion
    print("You exit this room before anything or anyone hears you.")
    random.shuffle(room)
    while len(room) > 0:
        dungeon.append(room[0])
        room.pop(0)
    while len(room) < 4:
        room.append(dungeon[0])
        dungeon.pop(0)
    has_fled = True
    has_drank_potion = False

def next_room():
    global has_fled, has_drank_potion
    print("You enter the next room, bringing " + card_name(room[0]) + " with you.")
    while(len(dungeon) > 0 and len(room) < 4):
        room.append(dungeon[0])
        dungeon.pop(0)
    has_fled = False
    has_drank_potion = False

def game_over():
    print("What a shame, you have been brought to " + str(health) + " health and can not continue your quest.")
    #TODO define score

def rules_and_credits():
    print('''In Scoundrel, your goal is to survive through a deck of cards (the dungeon)
full of monsters (clubs and spades), health potions (hearts), and equippable weapons
(diamonds.)  The game uses a 52-card deck, minus the red Ace and red face cards.

Each room consists of 4 cards.  As you enter a room, you may choose to flee - if you
leave the room, the four cards will be shuffled together and put back at the bottom
of the dungeon.  You may not flee two rooms in a row.

If you choose to brave a room, you must select the cards to interact with.  A diamond
is a WEAPON, and the higher the number the stronger.  As you use a weapon, it grows
damaged, and can only be used on monsters of a lower level than the last one you fought
with it.  When you pick up a new weapon, it has no damage, but you must discard the
previous weapon, even if the new weapon is less powerful.

A heart is a HEALTH POTION.  You may use one health potion per room, gaining the number
of health equal to its number, to a MAXIMUM of 20 health.  If you try to use a second
health potion in the same room, it will POUR OUT the potion, discarding it entirely.
(press enter for the rest of the instructions)''')
    input()
    print('''A club or spade is a MONSTER.  A monster has level equal to its number - a Jack is level
11, a Queen 12, a King 13, and an Ace a mighty 14.  If you fight a monster barehanded,
you will defeat it, taking damage equal to its level.  If you choose to fight a monster
with your weapon, you will take no damage if the weapon is at least as high leveled as
the monster.  If the monster is higher than the weapon, you will take the difference
in levels of damage.  Even if you have a weapon, you MAY CHOOSE to fight barehanded.

Once three cards have been cleared, you enter a new room.  The remaining card comes with
you, along with the top three cards drawn from the Dungeon.

Run out of health or clear the dungeon to finish the game!  If you fail to reach the end
with health left, your score will be the total amount of levels of monsters left in the
room and dungeon.  If you succeed, your score will be your health.  Plus, if you finish
the last monster, and leave one health potion in the room, you add that potion to your
score.

This game was created August 15, 2011 by Zach Gage and Kurt Bieg, and posted to the
website stfj.net.  This adaptation was made by P. Willie Eaton on March 2025.  No
claim to ownership of this game is made by Willie - although the rules are published
freely online, I was unable to determine the license of this game, so presumably
all rights are reserved to Gage and Bieg.
(press enter to begin the game)''')
    input()

# introduce game
print("Welcome to Scoundrel!  Would you like to see the rules and credits?")
response = input()
if str.lower(response) in ['yes', 'y']:
    rules_and_credits()
print('''\nYou step into the dungeon, in search of treasure and fame.  Armed only with
your wits, you prepare to brave the darkness and make your mark, doing whatever
it takes, the mark of a true Scoundrel!''')

# introduce global variables and initialize variables for new game
dungeon = []
for i in range(1, 53):
   dungeon.append(i) # ace-through-king of hearts, diamonds, spades, clubs
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

while True: #room loop
    while True: #individual card loop
        room_description()
        print("Would you like to engage with an object (1-4) or L)eave the room?")
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
                room.pop(response-1)
                break
            else:
                continue
    if health <= 0:
        game_over()
        break
    if len(room) < 2 and len(dungeon) > 0:
        next_room() # try to generate a new room
    if len(room) == 0 and len(dungeon) == 0:
        break #TODO win game



