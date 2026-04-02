def bubble_sort(*args, **kwargs):
    arr, = args
    if len(arr) < 2:
        return arr

    for i in range(0,len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j]= temp

    return arr
                
# Better
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
        
    Time Complexity: O(n^2) - TODO: Analyze after implementation
    Space Complexity: O(1) - TODO: Analyze after implementation
    """
    arr, = args
    if len(arr) < 2:
        return arr

    for i in range(0,len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr
                