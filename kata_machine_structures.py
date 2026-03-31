"""Stable data structure implementations used by the parity tests."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


class Queue:
    def __init__(self) -> None:
        self._data: deque[int] = deque()

    @property
    def length(self) -> int:
        return len(self._data)

    def enqueue(self, item: int) -> None:
        self._data.append(item)

    def deque(self) -> int | None:
        return self._data.popleft() if self._data else None

    def peek(self) -> int | None:
        return self._data[0] if self._data else None


class Stack:
    def __init__(self) -> None:
        self._data: list[int] = []

    @property
    def length(self) -> int:
        return len(self._data)

    def push(self, item: int) -> None:
        self._data.append(item)

    def pop(self) -> int | None:
        return self._data.pop() if self._data else None

    def peek(self) -> int | None:
        return self._data[-1] if self._data else None


class ArrayList:
    def __init__(self, _capacity: int = 0) -> None:
        self._data: list[int] = []

    @property
    def length(self) -> int:
        return len(self._data)

    def append(self, item: int) -> None:
        self._data.append(item)

    def prepend(self, item: int) -> None:
        self._data.insert(0, item)

    def get(self, index: int) -> int | None:
        if 0 <= index < len(self._data):
            return self._data[index]
        return None

    def remove(self, item: int) -> int | None:
        try:
            idx = self._data.index(item)
        except ValueError:
            return None
        return self._data.pop(idx)

    def remove_at(self, index: int) -> int | None:
        if 0 <= index < len(self._data):
            return self._data.pop(index)
        return None


@dataclass
class _Node:
    value: int
    prev: "_Node | None" = None
    next: "_Node | None" = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self._data: list[int] = []

    @property
    def length(self) -> int:
        return len(self._data)

    def append(self, item: int) -> None:
        self._data.append(item)

    def prepend(self, item: int) -> None:
        self._data.insert(0, item)

    def get(self, index: int) -> int | None:
        if 0 <= index < len(self._data):
            return self._data[index]
        return None

    def remove(self, item: int) -> int | None:
        try:
            idx = self._data.index(item)
        except ValueError:
            return None
        return self._data.pop(idx)

    def remove_at(self, index: int) -> int | None:
        if 0 <= index < len(self._data):
            return self._data.pop(index)
        return None


class DoublyLinkedList(SinglyLinkedList):
    pass


class Trie:
    def __init__(self) -> None:
        self._words: set[str] = set()

    def insert(self, word: str) -> None:
        self._words.add(word)

    def delete(self, word: str) -> None:
        self._words.discard(word)

    def find(self, prefix: str) -> list[str]:
        return [word for word in self._words if word.startswith(prefix)]


class LRU:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._data: dict[str, int] = {}
        self._order: list[str] = []

    def _touch(self, key: str) -> None:
        if key in self._order:
            self._order.remove(key)
        self._order.insert(0, key)

    def get(self, key: str) -> int | None:
        if key not in self._data:
            return None
        self._touch(key)
        return self._data[key]

    def update(self, key: str, value: int) -> None:
        if key not in self._data and len(self._data) == self.capacity:
            evicted = self._order.pop()
            del self._data[evicted]
        self._data[key] = value
        self._touch(key)


class Map:
    def __init__(self) -> None:
        self._data: dict[str, int] = {}

    def set(self, key: str, value: int) -> None:
        self._data[key] = value

    def get(self, key: str) -> int | None:
        return self._data.get(key)

    def delete(self, key: str) -> None:
        self._data.pop(key, None)

    def size(self) -> int:
        return len(self._data)


class MinHeap:
    def __init__(self) -> None:
        self._data: list[int] = []

    @property
    def length(self) -> int:
        return len(self._data)

    def insert(self, value: int) -> None:
        self._data.append(value)
        self._heapify_up(len(self._data) - 1)

    def delete(self) -> int | None:
        if not self._data:
            return None
        if len(self._data) == 1:
            return self._data.pop()
        out = self._data[0]
        self._data[0] = self._data.pop()
        self._heapify_down(0)
        return out

    def _heapify_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self._data[parent] <= self._data[idx]:
                return
            self._data[parent], self._data[idx] = self._data[idx], self._data[parent]
            idx = parent

    def _heapify_down(self, idx: int) -> None:
        size = len(self._data)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < size and self._data[left] < self._data[smallest]:
                smallest = left
            if right < size and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == idx:
                return
            self._data[idx], self._data[smallest] = self._data[smallest], self._data[idx]
            idx = smallest


class RingBuffer:
    def __init__(self) -> None:
        self._data: deque[int] = deque()

    def push(self, item: int) -> None:
        self._data.append(item)

    def pop(self) -> int | None:
        return self._data.popleft() if self._data else None

    def get(self, index: int) -> int | None:
        if 0 <= index < len(self._data):
            return list(self._data)[index]
        return None
