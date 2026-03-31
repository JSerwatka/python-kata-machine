"""Stable algorithm implementations used by the translated parity tests."""

from __future__ import annotations

from collections import deque
from math import floor, sqrt

from tests.helpers import BinaryNode, GraphEdge, Point


def bubble_sort(arr: list[int]) -> None:
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


def merge_sort(arr: list[int]) -> None:
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def quick_sort(arr: list[int]) -> None:
    def partition(lo: int, hi: int) -> int:
        pivot = arr[hi]
        idx = lo - 1
        for i in range(lo, hi):
            if arr[i] <= pivot:
                idx += 1
                arr[idx], arr[i] = arr[i], arr[idx]
        idx += 1
        arr[idx], arr[hi] = arr[hi], arr[idx]
        return idx

    def sort(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        pivot = partition(lo, hi)
        sort(lo, pivot - 1)
        sort(pivot + 1, hi)

    if arr:
        sort(0, len(arr) - 1)


def two_crystal_balls(breaks: list[bool]) -> int:
    jump = floor(sqrt(len(breaks)))
    i = jump
    while i < len(breaks) and not breaks[i]:
        i += jump
    i -= jump
    for j in range(jump):
        idx = i + j
        if idx < len(breaks) and breaks[idx]:
            return idx
    return -1


def bt_pre_order(head: BinaryNode | None) -> list[int]:
    path: list[int] = []

    def walk(curr: BinaryNode | None) -> None:
        if curr is None:
            return
        path.append(curr.value)
        walk(curr.left)
        walk(curr.right)

    walk(head)
    return path


def bt_in_order(head: BinaryNode | None) -> list[int]:
    path: list[int] = []

    def walk(curr: BinaryNode | None) -> None:
        if curr is None:
            return
        walk(curr.left)
        path.append(curr.value)
        walk(curr.right)

    walk(head)
    return path


def bt_post_order(head: BinaryNode | None) -> list[int]:
    path: list[int] = []

    def walk(curr: BinaryNode | None) -> None:
        if curr is None:
            return
        walk(curr.left)
        walk(curr.right)
        path.append(curr.value)

    walk(head)
    return path


def bt_bfs(head: BinaryNode | None, needle: int) -> bool:
    if head is None:
        return False
    q = deque([head])
    while q:
        curr = q.popleft()
        if curr.value == needle:
            return True
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)
    return False


def compare_binary_trees(a: BinaryNode | None, b: BinaryNode | None) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.value != b.value:
        return False
    return compare_binary_trees(a.left, b.left) and compare_binary_trees(a.right, b.right)


def dfs_on_bst(head: BinaryNode | None, needle: int) -> bool:
    curr = head
    while curr is not None:
        if curr.value == needle:
            return True
        curr = curr.left if needle < curr.value else curr.right
    return False


def bfs_graph_list(graph: list[list[GraphEdge]], source: int, needle: int) -> list[int] | None:
    seen = [False] * len(graph)
    prev = [-1] * len(graph)
    q = deque([source])
    seen[source] = True
    while q:
        curr = q.popleft()
        if curr == needle:
            break
        for edge in graph[curr]:
            if seen[edge.to]:
                continue
            seen[edge.to] = True
            prev[edge.to] = curr
            q.append(edge.to)
    if not seen[needle]:
        return None
    return _reconstruct_path(prev, source, needle)


def bfs_graph_matrix(graph: list[list[int]], source: int, needle: int) -> list[int] | None:
    seen = [False] * len(graph)
    prev = [-1] * len(graph)
    q = deque([source])
    seen[source] = True
    while q:
        curr = q.popleft()
        if curr == needle:
            break
        for idx, weight in enumerate(graph[curr]):
            if weight == 0 or seen[idx]:
                continue
            seen[idx] = True
            prev[idx] = curr
            q.append(idx)
    if not seen[needle]:
        return None
    return _reconstruct_path(prev, source, needle)


def dfs_graph_list(graph: list[list[GraphEdge]], source: int, needle: int) -> list[int] | None:
    seen = [False] * len(graph)
    path: list[int] = []

    def walk(curr: int) -> bool:
        if seen[curr]:
            return False
        seen[curr] = True
        path.append(curr)
        if curr == needle:
            return True
        for edge in graph[curr]:
            if walk(edge.to):
                return True
        path.pop()
        return False

    if walk(source):
        return path
    return None


def dijkstra_list(source: int, sink: int, graph: list[list[GraphEdge]]) -> list[int]:
    dist = [float("inf")] * len(graph)
    prev = [-1] * len(graph)
    seen = [False] * len(graph)
    dist[source] = 0
    while True:
        curr = -1
        lowest = float("inf")
        for i, value in enumerate(dist):
            if not seen[i] and value < lowest:
                lowest = value
                curr = i
        if curr == -1:
            break
        seen[curr] = True
        for edge in graph[curr]:
            if seen[edge.to]:
                continue
            alt = dist[curr] + edge.weight
            if alt < dist[edge.to]:
                dist[edge.to] = alt
                prev[edge.to] = curr
    return _reconstruct_path(prev, source, sink)


def prims_list(graph: list[list[GraphEdge]]) -> list[list[GraphEdge]]:
    seen = [False] * len(graph)
    out = [[] for _ in range(len(graph))]
    seen[0] = True
    edges: list[tuple[int, int, int]] = []
    for edge in graph[0]:
        edges.append((edge.weight, 0, edge.to))
    while edges:
        edges.sort(key=lambda item: item[0])
        weight, frm, to = edges.pop(0)
        if seen[to]:
            continue
        seen[to] = True
        out[frm].append(GraphEdge(to=to, weight=weight))
        out[to].append(GraphEdge(to=frm, weight=weight))
        for edge in graph[to]:
            if not seen[edge.to]:
                edges.append((edge.weight, to, edge.to))
    return out


def maze_solver(
    maze: list[str],
    wall: str,
    start: Point,
    end: Point,
) -> list[Point]:
    seen = [[False] * len(maze[0]) for _ in maze]
    path: list[Point] = []
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def walk(x: int, y: int) -> bool:
        if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
            return False
        if maze[y][x] == wall or seen[y][x]:
            return False
        seen[y][x] = True
        point = Point(x=x, y=y)
        path.append(point)
        if point == end:
            return True
        for dx, dy in directions:
            if walk(x + dx, y + dy):
                return True
        path.pop()
        return False

    if walk(start.x, start.y):
        return path
    return []


def _reconstruct_path(prev: list[int], source: int, needle: int) -> list[int]:
    path = []
    curr = needle
    while curr != -1:
        path.append(curr)
        if curr == source:
            break
        curr = prev[curr]
    path.reverse()
    return path if path and path[0] == source else []
