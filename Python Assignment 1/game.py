#implements the game data and logic.
import role1
import role2

def start_game():
    print("WELCOME TO THE HUNT FOR THE ONE PIECE")
    print("THE ONE PIECE TREASURE IS THE GIFT OF THE UNKNOW ")
    print("THE AIM TO THE HAVE THE DESIRE TO CONTINUE AFTER FAILURE")

    #Role Selection
    print("Pirate")
    print("Warrior")
    role = input().capitalize()

    puzzle1_completed = False
    puzzle2_completed = False
    puzzle3_completed = False
    puzzle4_completed = False

#Puzzle 1
    print("Puzzle 1: The Game of Truth")
    if role == "Pirate":
        puzzle1_completed = role1.puzzle1()
    else:
        puzzle1_completed =role2.puzzle1()


#Puzzle 2
    print("Puzzle 2: The Game of Intelligence")
    if role == "Pirate":
        puzzle2_completed = role1.puzzle2()
    else:
        puzzle2_completed =role2.puzzle2()


#Puzzle 3
    print("Puzzle 3: The Game of Awarness ")
    if role == "Pirate":
        puzzle3_completed = role1.puzzle3()
    else:
        puzzle3_completed =role2.puzzle3()



#Puzzle 4
    print("Puzzle 4: THE CHOICE BETWEEN OF DESIRE ")
    if role == "Pirate":
        puzzle4_completed = role1.puzzle4()
    else:
        puzzle4_completed =role2.puzzle4()

#Game Over Message
    if puzzle1_completed and puzzle2_completed and puzzle3_completed and puzzle4_completed:
        print("YOU HAVE COMPLETE THE SEARCH FOR ONE PIECE")
    else:
        print("Failed you need to do some self-reflection")


start_game()