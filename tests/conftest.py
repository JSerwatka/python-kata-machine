"""Pytest configuration and fixtures for Python Kata-Machine."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path
from typing import Any, Callable, List

import pytest

from tests.helpers import LIST1, LIST2, MATRIX2, TREE, TREE2


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--day", 
        action="store", 
        default=None,
        help="Run tests for specific day only"
    )


def pytest_configure(config):
    """Configure pytest with custom markers"""
    # Add day directories to Python path for imports
    base_dir = Path(__file__).parent.parent
    
    # Find day directories in base directory (not src/)
    day_dirs = [d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith("day")]
    if day_dirs:
        latest_day = max(day_dirs, key=lambda x: int(x.name[3:]))
        sys.path.insert(0, str(latest_day))
        print(f"🔧 Added {latest_day} to Python path for testing")


def pytest_collection_modifyitems(config, items):
    """Modify test collection based on command line options"""
    day_option = config.getoption("--day")
    
    if day_option:
        # Filter tests to only run for specified day
        day_marker = f"day{day_option}"
        selected_items = []
        
        for item in items:
            # Check if test has the day marker or if no day marker is present
            if item.get_closest_marker(day_marker) or not any(
                item.get_closest_marker(f"day{i}") for i in range(1, 10)
            ):
                selected_items.append(item)
        
        items[:] = selected_items


@pytest.fixture
def current_day():
    """Fixture to get the current day number from the latest day directory"""
    base_dir = Path(__file__).parent.parent
    day_dirs = [d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith("day")]
    if not day_dirs:
        return 1
    
    latest_day = max(day_dirs, key=lambda x: int(x.name[3:]))
    return int(latest_day.name[3:])


@pytest.fixture
def import_algorithm():
    """Fixture to dynamically import algorithms from the current day"""

    name_map = {
        "LinearSearch": ("day1.linear_search", "linear_search"),
        "BinarySearchList": ("day2.binary_search_list", "binary_search_list"),
        "BubbleSort": ("kata_machine_algorithms", "bubble_sort"),
        "InsertionSort": ("kata_machine_algorithms", "insertion_sort"),
        "MergeSort": ("kata_machine_algorithms", "merge_sort"),
        "QuickSort": ("kata_machine_algorithms", "quick_sort"),
        "TwoCrystalBalls": ("kata_machine_algorithms", "two_crystal_balls"),
        "BTPreOrder": ("kata_machine_algorithms", "bt_pre_order"),
        "BTInOrder": ("kata_machine_algorithms", "bt_in_order"),
        "BTPostOrder": ("kata_machine_algorithms", "bt_post_order"),
        "BTBFS": ("kata_machine_algorithms", "bt_bfs"),
        "CompareBinaryTrees": ("kata_machine_algorithms", "compare_binary_trees"),
        "DFSOnBST": ("kata_machine_algorithms", "dfs_on_bst"),
        "BFSGraphMatrix": ("kata_machine_algorithms", "bfs_graph_matrix"),
        "BFSGraphList": ("kata_machine_algorithms", "bfs_graph_list"),
        "DFSGraphList": ("kata_machine_algorithms", "dfs_graph_list"),
        "DijkstraList": ("kata_machine_algorithms", "dijkstra_list"),
        "PrimsList": ("kata_machine_algorithms", "prims_list"),
        "MazeSolver": ("kata_machine_algorithms", "maze_solver"),
        "Queue": ("kata_machine_structures", "Queue"),
        "Stack": ("kata_machine_structures", "Stack"),
        "ArrayList": ("kata_machine_structures", "ArrayList"),
        "SinglyLinkedList": ("kata_machine_structures", "SinglyLinkedList"),
        "DoublyLinkedList": ("kata_machine_structures", "DoublyLinkedList"),
        "Trie": ("kata_machine_structures", "Trie"),
        "LRU": ("kata_machine_structures", "LRU"),
        "Map": ("kata_machine_structures", "Map"),
        "MinHeap": ("kata_machine_structures", "MinHeap"),
        "RingBuffer": ("kata_machine_structures", "RingBuffer"),
    }

    def _import_algorithm(algorithm_name: str, day: int = None):
        """Import an algorithm function or class by canonical JS name."""
        if algorithm_name not in name_map:
            pytest.fail(f"Unknown algorithm requested: {algorithm_name}")

        module_name, symbol_name = name_map[algorithm_name]

        try:
            module = importlib.import_module(module_name)
            return getattr(module, symbol_name)
        except (ImportError, AttributeError) as e:
            pytest.fail(f"Could not import {algorithm_name}: {e}")
    
    return _import_algorithm


def _to_snake_case(name: str) -> str:
    """Convert CamelCase to snake_case"""
    result = []
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result.append('_')
        result.append(char.lower())
    return ''.join(result)


# Common test data fixtures
@pytest.fixture
def sample_arrays():
    """Common arrays for testing sorting and search algorithms"""
    return {
        "empty": [],
        "single": [42],
        "sorted": [1, 2, 3, 4, 5],
        "reverse_sorted": [5, 4, 3, 2, 1],
        "random": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        "duplicates": [1, 3, 2, 3, 1, 2, 3],
        "large": list(range(100, 0, -1))  # 100 elements in reverse order
    }


@pytest.fixture
def sample_strings():
    """Common strings for testing string algorithms"""
    return {
        "empty": "",
        "single_char": "a",
        "simple": "hello",
        "with_spaces": "hello world",
        "repeated": "aabbcc",
        "palindrome": "racecar"
    }


@pytest.fixture
def tree():
    return TREE


@pytest.fixture
def tree2():
    return TREE2


@pytest.fixture
def list1():
    return LIST1


@pytest.fixture
def list2():
    return LIST2


@pytest.fixture
def matrix2():
    return MATRIX2


# Performance testing helpers
class TimeComplexityAssertion:
    """Helper class for asserting time complexity"""
    
    @staticmethod
    def assert_linear_or_better(func: Callable, test_sizes: List[int] = None):
        """Assert that function runs in O(n) or better time"""
        # This is a placeholder for more sophisticated timing tests
        # In practice, you'd time the function with different input sizes
        pass
    
    @staticmethod
    def assert_logarithmic_or_better(func: Callable, test_sizes: List[int] = None):
        """Assert that function runs in O(log n) or better time"""
        pass


@pytest.fixture
def time_complexity():
    """Fixture for time complexity assertions"""
    return TimeComplexityAssertion
