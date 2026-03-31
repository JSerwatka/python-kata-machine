"""Translated from `kata-machine-js/src/__tests__/PrimsList.ts`."""

from tests.helpers import GraphEdge, LIST1


def test_prims_algorithm(import_algorithm):
    prims = import_algorithm("PrimsList")
    assert prims(LIST1) == [
        [GraphEdge(to=2, weight=1), GraphEdge(to=1, weight=3)],
        [GraphEdge(to=0, weight=3), GraphEdge(to=4, weight=1)],
        [GraphEdge(to=0, weight=1)],
        [GraphEdge(to=6, weight=1)],
        [GraphEdge(to=1, weight=1), GraphEdge(to=5, weight=2)],
        [GraphEdge(to=4, weight=2), GraphEdge(to=6, weight=1)],
        [GraphEdge(to=5, weight=1), GraphEdge(to=3, weight=1)],
    ]
