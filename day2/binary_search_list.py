"""Day 2 BinarySearchList implementation."""


import math


def binary_search_list(haystack: list[int], needle: int) -> bool:
    
    lo = 0
    hi = len(haystack) - 1
    while lo <= hi:
        mid_idx = lo + (hi - lo) // 2
        mid_val = haystack[mid_idx]

        if mid_val == needle:
            return True
        if needle < mid_val:
            hi = mid_idx - 1
        elif needle > mid_val:
            lo = mid_idx + 1
    return False


# Example usage and testing
if __name__ == "__main__":
    print("Run 'python kata.py test' to run the full test suite")



#