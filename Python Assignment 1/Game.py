#Implements the game data and logic.
import Role1
import Role2

def start_game():
    print("WELCOME TO THE TREASURE HUNT")
    print("YOUR GOAL IS TO FIND THE ONE PIECE")

#Choose your role
print("Choose your role: (Priate/Warrior)")
role = input().strip().capitalize()
    
while True:
    print("Which direction would you like to go? (East, West, North, South)")
    direction = input().strip().capitalize()

    #MOVEMENT
    
    if direction == "north":
        # Move player to new location
        print("You have moved north.")
    elif direction == "south":
        # Move player to new location
        print("You have moved south.")
    elif direction == "east":
        # Move player to new location
        print("You have moved east.")
    elif direction == "west":
        # Move player to new location
        print("You have moved west.")
    elif direction == "quit":
        # End game
        print("Thanks for playing!")
        break
    else:
        # Invalid input
        print("Invalid choice. Please try again.")
    
