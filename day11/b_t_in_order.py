"""
BTInOrder Algorithm Implementation
Daily Practice - Day 11

Follow ThePrimeagen's course to implement this algorithm.
"""

from typing import List, Optional, Any


def b_t_in_order(*args, **kwargs):
    """
    BTInOrder implementation
    
    TODO: 
    1. Follow the course lesson for BTInOrder
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
    tree, = args
    arr = []
    def traverse_in_order(node = tree):
        if node is None:
            return
        
        # 1. Left node
        traverse_in_order(node.left)
        
        # 2. Root
        arr.append(node.value)
        
        # 3. Right node
        traverse_in_order(node.right)
    traverse_in_order(tree)
    return arr




# Example usage and testing
if __name__ == "__main__":
    # TODO: Add example usage and basic testing
    print(f"Testing BTInOrder...")
    
    # Example test cases (replace with actual test cases)
    # result = b_t_in_order(test_input)
    # print(f"Result: {result}")
    
    print("Run 'python kata.py test' to run the full test suite")
