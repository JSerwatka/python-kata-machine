"""
BubbleSort Algorithm Implementation
Daily Practice - Day 4

Follow ThePrimeagen's course to implement this algorithm.
"""

from typing import List, Optional, Any


def bubble_sort(*args, **kwargs):
    """
    BubbleSort implementation
    
    TODO: 
    1. Follow the course lesson for BubbleSort
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
    if len(arr) < 2:
        return arr

    for i in range(0,len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr
                
    


# Example usage and testing
if __name__ == "__main__":
    # TODO: Add example usage and basic testing
    print(f"Testing BubbleSort...")
    
    # Example test cases (replace with actual test cases)
    # result = bubble_sort(test_input)
    # print(f"Result: {result}")
    
    print("Run 'python kata.py test' to run the full test suite")
