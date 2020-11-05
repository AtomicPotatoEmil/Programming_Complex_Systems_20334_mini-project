from Game_Server.EventListener import *

class GameLoop:

    def __init__(self, is_running : bool):
        self.is_running = is_running
        self.event_listener = EventListener()
        pass

    def game_loop(self):
        pass