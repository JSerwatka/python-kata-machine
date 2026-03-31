"""Translated from `kata-machine-js/src/__tests__/BFSGraphMatrix.ts`."""

from tests.helpers import MATRIX2


def test_bfs_graph_matrix(import_algorithm):
    bfs = import_algorithm("BFSGraphMatrix")
    assert bfs(MATRIX2, 0, 6) == [0, 1, 4, 5, 6]
    assert bfs(MATRIX2, 6, 0) is None
