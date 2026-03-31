"""Translated from `kata-machine-js/src/__tests__/RingBuffer.ts`."""


def test_ring_buffer(import_algorithm):
    ring_buffer_cls = import_algorithm("RingBuffer")
    buffer = ring_buffer_cls()
    buffer.push(5)
    assert buffer.pop() == 5
    assert buffer.pop() is None
    buffer.push(42)
    buffer.push(9)
    assert buffer.pop() == 42
    assert buffer.pop() == 9
    assert buffer.pop() is None
    buffer.push(42)
    buffer.push(9)
    buffer.push(12)
    assert buffer.get(2) == 12
    assert buffer.get(1) == 9
    assert buffer.get(0) == 42
