import math


def two_crystal_balls(*args, **kwargs):
    arr, = args
    if len(arr) == 0:
        return False
    STEP = math.floor(math.sqrt(len(arr)))
    last_idx = 0
    next_idx = STEP

    while next_idx < (len(arr) - 1):
        if arr[next_idx]:
            for i in range(last_idx, next_idx+1):
                if arr[i]:
                    return i
        last_idx = next_idx + 1
        next_idx = next_idx + STEP

    for i in range(last_idx, len(arr)):
        if arr[i]:
            return i
    return -1



# Lepsze

def two_crystal_balls(*args, **kwargs):
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