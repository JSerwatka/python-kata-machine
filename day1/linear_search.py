"""Day 1 LinearSearch implementation."""


def linear_search(haystack: list[int], needle: int) -> bool:
    for value in haystack:
        if value == needle:
            return True
    return False


# Example usage and testing
if __name__ == "__main__":
    print("Run 'python kata.py test' to run the full test suite")
