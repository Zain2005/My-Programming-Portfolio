import time
import random
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.08)

print('''
 ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO
       ::::::;       ;          OOOOO
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
''')

from random import *
import random

health = 50
Ihealth = 50
points = 0
Opoints = 0
you = {"d1": 10 , "d2": 15 , "d3": 20 , "d4": 40}

ranNum = randint(1,3)
ranHope = randint(1,3)
choicea = ["left", "right"]
choiceb = ["red","blue","green","black"]
choicee = ["blue"  , "yellow"]              #use .lowercase fonction
choicef = ["diamond" , "gold"]
choiceg = ["rock" , "paper" , "scissors"]
choiceh = ["big" , "small" , "large" , "slim" , "wooden"]
a = random.choice(choicea)
b = random.choice(choiceb)
c = random.choice(choiceb)
d = random.choice(choiceb)
e = random.choice(choicee)
f = random.choice(choicef)
h = random.choice(choiceh)
h1 = random.choice(choiceh)
h2 = random.choice(choiceh)

# Stage 1
print_slow("Welcome to the dungeons of hell. Here you may find the treasure you are looking for but you will most likely die\n")
entry = input("Are you sure you would like to enter ? There is no turning back \n")
if entry == "y" or entry == "Y" or entry == "yes" or entry == "Yes":
    where = input("Would you like to enter the dungeon from the right or the left \n")
    if where == a:
        print_slow("You are on the right track for now\n")
        print_slow("You can see a a door in-front of you. The only way to get there is to swim over the pit of water that seperates you from the door\n")
        swim = input("Will you 'swim' over, 'wait' or 'climb' the side walls to get to the door\n")
        if swim == "swim":
            print_slow("You were crushed and eaten alive by a shark waiting under the water\n")
            sys.exit()
        elif swim == "wait":
            print_slow("You have made the right decision to wait, the water is receding and your path to the door is clear\n")
        else:
            print_slow("You have decided to climb, however you widely overestimated your grip strength and fell in to the water\n")
            num = input("choose a number between 1 and 3, only fait can decide if you will survive \n")
            if num == ranNum:
                print_slow("Somehow you managed to pick yourself back up and climb to the door before sinking deep into the water\n")
            else:
                print_slow("You were unable to attract god's sympathy, instead you sunk deep into the water and died a slow painfull death\n")
                sys.exit()
    else:
        print_slow(f"you went {where} into the dangerous daniels warehouse and he killed you\n")
        sys.exit()
else:
    print("get lost wimp")
    sys.exit()

# Stage 2
print_slow("\nYou have passed the door, and with it an important milestone in your travels.\nHowever another four coloured doors await you. Pick your colour\n")
fourDoors = input("red,blue,green,black \n")
if fourDoors == b:
    print_slow("You have yet again picked the fastest and safest route to the end. The future is looking bright for you.\n ")
elif fourDoors == c:
    print_slow("Your luck ends here looser. As you walk through the door you fall into a hole so deep that every bone in your body is crushed to smitherins as you hit the floor \n")
    sys.exit()
elif fourDoors == d:
    print_slow("As you walk through this door a wise old man awaits you. A challenge awaits you before you can asure your survival\n")
    print_slow("To pass the old man you must answer his riddle: 'How many months of the year have 28 days?'\n")
    riddle = input("Answer the riddle with a number or press 's' to skip to another riddle\n ")
    if riddle == "12":
        print_slow("Good, you're not as dumb as i thought.\n As you pass the old man to continue your quest he hands you a health potion that you will be able to use later in your travels\n")
        health += 10
    elif riddle == "s":
        riddle2 = input("I have a tail and a head, but no body. What am I?\n ")
        if riddle2 == "A coin" or riddle2 == "a coin" or riddle2 == "coin" or riddle2 == "Coin":
            print_slow("Good, you're not as dumb as i thought.\n As you pass the old man to continue your quest he hands you a health potion that you will be able to use later in your travels\n")
        else:
            print_slow("Not only did you skip the first riddle but you also failed the second.You don't deserve the treasure")
            print_slow ("Without even telling you if you answered correctly the old wise man pulls out a sword and plunges it down your stomach \nthen spits on your face and leaves you to bleed slowly to death\n")
            sys.exit()
    else:
        print_slow("You failed a pre-school level riddle you dumb schmuck. You don't deserve the treasure")
        print_slow("Without even telling you if you answered correctly the old wise man pulls out a sword and plunges it down your stomack \nthen spits on your face and leaves you to bleed slowly to death\n")
        sys.exit()
