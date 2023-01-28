#Implements the game data and logic.
import Role1
import Role2

def start_game():
    print("WELCOME TO THE TREASURE HUNT")
    print("YOUR GOAL IS TO FIND THE ONE PIECE")

#Choose your role
while True:
    print("Choose your role: (Priate/Warrior)")
    role = input().strip().capitalize()
    if role == "priate":
        player = Priate()
        break
    elif role == "warrior":
        player = Warrior()
        break
    else:
        print("Invalid role choice.(Priate/Warrior)")

while True:
    print("Which direction would you like to go? (East, West, North, South)")
    direction = input().strip().capitalize()


    #Movement
    if direction == "East":
        print("You have moved towards the East")
    elif direction == "South":
         print("You have moved towards the South")
    elif direction == "West":
         print("You have moved towards the West")
    elif direction == "North":
         print("You have moved towards the North")
    else:
        print("Invalid Input You have moved towards the (East, West, North, South")

    #BATTLE

    if fight_guards:
    

