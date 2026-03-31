"""Translated from `kata-machine-js/src/__tests__/InsertionSort.ts`."""


def test_insertion_sort(import_algorithm):
    insertion_sort = import_algorithm("InsertionSort")
    arr = [9, 3, 7, 4, 69, 420, 42]
    insertion_sort(arr)
    assert arr == [3, 4, 7, 9, 42, 69, 420]
