from Game_Server.EventListener import *
import threading
class GameLoop:

    def __init__(self, is_running : bool):
        self.is_running = is_running
        self.event_listener = EventListener()
        pass

    def game_loop(self):
        while self.is_running:
            command = input("Type command: ")
            command.lower()
            thread = threading.Thread(target=self.debug, args=(command,))
            thread.start()
        pass

    def debug(self, command : str):
        if command == "hello":
            print("Hello back")
        if command == "poop":
            print("lol")
        pass