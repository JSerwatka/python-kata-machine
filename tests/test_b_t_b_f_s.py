"""Translated from `kata-machine-js/src/__tests__/BTBFS.ts`."""

from tests.helpers import TREE


def test_bt_bfs(import_algorithm):
    bfs = import_algorithm("BTBFS")
    assert bfs(TREE, 45) is True
    assert bfs(TREE, 7) is True
    assert bfs(TREE, 69) is False
