from Game_Server.EventListener import *
import threading
class GameLoop:

    def __init__(self):
        self.event_listener = EventListener()
        self.current_command = None
        pass

    def game_loop(self, command : str):
        command.lower()
        thread = threading.Thread(target=self.debug, args=(command,))
        thread.start()

    def debug(self, command : str):
        if command == "hello":
            self.current_command = "hello back"
            print("hello back")
        if command == "poop":
            self.current_command = "lol"