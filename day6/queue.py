"""
Queue Algorithm Implementation
Daily Practice - Day 6

Follow ThePrimeagen's course to implement this algorithm.
"""

from typing import List, Optional, Any


def queue(*args, **kwargs):
    """
    Queue implementation
    
    TODO: 
    1. Follow the course lesson for Queue
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
            self.val = value
            self.next = None

    class Queue:
        def __init__(self):
            self.head = None
            self.tail = None
            self._length = 0

        @property
        def length(self):
            return self._length
        
        def enqueue(self, value):
            new_node = Node(value)
            self._length += 1

            if self.tail is None:
                self.tail = new_node
                self.head = self.tail
                return self.tail
            
            self.tail.next = new_node
            self.tail = new_node
        
        def deque(self):
            head_node = self.head

            if self.head is None:
                self.tail = None
                return None
            
            self._length -= 1
            self.head = self.head.next

            return head_node.val

        def peek(self):
            return  None if self.head is None else self.head.val
        
        def __str__(self):
            curr_node = self.head
            str_out = ""
            while curr_node:
                str_out += str(curr_node.val) + ", "
                curr_node = curr_node.next
            return str_out
    return Queue()
                



# Example usage and testing
if __name__ == "__main__":
    # TODO: Add example usage and basic testing
    print(f"Testing Queue...")
    
    # Example test cases (replace with actual test cases)
    # result = queue(test_input)
    # print(f"Result: {result}")
    
    print("Run 'python kata.py test' to run the full test suite")
