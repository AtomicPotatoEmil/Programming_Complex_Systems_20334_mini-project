import time
from Game_Server.Economy import *

class MineBuilding:
    def __init__(self):
        super.__init__()
        self.economy = Economy()
        pass

    def construction(self):
        print("You are building a mine")
        time.sleep(8)
        print("You have built a mine")
        self.economy.economy_iron_income(2)
