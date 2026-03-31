"""Translated from `kata-machine-js/src/__tests__/Stack.ts`."""


def test_stack(import_algorithm):
    stack_cls = import_algorithm("Stack")
    stack = stack_cls()
    stack.push(5)
    stack.push(7)
    stack.push(9)
    assert stack.pop() == 9
    assert stack.length == 2
    stack.push(11)
    assert stack.pop() == 11
    assert stack.pop() == 7
    assert stack.peek() == 5
    assert stack.pop() == 5
    assert stack.pop() is None
    stack.push(69)
    assert stack.peek() == 69
    assert stack.length == 1
