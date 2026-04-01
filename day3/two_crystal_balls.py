"""
TwoCrystalBalls Algorithm Implementation
Daily Practice - Day 3

Follow ThePrimeagen's course to implement this algorithm.
"""

import math
from typing import List, Optional, Any


def two_crystal_balls(*args, **kwargs):
    """
    TwoCrystalBalls implementation
    
    TODO: 
    1. Follow the course lesson for TwoCrystalBalls
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
    arr, = args
    if len(arr) == 0:
        return -1
    STEP = math.floor(math.sqrt(len(arr)))
    i = STEP

    while i < len(arr):
        if arr[i]:
            break
        i += STEP

    start_of_block = i - STEP
    for i in range(start_of_block, min(i+1, len(arr))):
        if arr[i]:
            return i
    return -1



# Example usage and testing
if __name__ == "__main__":
    # TODO: Add example usage and basic testing
    print(f"Testing TwoCrystalBalls...")
    
    # Example test cases (replace with actual test cases)
    # result = two_crystal_balls(test_input)
    # print(f"Result: {result}")
    
    print("Run 'python kata.py test' to run the full test suite")
