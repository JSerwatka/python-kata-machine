"""
SinglyLinkedList Algorithm Implementation
Daily Practice - Day 5

Follow ThePrimeagen's course to implement this algorithm.
"""

from typing import List, Optional, Any


def singly_linked_list(*args, **kwargs):
    """
    SinglyLinkedList implementation
    
    TODO: 
    1. Follow the course lesson for SinglyLinkedList
    2. Implement the algorithm step by step
    3. Test your implementation with: python kata.py test
    
    Args:
        *args: Replace with actual parameters based on algorithm requirements
        **kwargs: Replace with actual parameters based on algorithm requirements
    
    Returns:
        Replace with actual return type and description
        
    Time Complexity: O(?) - TODO: Analyze after implementation
    Space Complexity: O(?) - TODO: Analyze after implementation
    """
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class ListLike():
        length: int

        def __init__(self):
            self.head = None
            self.tail = None

        def append(self, item: int) -> None:
            new_item  = Node(item)
            self.tail.next = new_item
            self.tail = new_item

            if self.head is None:
                self.head = self.tail

        def prepend(self, item: int) -> None:
            temp = self.head
            self.head = Node(item)
            self.head.next = temp

            if self.tail is None:
                self.tail = self.head

        def get(self, index: int) -> int | None:
            curr_index = 0
            curr_node = self.head

            if curr_node is None:
                return -1
        
            while curr_node:
                if curr_index == index:
                    return curr_node.value

                curr_index += 1
                curr_node = curr_node.next
            return -1

        def insert_at(self, index: int, value: int) -> bool:
            curr_index = 0
            curr_node = self.head

            if index == 0:
                self.prepend(value)
                return True

            while curr_node:
                prev_node = curr_node
                curr_node = curr_node.next
                curr_index += 1

                if curr_index == index:
                    new_node = Node()
                    prev_node.next  = new_node
                    new_node.next = curr_node
                    return True
            
            return False

        def remove(self, item: int) -> int | None:
            curr_index = 0
            curr_node = self.head

            if curr_node is None:
                return -1
            
            if self.head == item:
                self.head = self.head.next
                return 0

            while curr_node:
                prev_node = curr_node
                curr_node = curr_node.next
                curr_index += 1

                if curr_node.value == item:
                    prev_node.next = curr_node.next
                    return curr_index

        def remove_at(self, index: int) -> int | None:
            curr_index = 0
            curr_node = self.head

            if curr_node is None:
                return -1
            
            if index == 0:
                self.head = self.head.next
                return 0

            while curr_node:
                prev_node = curr_node
                curr_node = curr_node.next
                curr_index += 1

                if curr_index == index:
                    prev_node.next = curr_node.next
                    return curr_index

            

# Example usage and testing
if __name__ == "__main__":
    # TODO: Add example usage and basic testing
    print(f"Testing SinglyLinkedList...")
    
    # Example test cases (replace with actual test cases)
    # result = singly_linked_list(test_input)
    # print(f"Result: {result}")
    
    print("Run 'python kata.py test' to run the full test suite")
