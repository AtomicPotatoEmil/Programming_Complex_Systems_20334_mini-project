import time
from Game_Server.Economy import *

class Building:

    def __init__(self):
        self.houses = 0
        self.mills = 0
        self.quarries = 0
        self.mines = 0

    def houseContruction(self, bank1):
        print("You are building a house")
        time.sleep(2)
        self.houses += bank1
        print("You have built a house")
        return self.houses

    def lumbermillConstruction(self, mill1):
        print("You are building a bank")
        time.sleep(4)
        self.mills += mill1
        print("You have built a lumbermill")
        return self.mills

    def quarryConstruction(self, quarry1):
        print("You are building a quarry")
        time.sleep(6)
        self.quarries += quarry1
        print("You have built a quarry")
        return self.quarries

    def mineConstruction(self, mine1):
        print("You are building a mine")
        time.sleep(8)
        self.mines += mine1
        print("You have built a mine")
        return self.mines