else:
    choicea = ["left", "right"]
    a = random.choice(choicea)
    ranNum = randint(1, 3)
    choiceb = ["red", "blue", "green", "black"]
    b = random.choice(choiceb)
    c = random.choice(choiceb)
    d = random.choice(choiceb)
    print_slow("The door you have opened has led you to a fate worse than death.\nThis door has led you right back to the start of the dungeon....\n")
    print_slow("Welcome back to the start of the dungeons of hell.\nBe warned the answers could or could not be the same as your previous path\n")
    entry = input("Are you sure you would like to enter ? There is no turning back \n")
    if entry == "y" or entry == "Y" or entry == "yes" or entry == "Yes":
        where = input("Would you like to enter the dungeon from the right or the left \n")
        if where == a:
            print("You are on the right track for now")
            print("You can see a a door in-front of you. The only way to get there is to swim over the pit of water that seperates you from the door")
            swim = input("Will you 'swim' over, 'wait' or 'climb' the side walls to get to the door \n")
            if swim == "swim":
                print("You were crushed and eaten alive by a shark waiting under the water")
                sys.exit()
            elif swim == "wait":
                print("You have made the right decision to wait, the water is receding and you path to the door is clear")
            else:
                print("You have decided to climb, however you widely overestimated your grip strength and fell in to the water")
                num = input("choose a number between 1 and 4, only fait can decide if you will survive \n")
                if num == ranNum:
                    print("Somehow you managed to pick yourself back up and climb to the door before sinking deep into the water")
                else:
                    print("You were unable to attract god's sympathy, instead you sunk deep into the water and died a slow painfull death")
                    sys.exit()
        else:
            print(f"you went {where} into the dangerous daniels warehouse and he killed you")
            sys.exit()
    else:
        print("get lost wimp")
        sys.exit()
    print_slow("\nYou have passed the door, and with it an important milestone in your travels.\nHowever another four coloured doors await you. Pick your colour\n")
    fourDoors = input("red,blue,green,black \n")
    if fourDoors == b:
        print_slow("You have yet again picked the fastest and safest route to the end. The future is looking bright for you.\n ")
    elif fourDoors == c:
        print_slow("Your luck ends here looser. As you walk through the door you fall into a hole so deep that every bone in your body is crushed to smitherins as you hit the floor \n")
        sys.exit()
    elif fourDoors == d:
        print_slow("As you walk through this door a wise old man awaits you. A challenge awaits you before you can asure your survival\n")
        print_slow("To pass the old man you must answer his riddle: 'How many months of the year have 28 days?'\n")
        riddle = input("Answer the riddle with a number or press 's' to skip to another riddle\n ")
        if riddle == "12":
            print_slow("Good, you're not as dumb as i thought.\n As you pass the old man to continue your quest he hands you a health potion that you will be able to use later in your travels\n")
            health += 10
        elif riddle == "s":
            riddle2 = input("I have a tail and a head, but no body. What am I?\n ")
            if riddle2 == "A coin" or riddle2 == "a coin" or riddle2 == "coin" or riddle2 == "Coin":
                print_slow("Good, you're not as dumb as i thought.\n As you pass the old man to continue your quest he hands you a health potion that you will be able to use later in your travels\n")
            else:
                print_slow("Not only did you skip the first riddle but you also failed the second.You don't deserve the treasure\n")
                print_slow("Without even telling you if you answered correctly the old wise man pulls out a sword and plunges it down your stomack \nthen spits on your face and leaves you to bleed slowly to death\n")
                sys.exit()
        else:
            print_slow("You failed a pre-school level riddle you dumb schmuck. You don't deserve the treasure\n")
            print_slow("Without even telling you if you answered correctly the old wise man pulls out a sword and plunges it down your stomack \nthen spits on your face and leaves you to bleed slowly to death\n")
            sys.exit()
    else:
        print_slow("You're bad. You picked the same door as las time. This time instead of restarting the dungeon from the start you plunge your fist down your throat pull out your heart and die a painfull death")
        sys.exit()

