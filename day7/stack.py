"""
Stack Algorithm Implementation
Daily Practice - Day 7

Follow ThePrimeagen's course to implement this algorithm.
"""

from typing import List, Optional, Any


def stack(*args, **kwargs):
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class Stack:
        def __init__(self):
            self.head = None
            self.__length = 0 

        def push(self, value):
            new_node = Node(value)

            self.__length += 1
            new_node.next = self.head
            self.head = new_node


        def pop(self):
            if self.head is None:
                return None

            value_to_pop = self.head.value
            self.__length -= 1
            self.head = self.head.next
            return value_to_pop
        
        @property
        def length(self):
            return self.__length
        
        def peek(self):
            return None if self.head is None else self.head.value
        
        def __str__(self):
            curr_node = self.head
            str_out = ""
            while curr_node:
                str_out += str(curr_node.value) + ", "
                curr_node = curr_node.next
            return str_out
    return Stack()

# Example usage and testing
if __name__ == "__main__":
    # TODO: Add example usage and basic testing
    print(f"Testing Stack...")
    
    # Example test cases (replace with actual test cases)
    # result = stack(test_input)
    # print(f"Result: {result}")
    
    print("Run 'python kata.py test' to run the full test suite")
