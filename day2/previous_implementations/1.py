# V1
# def binary_search_list(haystack: list[int], needle: int) -> bool:
#     arr_len = len(haystack)
    
#     if arr_len == 0:
#         return False
    
#     middle_index =  math.floor(arr_len / 2) 
#     middle_val = haystack[middle_index]
#     if needle == middle_val:
#         return True
    
#     if needle < middle_val:
#         return binary_search_list(haystack[0:middle_index], needle)
#     elif needle > middle_val:
#         return binary_search_list(haystack[(middle_index + 1):], needle)
#     else:
#         raise ValueError()



#  V2

# def binary_search_list(haystack: list[int], needle: int) -> bool:
#     lo_idx = 0
#     high_idx = len(haystack) - 1

#     while lo_idx <= high_idx:
#         middle_idx = (high_idx + lo_idx) // 2 
#         middle_val = haystack[middle_idx]
#         if needle == middle_val:
#             return True
#         if needle < middle_val:
#             high_idx = middle_idx - 1
#             continue
#         if needle > middle_val:
#             lo_idx = middle_idx + 1
#             continue
#     return False


'''
Lepiej ustawić middle_idx =  lo_idx + (hi - lo) // 2 
Instead of averaging the two numbers directly, it measures the distance between them and takes half of that distance.
'''