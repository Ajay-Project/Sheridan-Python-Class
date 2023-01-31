#implements the data and logic associated with the second role Warrior

import random

def warrior_ability():
    strength = random.randint(1, 100)
    iq = random.randint(1, 130)
    stamina = random.randint(1, 100)

def puzzle1():
    answer=input("What is your role? ")
    if answer == "Warrior":
        print("Correct! The truth shallset you free")
        return True
    else:
        print("YOU LIAR!!!!")
        return False

def puzzle2():
    answer =  input("How many seas are there? ")
    if answer == "7":
        print("Correct! You're a smart one")
        return True
    else:
        print("Incorrect! Not So Smart")
        return False

def puzzle3():
    answer = int(input("How many times did you blink while playing this game? "))
    if answer  > 1 and answer < 20000000000000:
        print("Intersting that you got that correct")
        return True
    else:
        print("Be aware!!!!")
        return False

def puzzle4():
    answer= input("What was the aim of this game? ")
    if answer =="To find One Piece":
        print("Desire is the starting point of all achievement, not a hope, not a wish, but a keen pulsating desire which transcends everything. - Napoleon Hill")
        return True
    else:
        print("Think!!!!!!!!!!!!!!!!!!")
        return False