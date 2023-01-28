#Implements the game data and logic.
import Role1
import Role2

def start_game():
    print("WELCOME TO THE TREASURE HUNT")
    print("YOUR GOAL IS TO FIND THE ONE PIECE")

#Chose your role
print("Choose your role: (priate/warrior)")
role = input().strip().capitalize()

while True:
    print("Which direction would you like to go? (East, West, North, South)")
    direction = input()

    #Movement
    if direction == "East":
        print("You have moved towards the east")
    elif direction == "South":
         print("You have moved towards the South")
    elif direction == "West":
         print("You have moved towards the West")
    else:
        print("Invalid Input You have moved towards the (East, West, North, South")


