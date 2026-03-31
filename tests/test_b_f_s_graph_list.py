"""Translated from `kata-machine-js/src/__tests__/BFSGraphList.ts`."""

from tests.helpers import LIST2


def test_bfs_graph_list(import_algorithm):
    bfs = import_algorithm("BFSGraphList")
    assert bfs(LIST2, 0, 6) == [0, 1, 4, 5, 6]
    assert bfs(LIST2, 6, 0) is None
