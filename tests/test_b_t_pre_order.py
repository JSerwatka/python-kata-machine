"""Translated from `kata-machine-js/src/__tests__/BTPreOrder.ts`."""

from tests.helpers import TREE


def test_bt_pre_order(import_algorithm):
    bt_pre_order = import_algorithm("BTPreOrder")
    assert bt_pre_order(TREE) == [20, 10, 5, 7, 15, 50, 30, 29, 45, 100]