# Stage 3
print_slow("\nYou are entering the final stages of your Quest. Good job\n")
print_slow("Somehow you are still alive. However, that will most likely change very soon\n")
print_slow("You are now met with the choice of a trap door above you and a trap door below you to continue ahead.\n")
print_slow("On the trap door above you can hear the grunting of a wild beast.\nWhereas on the trap door below you are met with a deathening silence\n")
upDown = input("Do you go 'up' or 'down'.\n")
if upDown == "up":
    print_slow("Just as predicted, once you climbed the sealing trap door you are met with a disgustingly ugly beast named ibi the piggy.\nIt is clear you will need to battle your way through  to continue your excursion\n")
    if health > 50:
        print_slow("You start with 50 health. However you think that now is a good time to drink the potion given to you by the wise old man\n")
        print_slow("You drink the potion and it give you 10 extra health. You now have 60 health\n")
    else:
        print_slow("You start with 50 health. Be careful once you reach zero you will die\n")
    print_slow("To defeat your enemy you will need to pick a number between one and four until you have extermenated ibi\n")
    print('''Your stats:\n
              xxx | attack 1 | attack 2 | attack 3 | attack 4 |
           damage |    10    |     15   |    20    |    40    |
           chance |    2/3   |     2/4  |    1/3   |    1/5   |
           \n''')
    while True:
        chance = {"c1": randint(1, 3), "c2": randint(1, 4), "c3": randint(1, 3), "c4": randint(1, 5)}
        yourHit = input("1,2,3 or 4 ")
        if yourHit == "1" and chance["c1"] == 1:
            print_slow("You missed your hit\n")
        elif yourHit == "1" and chance["c1"] != 1:
            Ihealth -= 10
            print_slow("You did 10 damage to ibi\n")
        #
        elif yourHit == "2" and chance["c2"] > 2:
            print_slow("You missed your hit\n")
        elif yourHit == "2" and chance["c2"] <= 2:
            Ihealth -= 15
            print_slow("You did 15 damage to ibi\n")
        #
        elif yourHit == "3" and chance["c3"] == 1:
            Ihealth -= 20
            print_slow("You did 20 damage to ibi\n")
        elif yourHit == "3" and chance["c3"] != 1:
            print_slow("You missed your hit\n")
        #
        elif yourHit == "4" and chance["c4"] == 1:
            Ihealth -= 40
            print_slow("You did 40 damage to ibi\n")
        elif yourHit == "4" and chance["c4"] != 1:
            print_slow("You missed your hit\n")
        else:
            print_slow("You missed your hit\n")
        if Ihealth <= 0:
            print_slow(
                f"You finish ibi off with a last hit and run past his unconscious body with your {health} health\n")
            break
        ##
        chance = {"c1": randint(1, 3), "c2": randint(1, 4), "c3": randint(1, 3), "c4": randint(1, 5)}
        hance = randint(1, 6)
        if hance <= 2:
            if chance["c1"] == 1:
                print_slow("ibi was to slow and missed his hit\n")
            else:
                health -= 10
                print_slow("ibi farted on your face and did 10 damage\n")
        elif hance <= 4:
            if chance["c2"] > 2:
                print_slow("You were to fast, ibi missed his hit\n")
            else:
                health -= 15
                print_slow("ibi kicked your nuts and did 15 damage\n")
        elif hance == 5:
            if chance["c3"] == 1:
                health -= 20
                print_slow("ibi stomped your face and did 20 damage\n")
            else:
                print_slow("ibi missed like a looser\n")
        elif hance == 6:
            if chance["c4"] == 1:
                health -= 40
                print_slow("ibi hit you hard for 40 damage !!\n")
            else:
                print_slow("Nice! you dodged ibi's shot\n")
        if health <= 0:
            print_slow("ibi deals a last hit and knocks you out, bites your head of and spits out your brains and stomps on you until you become a puddle of blood")
            sys.exit()
        print_slow(f"YOUR HEALTH IS: {health}\n")
        print_slow(f"IBI's HEALTH IS: {Ihealth}\n")
