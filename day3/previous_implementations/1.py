# v1
'''
Ta wersja jest O(n)

'''

    # arr, = args
    # index = 0
    # print(arr, index)
    # while index < len(arr):
    #     if arr[index]:
    #         return index 

    #     index += 1
        
    # return -1

'''
Ta wersja jest wersja która skacze  o połowę arr aż znajdzie pęknięcie a potem szuka liniowo
Problem tutaj jest takie że jak zbije nam się kulka w pierwszy kroku (dla arr o długości 100 będzie to 50), to będzimey musieli przuszkać O(N/2) = O(N), czyli nie zrobiliśmy żadnego progresu
https://medium.com/@wudlig/the-two-crystal-ball-problem-2d31093bbd33
'''

import math


def two_crystal_balls(*args, **kwargs):
    arr, = args
    num_of_balls = 2
    lo = 0
    hi = len(arr) - 1

    while num_of_balls == 2:
        mid = math.floor(lo + (hi-2) / 2)
        if mid < lo or mid > hi:
            return -1

        if arr[mid] == True:
            num_of_balls -= 1
            continue

        lo = mid + 1
    
    for idx in range(lo, len(arr) - 1):
        if arr[idx] == True:
            return idx
