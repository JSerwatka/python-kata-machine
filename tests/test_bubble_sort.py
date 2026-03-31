"""Translated from `kata-machine-js/src/__tests__/BubbleSort.ts`."""


def test_bubble_sort(import_algorithm):
    bubble_sort = import_algorithm("BubbleSort")
    arr = [9, 3, 7, 4, 69, 420, 42]
    bubble_sort(arr)
    assert arr == [3, 4, 7, 9, 42, 69, 420]
