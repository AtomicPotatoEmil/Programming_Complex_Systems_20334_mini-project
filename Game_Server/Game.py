import threading
from SingleLinkedList import *
from Player import *
from buildings.Lumberyard import *
from buildings.Quarry import *
from buildings.Mine import *
from buildings.Bank import *
from buildings.TownHall import *

class Game:

    def __init__(self):
        self.at_the_start = True
        self.player = Player()
        self.buildings = SingleLinkedList()
        self.tools = SingleLinkedList()
        self.options = ["info", "build lumberyard", "build quarry", "build mine", "build bank", "build town hall"]


    def game(self, socket_object, format, command):

        if command == "info":
            self.show_options(socket_object, format)

        if command == "info me":
            self.player.your_info(socket_object, format)



        if command == "build lumberyard" and self.buildings.find_node("lumberyard") is False:
            self.options.append("info lumberyard")
            self.buildings.stack_value("lumberyard", Lumberyard())
            socket_object.send("\n You have build a lumberyard, a new option have been added \n".encode(format))
        elif command == "build lumberyard" and self.buildings.find_node("lumberyard"):
            socket_object.send("\n you have already build a Lumberyard try and build something else \n".encode(format))

        if command == "info lumberyard" and self.buildings.find_node("lumberyard"):
            socket_object.send(self.buildings.get_node("lumberyard").description.encode(format))
        elif command == "info lumberyard" and self.buildings.find_node("lumberyard") is False:
            socket_object.send("\n What lumberyard? \n".description.encode(format))


        if command == "build quarry" and self.buildings.find_node("lumberyard"):
            self.options.append("info quarry")
            self.options.append("build tools")
            self.buildings.stack_value("quarry", Quarry())
            socket_object.send("\n You have build a quarry, new options have been added \n".encode(format))
        elif command == "build quarry" and self.buildings.find_node("quarry") and self.buildings.find_node("lumberyard"):
            socket_object.send("\n you have already build a quarry try and build something else \n".encode(format))
        elif command == "build quarry" and self.buildings.find_node("quarry") is False and self.buildings.find_node("lumberyard") is False:
            socket_object.send("\n You don't have any wood to build the quarry \n".encode(format))
        elif command == "build quarry" and self.buildings.find_node("quarry"):
            socket_object.send("\n you have already build a quarry \n".encode(format))

        if command == "info quarry" and self.buildings.find_node("quarry"):
            socket_object.send(self.buildings.get_node("quarry").description.encode(format))
        elif command == "info quarry" and self.buildings.find_node("quarry") is False:
            socket_object.send("\n you haven't build a quarry yet \n".encode(format))


        if command == "build tools" and self.tools.find_node("mining tools") is False and self.buildings.find_node("quarry"):
            self.tools.stack_value("mining tools", "tools")
            socket_object.send("\n you have build tools, try and figure out what to use them for \n".encode(format))
        elif command == "build tools" and self.tools.find_node("mining tools"):
            socket_object.send("\n you have already build tools, try and figure out what to use them for \n".encode(format))


        if command == "build mine" and self.tools.find_node("mining tools") and self.buildings.find_node("mine") is False:
            self.options.append("info mine")
            self.buildings.stack_value("mine", Mine())
            socket_object.send("\n you have build a mine, new options have been added \n".encode(format))
        elif command == "build mine" and self.tools.find_node("mining tools") is False and self.buildings.find_node("mine") is False:
            socket_object.send("\n you don't have any tools to start mining \n".encode(format))
        elif command == "build mine" and self.buildings.find_node("mine"):
            socket_object.send("\n you have already dug a mine \n".encode(format))

        if command == "info mine" and self.buildings.find_node("mine"):
            socket_object.send(self.buildings.get_node("mine").description.encode(format))
        elif command == "info mine" and self.buildings.find_node("mine") is False:
            socket_object.send("\n you haven't dug a mine yet \n".encode(format))

        if command == "build bank" and self.buildings.find_node("bank") is False and self.buildings.find_node("mine"):
            self.options.append("info bank")
            self.buildings.stack_value("bank", Bank())
            socket_object.send("\n you have build a bank now go fund stuff \n".encode(format))
        elif command == "build bank" and self.buildings.find_node("bank") is False and self.buildings.find_node("mine") is False:
            socket_object.send("\n You don't have any gold to store in the bank \n".encode(format))
        elif command == "build bank" and self.buildings.find_node("mine"):
            socket_object.send("\n You have already build a bank, go fund some stuff \n".encode(format))

        if command == "info bank" and self.buildings.find_node("bank"):
            socket_object.send(self.buildings.get_node("bank").description.encode(format))
        elif command == "info bank" and self.buildings.find_node("bank") is False:
            socket_object.send("\n There is no bank \n".encode(format))

        if command == "build town hall" and self.buildings.find_node("bank"):
            self.buildings.stack_value("town hall", TownHall())
            socket_object.send(self.buildings.get_node("town hall").win_message.encode(format))
        elif command == "build town hall" and self.buildings.find_node("bank") is False:
            socket_object.send("\n You do n ot have the funding for that \n".encode(format))

        if command not in self.options:
            socket_object.send(f"\n command not understood... type info to see commands \n".encode(format))


    def show_options(self, socket_object, format):
        message = ""
        for command in self.options:
            message += "\n"+command+"\n"

        socket_object.send((message+"\n").encode(format))