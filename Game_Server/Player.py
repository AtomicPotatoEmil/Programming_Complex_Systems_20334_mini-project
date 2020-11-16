class Player:

    def __init__(self):
        self.name = None
        self.kingdom_name = None
        self.steady_income = 10
        self.population = 6
        self.housings = 2
        self.lumberyard_build = False
        self.quarry_build = False
        self.bank_build = False

    def your_info(self, socket_object, format):
        socket_object.send(f"\n Your name is {self.name} and your kingdom is called {self.kingdom_name} \n".encode(format))
