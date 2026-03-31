"""Translated from `kata-machine-js/src/__tests__/ArrayList.ts`."""

from tests.helpers import exercise_list_contract


def test_array_list(import_algorithm):
    array_list_cls = import_algorithm("ArrayList")
    array_list = array_list_cls(3)
    exercise_list_contract(array_list)
