"""Translated from `kata-machine-js/src/__tests__/MinHeap.ts`."""


def test_min_heap(import_algorithm):
    min_heap_cls = import_algorithm("MinHeap")
    heap = min_heap_cls()
    assert heap.length == 0
    heap.insert(5)
    heap.insert(3)
    heap.insert(69)
    heap.insert(420)
    heap.insert(4)
    heap.insert(1)
    heap.insert(8)
    heap.insert(7)
    assert heap.length == 8
    assert heap.delete() == 1
    assert heap.delete() == 3
    assert heap.delete() == 4
    assert heap.delete() == 5
    assert heap.length == 4
    assert heap.delete() == 7
    assert heap.delete() == 8
    assert heap.delete() == 69
    assert heap.delete() == 420
    assert heap.length == 0
