class EventListener:

    def __init__(self):
        self.current_feedback = None
        pass

    def listen_to_events(self, command):
        if command == "info":
            print("Here should be info")

    def has_building(self, command):
        pass

    def check_buildings(self, command):
        pass

    def building_progress(self):
        pass

    def debug(self):

        pass