"""Translated from `kata-machine-js/src/__tests__/Queue.ts`."""


def test_queue(import_algorithm):
    queue_cls = import_algorithm("Queue")
    queue = queue_cls()
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)
    print(queue)
    assert queue.deque() == 5
    assert queue.length == 2
    queue.enqueue(11)
    assert queue.deque() == 7
    assert queue.deque() == 9
    assert queue.peek() == 11
    assert queue.deque() == 11
    assert queue.deque() is None
    assert queue.length == 0
    queue.enqueue(69)
    assert queue.peek() == 69
    assert queue.length == 1
