#implements the data and logic associated with the first role Pirate

import random

def pirate_ability():
    strength = random.randint(1, 100)
    iq = random.randint(1, 130)
    stamina = random.randint(1, 100)
    
def puzzle1():
    answer=input("What is your role? ")
    if answer == "Pirate":
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
    answer = input("How many times did you blink while playing this game? ")
    if answer == range(100):
        print("Intersting that you got that correct")
        return True
    else:
        print("Be aware!!!!")
        return False

def puzzle4():
    answer= input("What was the aim of this game? ")
    if answer == input("THE AIM TO THE HAVE THE DESIRE TO CONTINUE AFTER FAILURE"):
        print("Desire is the starting point of all achievement, not a hope, not a wish, but a keen pulsating desire which transcends everything. - Napoleon Hill")
        return True
    else:
        print("Think!!!!!!!!!!!!!!!!!!")