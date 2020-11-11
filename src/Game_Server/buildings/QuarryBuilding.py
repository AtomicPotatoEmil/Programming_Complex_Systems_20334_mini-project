import time
from Game_Server.Economy import *

class QuarryBuilding:
    def __init__(self):
        super.__init__()
        self.economy = Economy()
        pass

    def construction(self):
        print("You are building a quarry")
        time.sleep(6)
        print("You have built a quarry")
        self.economy.economy_stone_income(2)