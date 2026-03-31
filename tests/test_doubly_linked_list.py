"""Translated from `kata-machine-js/src/__tests__/DoublyLinkedList.ts`."""

from tests.helpers import exercise_list_contract


def test_doubly_linked_list(import_algorithm):
    linked_list_cls = import_algorithm("DoublyLinkedList")
    linked_list = linked_list_cls()
    exercise_list_contract(linked_list)
