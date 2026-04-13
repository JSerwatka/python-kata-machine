"""
BTPostOrder Algorithm Implementation
Daily Practice - Day 13

Follow ThePrimeagen's course to implement this algorithm.
"""

from typing import List, Optional, Any


def b_t_post_order(*args, **kwargs):
    """
    BTPostOrder implementation
    
    TODO: 
    1. Follow the course lesson for BTPostOrder
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
    def traversal_post_order(node = tree):
        if node is None:
            return
    
        traversal_post_order(node.left)
        traversal_post_order(node.right)
        arr.append(node.value)

    traversal_post_order(tree)
    return arr

# Example usage and testing
if __name__ == "__main__":
    # TODO: Add example usage and basic testing
    print(f"Testing BTPostOrder...")
    
    # Example test cases (replace with actual test cases)
    # result = b_t_post_order(test_input)
    # print(f"Result: {result}")
    
    print("Run 'python kata.py test' to run the full test suite")
