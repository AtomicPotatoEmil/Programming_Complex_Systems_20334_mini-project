class Node:

    def __init__(self, data_value):
        self.data_value = data_value
        self.next_value = None
        self.previous_value = None

    def has_value(self, value):
        if self.data_value == value:
            return True
        else:
            return False