"""Translated from `kata-machine-js/src/__tests__/LinearSearchList.ts`."""


def test_linear_search_array(import_algorithm):
    linear_search = import_algorithm("LinearSearch")
    data = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert linear_search(data, 69) is True
    assert linear_search(data, 1336) is False
    assert linear_search(data, 69420) is True
    assert linear_search(data, 69421) is False
    assert linear_search(data, 1) is True
    assert linear_search(data, 0) is False
