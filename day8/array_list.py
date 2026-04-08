"""
ArrayList Algorithm Implementation
Daily Practice - Day 8

Follow ThePrimeagen's course to implement this algorithm.
"""

from typing import List, Optional, Any


def array_list(*args, **kwargs):
    """
    ArrayList implementation
    
    TODO: 
    1. Follow the course lesson for ArrayList
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
    class ArrayList:
        def __init__(self, capacity):
            self.arr = [None]*capacity
            self.lenght = 0
            self.capacity = capacity

        def append(self, item: int):
            self.lenght += 1
            if self.lenght > self.capacity:
                self.capacity *= 2
                new_arr = [None] * self.capacity
    
                for idx, el in enumerate(self.arr):
                    new_arr[idx] = el
                new_arr[self.lenght - 1] = item
                self.arr = new_arr
            else:
                self.arr[self.lenght-1] = item
            return item
                

        def prepend(self, item: int) -> None:
            self.lenght += 1
            if self.lenght > self.capacity:
                self.capacity = max(1, self.capacity * 2)
                new_arr = [None] * self.capacity
                new_arr[0] = item
                for idx, el in enumerate(self.arr):
                    new_arr[idx + 1] = el
                self.arr = new_arr
            else:
                for i in range(self.lenght - 1, 0, -1):
                    self.arr[i] = self.arr[i - 1]
                self.arr[0] = item

        def get(self, index: int) -> int | None:
            if index >= self.lenght or index < 0:
                return False
            return self.arr[index]

        def remove(self, item: int) -> int | None:
            if self.lenght == 0:
                return False

            for idx, el in enumerate(self.arr):
                if el == item:
                    return self.remove_at(idx)
        def remove_at(self, index: int) -> int | None: 
            if index >= self.lenght or index < 0:
                return False
            item = self.arr[index]
            for i in range(index + 1, self.lenght - 1):  # was self.lenght
                self.arr[i] = self.arr[i + 1]
            self.lenght -= 1
            self.arr[self.lenght] = None
            return item
    return ArrayList


# Example usage and testing
if __name__ == "__main__":
    # TODO: Add example usage and basic testing
    print(f"Testing ArrayList...")
    
    # Example test cases (replace with actual test cases)
    # result = array_list(test_input)
    # print(f"Result: {result}")
    
    print("Run 'python kata.py test' to run the full test suite")
