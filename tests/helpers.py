"""Shared fixtures and helper contracts translated from the JS test suite."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(eq=True)
class GraphEdge:
    to: int
    weight: int


@dataclass(eq=True)
class BinaryNode:
    value: int
    left: "BinaryNode | None" = None
    right: "BinaryNode | None" = None


@dataclass(eq=True)
class Point:
    x: int
    y: int


LIST1 = [
    [GraphEdge(to=1, weight=3), GraphEdge(to=2, weight=1)],
    [GraphEdge(to=0, weight=3), GraphEdge(to=2, weight=4), GraphEdge(to=4, weight=1)],
    [GraphEdge(to=1, weight=4), GraphEdge(to=3, weight=7), GraphEdge(to=0, weight=1)],
    [GraphEdge(to=2, weight=7), GraphEdge(to=4, weight=5), GraphEdge(to=6, weight=1)],
    [GraphEdge(to=1, weight=1), GraphEdge(to=3, weight=5), GraphEdge(to=5, weight=2)],
    [GraphEdge(to=6, weight=1), GraphEdge(to=4, weight=2), GraphEdge(to=2, weight=18)],
    [GraphEdge(to=3, weight=1), GraphEdge(to=5, weight=1)],
]

LIST2 = [
    [GraphEdge(to=1, weight=3), GraphEdge(to=2, weight=1)],
    [GraphEdge(to=4, weight=1)],
    [GraphEdge(to=3, weight=7)],
    [],
    [GraphEdge(to=1, weight=1), GraphEdge(to=3, weight=5), GraphEdge(to=5, weight=2)],
    [GraphEdge(to=2, weight=18), GraphEdge(to=6, weight=1)],
    [GraphEdge(to=3, weight=1)],
]

MATRIX2 = [
    [0, 3, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 5, 0, 2, 0],
    [0, 0, 18, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
]

TREE = BinaryNode(
    value=20,
    left=BinaryNode(
        value=10,
        left=BinaryNode(value=5, right=BinaryNode(value=7)),
        right=BinaryNode(value=15),
    ),
    right=BinaryNode(
        value=50,
        left=BinaryNode(
            value=30,
            left=BinaryNode(value=29),
            right=BinaryNode(value=45),
        ),
        right=BinaryNode(value=100),
    ),
)

TREE2 = BinaryNode(
    value=20,
    left=BinaryNode(
        value=10,
        left=BinaryNode(value=5, right=BinaryNode(value=7)),
        right=BinaryNode(value=15),
    ),
    right=BinaryNode(
        value=50,
        left=BinaryNode(
            value=30,
            left=BinaryNode(value=29, left=BinaryNode(value=21)),
            right=BinaryNode(value=45, right=BinaryNode(value=49)),
        ),
    ),
)


class ListLike(Protocol):
    length: int

    def append(self, item: int) -> None: ...

    def prepend(self, item: int) -> None: ...

    def get(self, index: int) -> int | None: ...

    def remove(self, item: int) -> int | None: ...

    def remove_at(self, index: int) -> int | None: ...


def exercise_list_contract(lst: ListLike) -> None:
    """Literal translation of JS `test_list` helper."""
    lst.append(5)
    lst.append(7)
    lst.append(9)

    assert lst.get(2) == 9
    assert lst.remove_at(1) == 7
    assert lst.length == 2

    lst.append(11)
    assert lst.remove_at(1) == 9
    assert lst.remove(9) is None
    assert lst.remove_at(0) == 5
    assert lst.remove_at(0) == 11
    assert lst.length == 0

    lst.prepend(5)
    lst.prepend(7)
    lst.prepend(9)

    assert lst.get(2) == 5
    assert lst.get(0) == 9
    assert lst.remove(9) == 9
    assert lst.length == 2
    assert lst.get(0) == 7


def draw_path(data: list[str], path: list[Point]) -> list[str]:
    maze = [list(row) for row in data]
    for point in path:
        if 0 <= point.y < len(maze) and 0 <= point.x < len(maze[point.y]):
            maze[point.y][point.x] = "*"
    return ["".join(row) for row in maze]
