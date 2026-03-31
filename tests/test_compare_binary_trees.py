"""Translated from `kata-machine-js/src/__tests__/CompareBinaryTrees.ts`."""

from tests.helpers import TREE, TREE2


def test_compare_binary_trees(import_algorithm):
    compare = import_algorithm("CompareBinaryTrees")
    assert compare(TREE, TREE) is True
    assert compare(TREE, TREE2) is False
