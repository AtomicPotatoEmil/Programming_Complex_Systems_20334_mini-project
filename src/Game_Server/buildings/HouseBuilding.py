import time
from Game_Server.Economy import *

class HouseBuilding:
    def __init__(self):
        super.__init__()
        self.economy = Economy()
        pass

    def construction(self):
        print("You are building a house")
        time.sleep(2)
        print("You have built a house")
        self.economy.economy_gold_income(3)



