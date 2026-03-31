"""Translated from `kata-machine-js/src/__tests__/DFSOnBST.ts`."""

from tests.helpers import TREE


def test_dfs_on_bst(import_algorithm):
    dfs = import_algorithm("DFSOnBST")
    assert dfs(TREE, 45) is True
    assert dfs(TREE, 7) is True
    assert dfs(TREE, 69) is False
