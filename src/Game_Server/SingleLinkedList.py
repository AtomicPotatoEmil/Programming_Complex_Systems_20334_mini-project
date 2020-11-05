from Game_Server.Node import *

class SingleLinkedList:

    def __init__(self):
        self.head_value = None

    def list_print(self):
        print_value = self.head_value
        while print_value is not None:
            print(print_value.data_value)
            print_value = print_value.next_value

    def add_beginning(self, new_data):
        new_node = Node(new_data)

        new_node.next_value = self.head_value
        self.head_value = new_node

    def inbetween(self, middle_node, new_data):
        if middle_node is None:
            print("The present node is absent")
            return

        new_node = Node(new_data)
        new_node.next_value = middle_node.next_value
        middle_node.next_value = new_node

    def add_end(self, new_data):
        new_node = Node(new_data)

        if self.head_value is Node:
            self.head_value = new_node
            return

        laste = self.head_value
        while(laste.next_value):
            laste = laste.next_value
        laste.next_value = new_node

    def remove_node(self, remove_key): # This function only works with Keys made with the add_beginning function

        head_value = self.head_value

        if head_value is not None:
            if head_value.data_value == remove_key:
                self.head_value = head_value.next_value
                head_value = None
                return

        while head_value is not None:
            if head_value == remove_key:
                break
            previous_value = head_value
            head_value = head_value.next_value

        if head_value == None:
            return

        previous_value.next_value = head_value.next_value

        head_value = None


    def find_value(self, value):
        current_node = self.head_value

        node_id = 1

        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            current_node = current_node.next_value
            node_id += 1
        return results