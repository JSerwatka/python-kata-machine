"""Translated from `kata-machine-js/src/__tests__/QuickSort.ts`."""


def test_quick_sort(import_algorithm):
    quick_sort = import_algorithm("QuickSort")
    arr = [9, 3, 7, 4, 69, 420, 42]
    quick_sort(arr)
    assert arr == [3, 4, 7, 9, 42, 69, 420]