else:
    print_slow("As you jump down the trap door you realise you are falling to your death, however it seems that there is water at the bottom to break your fall\n")
    falling = input("Press 'f' to continue falling or press 'g' to try and grab onto the wall and break your fall")
    if falling == "f":
        print_slow("Bad luck the water ended being frozen solid and crushed your feet once you landed\n")
        print_slow("You are now limping around the ground trying to survive the cold ice under your crushed feet as blood is leaking out of all parts of your body\n")
        hope = input("But all hope is not lost ! pick a number between 1 and 3 to try and stay alive\n")
        if hope  == ranHope:
            print_slow("Somehow you managed grab two pebbles of the wall to light yourself a fire and survive the cold ice\n")
            print_slow("You stay alive...For now")
        else:
            print_slow("Your luck has officially ran out you die a painful death as you are to cold to move and the blood from crushed legs leaks out and swallows you up like a puddle.")
            sys.exit()
    else:
        print_slow("you are now  hanging with one hand on to the wall. If you let go you will fall tou your death\n")
        stranded = input("You seem to be stranded on the wall. You can either 'call' for help, 'wait' or test you luck and 'fall'\n")
        if stranded == "fall" or stranded == "Fall":
            print_slow("Your extremely dumb. You died a fast painful death as every bone in your body is shattered by the cold floor\n")
            sys.exit()
        elif stranded == "call" or stranded == "Call":
            print_slow("As you call for help you attract the beast from the trapdoor upstairs: ibi.\nIt is clear you will need to battle your way through to continue your excursion\n")
            if health > 50:
                print_slow("You start with 50 health. However you think that now is a good time to drink the potion given to you by the wise old man\n")
                print_slow("You drink the potion and it give you 10 extra health. You now have 60 health\n")
            else:
                print_slow("You start with 50 health. Be careful once you reach zero you will die\n")
            print_slow("To defeat your enemy you will need to pick a number between one and four until you have exterminated ibi\n")
            print('''Your stats:\n
                      xxx | attack 1 | attack 2 | attack 3 | attack 4 |
                   damage |    10    |     15   |    20    |    40    |
                   chance |    2/3   |     2/4  |    1/3   |    1/5   |
                   \n''')
            while True:
                chance = {"c1": randint(1, 3), "c2": randint(1, 4), "c3": randint(1, 3), "c4": randint(1, 5)}
                yourHit = input("1,2,3 or 4 ")
                if yourHit == "1" and chance["c1"] == 1:
                    print_slow("You missed your hit\n")
                elif yourHit == "1" and chance["c1"] != 1:
                    Ihealth -= 10
                    print_slow("You did 10 damage to ibi\n")
                #
                elif yourHit == "2" and chance["c2"] > 2:
                    print_slow("You missed your hit\n")
                elif yourHit == "2" and chance["c2"] <= 2:
                    Ihealth -= 15
                    print_slow("You did 15 damage to ibi\n")
                #
                elif yourHit == "3" and chance["c3"] == 1:
                    Ihealth -= 20
                    print_slow("You did 20 damage to ibi\n")
                elif yourHit == "3" and chance["c3"] != 1:
                    print_slow("You missed your hit\n")
                #
                elif yourHit == "4" and chance["c4"] == 1:
                    Ihealth -= 40
                    print_slow("You did 40 damage to ibi\n")
                elif yourHit == "4" and chance["c4"] != 1:
                    print_slow("You missed your hit\n")
                else:
                    print_slow("You missed your hit\n")
                if Ihealth <= 0:
                    print_slow(
                        f"You finish ibi off with a last hit and run past his unconscious body with your {health} health\n")
                    break
                ##
                chance = {"c1": randint(1, 3), "c2": randint(1, 4), "c3": randint(1, 3), "c4": randint(1, 5)}
                hance = randint(1, 6)
                if hance <= 2:
                    if chance["c1"] == 1:
                        print_slow("ibi was to slow and missed his hit\n")
                    else:
                        health -= 10
                        print_slow("ibi farted on your face and did 10 damage\n")
                elif hance <= 4:
                    if chance["c2"] > 2:
                        print_slow("You were to fast, ibi missed his hit\n")
                    else:
                        health -= 15
                        print_slow("ibi kicked your nuts and did 15 damage\n")
                elif hance == 5:
                    if chance["c3"] == 1:
                        health -= 20
                        print_slow("ibi stomped your face and did 20 damage\n")
                    else:
                        print_slow("ibi missed like a looser\n")
                elif hance == 6:
                    if chance["c4"] == 1:
                        health -= 40
                        print_slow("ibi hit you hard for 40 damage !!\n")
                    else:
                        print_slow("Nice! you dodged ibi's shot\n")
                if health <= 0:
                    print_slow("ibi deals a last hit and knocks you out, bites your head of and spits out your brains and stomps on you until you become a puddle of blood\n")
                    sys.exit()
                print_slow(f"YOUR HEALTH IS: {health}\n")
                print_slow(f"IBI's HEALTH IS: {Ihealth}\n")
        else:
            print("")

