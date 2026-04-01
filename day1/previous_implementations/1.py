def linear_search(haystack: list[int], needle: int) -> bool:
    for value in haystack:
        if value == needle:
            return True
    return False


