"""Translated from `kata-machine-js/src/__tests__/MergeSort.ts`."""


def test_merge_sort(import_algorithm):
    merge_sort = import_algorithm("MergeSort")
    arr = [9, 3, 7, 4, 69, 420, 42]
    merge_sort(arr)
    assert arr == [3, 4, 7, 9, 42, 69, 420]