## stage 4
print_slow("As you wait hanging on the wall a rope drops down.You climb up the rope and meet an old wise man at the top\n")
print_slow("The man leads you to a room and tells you that you must choose between three potions to pass him.\nThe first potion is blue, the second potion is red and the last potion is yellow\n")
flask = input("What colour do you choose ? ")
if flask == "e":
    health -= "10"
    if health <= 0:
        print_slow("This potion has taken away 10 of your health which means that you have now lost all your health because you were on low health after battling ibi\n")
        print_slow("Unfortunately you are dead")
        sys.exit()
    else:
        print_slow(f"The flask has taken away 10 of your health but the old man grants you safe passage to continue the dungeon. You now have {health}\n")
elif flask == "red":
    print_slow("The red potion was a poison. You stare at the old man whilst coughing up blood. After a minute you start chocking on your own blood and die a sad death\n")
    sys.exit()
else:
    print_slow("This potion has teleported you into a room with one door. There are two keys in-front of you\n")
    key = input("Do you pick the 'diamond' key to unlock the door or the 'gold' key")
    if key == f:
        print_slow("You picked the correct key which has led you back to the dungeon. You have nearly completed your quest\n")
    else:
        print_slow("You picked the wrong key. As you step through the door a giant tarantula appears and bites of your head and stuffs it down your bum")
        sys.exit()
## Stage 5
print_slow("In the next room you go into you are met by an ogre. To get past him you must beat him in a game of rock,paper, scissors.\nFirst to three points\n")
while True:
    g = random.choice(choiceg)
    rps = input("Do you choose rock, paper or scissors ? ")
    if rps == "rock":
        if g == "rock":
            print_slow("The ogre chose rock. It's a draw\n")
        elif g == "paper":
            Opoints += 1
            print_slow("The ogre chose paper. He gets a point\n")
        else:
            points += 1
            print_slow("The ogre chose scissors. you get a point\n")
    elif rps == "scissors":
        if g == "rock":
            Opoints += 1
            print_slow("The ogre chose rock. He gets a point\n")
        elif g == "paper":
            points += 1
            print_slow("The ogre chose paper. You get a point\n")
        else:
            print_slow("The ogre chose scissors. It's a draw\n")
    elif rps == "paper":
        if g == "rock":
            points += 1
            print_slow("The ogre chose rock. You get a point\n")
        elif g == "paper":
            print_slow("The ogre chose paper. It's a draw\n")
        else:
            Opoints += 1
            print_slow("The ogre chose scissors. He gets a point\n")
    print_slow(f"YOU HAVE {points} POINTS\n")
    print_slow(f"THE OGRE HAS {Opoints} POINTS\n")
    if points == 3:
        print_slow("You have reached three points and therefore defeated the ogre. You are granted safe passage to continue\n")
    if Opoints == 3:
        print_slow("The ogre has reached three points and therefore has defeated you. Takes a rock and bashed your head until you start tasting your brain fluid\nYou then die a painful death as the ogre eats your ding dong")
        sys.exit()
##Final stage
print_slow("You have reached the final stage of your quest\n")
print_slow("In front of you there are five doors a small one and a big one, a large one, a slim one and a wooden one\n")
door = input("Do you chose 'big' , 'small' , 'large' , 'slim' or 'wooden' ?")
if door == h or door == h1:
    print_slow("The door you have opened leads you safely into the final room\n")
elif door == h2:
    health -= 25
    if health <= 0:
        print_slow("This door has removed twenty of your health. Because of you previous battles you were unable to survive.\nYou nearly made it but insteaad you died !\n")
        sys.exit()
    else:
        print_slow(f"The door took away twenty of your health but somehow you ar still alive and ready to walk into the final room with your {health} health\n")
else:
    print_slow("As you open the door you can see the treasure in-front of you but a bomb blows up from under your feet and shredds you into a thousand pieces\n")
    sys.exit()
##Final room
print_slow("You have reached the final stage of the dungeon. You can see two treasure chests ")
last_choice = input("Do you take the one on the right or the one on the left")
a = random.choice(choicea)
if last_choice == "a":
    print_slow("YOU WON!!!! You have left the dungeon safely with the treasure and will be rich forever")
    import test.py
else:
    print_slow("You came this far but your last decision was the wrong one. You were sucked in by the chest and you will be trapped in there burning for the rest of eternity")
    import image2.py
