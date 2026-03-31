"""Translated from `kata-machine-js/src/__tests__/BTPostOrder.ts`."""

from tests.helpers import TREE


def test_bt_post_order(import_algorithm):
    bt_post_order = import_algorithm("BTPostOrder")
    assert bt_post_order(TREE) == [7, 5, 15, 10, 29, 45, 30, 100, 50, 20]
