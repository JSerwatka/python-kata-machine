"""Translated from `kata-machine-js/src/__tests__/DFSGraphList.ts`."""

from tests.helpers import LIST2


def test_dfs_graph_list(import_algorithm):
    dfs = import_algorithm("DFSGraphList")
    assert dfs(LIST2, 0, 6) == [0, 1, 4, 5, 6]
    assert dfs(LIST2, 6, 0) is None
