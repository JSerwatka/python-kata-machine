"""Translated from `kata-machine-js/src/__tests__/BinarySearchList.ts`."""


def test_binary_search_array(import_algorithm):
    binary_search_list = import_algorithm("BinarySearchList")
    data = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert binary_search_list(data, 69) is True
    assert binary_search_list(data, 1336) is False
    assert binary_search_list(data, 69420) is True
    assert binary_search_list(data, 69421) is False
    assert binary_search_list(data, 1) is True
    assert binary_search_list(data, 0) is False
