import time
class Economy:

    def __init__(self):
        self.stone_inc = 0
        self.wood_inc = 0
        self.gold_inc = 1
        self.iron_inc = 0
        self.houseUpkeep = 0
        self.millUpkeep = 0
        self.quarryUpkeep = 0
        self.mineUpkeep = 0
        self.totalUpkeep = 0

    def economy_gold_income(self, gold_Change):
        self.gold_inc += gold_Change - self.houseUpkeep

        return self.gold_inc

    def economy_wood_income(self, wood_Change):
        self.wood_inc += wood_Change - self.millUpkeep

        return self.wood_inc

    def economy_stone_income(self, stone_Change):
        self.stone_inc += stone_Change - self.quarryUpkeep

        return self.stone_inc

    def economy_iron_income (self, iron_Change):
        self.iron_inc += iron_Change - self.mineUpkeep

        return self.iron_inc

    def upkeep(self, housenr, millnr, quarrynr, minenr):
        self.housenr = housenr
        self.millnr = millnr
        self.quarrynr = quarrynr
        self.minenr = minenr
        self.houseUpkeep = self.housenr * 1
        self.millUpkeep = self.millnr * 2
        self.quarryUpkeep = self.quarrynr * 3
        self.mineUpkeep = self.minenr * 4
        self.totalUpkeep = self.houseUpkeep + self.millUpkeep + self.quarryUpkeep + self.mineUpkeep

        print(self.houseUpkeep)
        print(self.millUpkeep)
        print(self.quarryUpkeep)
        print(self.mineUpkeep)
        print(self.totalUpkeep)
        return self.totalUpkeep

    def fullEconomy(self):
        time.sleep(5)
        print("you gained " + str(self.economy_gold_income(6)) + " gold")
        print("you gained " + str(self.economy_wood_income(4)) + " wood")
        print("you gained " + str(self.economy_stone_income(1)) + " stone")