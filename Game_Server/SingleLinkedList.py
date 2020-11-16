from Node import *

class SingleLinkedList:

    def __init__(self):
        self.head_value = None
        self.node_values = {}

    def stack_value(self, key, value):
        new_node = Node(value)
        new_node.next_value = self.head_value
        self.node_values[key] = value
        self.head_value = new_node

    def print_values(self, socket_object, format):
        print_node = self.head_value
        while print_node:
            print(print_node.data_value)
            print_node = print_node.next_value

    def find_node(self, key):
        if key in self.node_values:
            return True
        else:
            return False

    def get_node(self, key):
        if key in self.node_values:
            return self.node_values[key]
        else:
            return