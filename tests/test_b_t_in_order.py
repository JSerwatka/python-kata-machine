"""Translated from `kata-machine-js/src/__tests__/BTInOrder.ts`."""

from tests.helpers import TREE


def test_bt_in_order(import_algorithm):
    bt_in_order = import_algorithm("BTInOrder")
    assert bt_in_order(TREE) == [5, 7, 10, 15, 20, 29, 30, 45, 50, 100]
