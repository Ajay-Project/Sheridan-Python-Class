import random

class Player1:
    def dice (self):
        prob =random.randrange(1,7)
        prob2 =random.randrange(1,7)
        prob3 =random.randrange(1,7)
        print ("PLAYER 1:",prob,prob2,prob3)
        sum1 = prob + prob2 + prob3
        if sum1 == 10:
            print("Winner")
        else:
            print("You Lose")
