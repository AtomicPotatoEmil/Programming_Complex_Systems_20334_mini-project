import time
from Game_Server.Economy import *

class LumbermillBuilding:
    def __init__(self):
        super.__init__()
        self.economy = Economy()
        pass

    def construction(self):
        print("You are building a bank")
        time.sleep(4)
        print("You have built a lumbermill")
        self.economy.economy_wood_income(2)