import random

class Player2:
    def roledice (self):
        prob = random.randrange(1,7)
        prob2 = random.randrange(1,7)
        prob3 = random.randrange(1,7)
        print ("PLAYER 2:",prob,prob2,prob3)
        sum2 = prob + prob2 + prob3
        if sum2 == 10:
            print("Winner")
        else:
            print("You Lose")

