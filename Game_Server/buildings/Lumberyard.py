class Lumberyard:

    def __init__(self):
        self.description = "\n This building produces wood. Wood is a great material to build other structures"
        self.wood_gain = 5

    def gain(self):
        return self.wood_gain