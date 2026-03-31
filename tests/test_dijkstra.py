"""Translated from `kata-machine-js/src/__tests__/DijkstraList.ts`."""

from tests.helpers import LIST1


def test_dijkstra_via_adj_list(import_algorithm):
    dijkstra_list = import_algorithm("DijkstraList")
    assert dijkstra_list(0, 6, LIST1) == [0, 1, 4, 5, 6]
