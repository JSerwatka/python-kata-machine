# JS Parity Test Port Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Translate the visible `kata-machine-js` test suite into `python-kata-machine`, remove all placeholder/skipped parity tests, and add the minimal Python runtime and implementation support needed for those tests to pass without pre-generating future `dayN` folders.

**Architecture:** Keep the Python repo's day-based workflow intact, but make the test and import layer capable of resolving both function-style and class-style algorithms by canonical JS algorithm name. Port the JS test helpers into Python fixtures/modules, then implement only the runtime/config and algorithm modules necessary for parity and generator correctness.

**Tech Stack:** Python 3, pytest, existing `kata.py`/`test_runner.py`/`scripts/daily.py` workflow

---

### Task 1: Establish parity inventory and helper surface

**Files:**
- Create: `docs/plans/2026-03-31-js-parity-test-port.md`
- Create: `tests/helpers.py`
- Modify: `tests/conftest.py`

**Step 1: Write the failing test**

```python
from tests.helpers import TREE, TREE2, LIST1, LIST2, MATRIX2, exercise_list_contract
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_array_list.py -q`
Expected: FAIL because `tests.helpers` does not exist.

**Step 3: Write minimal implementation**

```python
# Add Python equivalents for JS tree/graph/list helper fixtures and expose them
# through `tests.helpers` and/or pytest fixtures.
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_array_list.py -q`
Expected: test module imports cleanly; remaining failures move to missing algorithm behavior.

**Step 5: Commit**

```bash
git add docs/plans/2026-03-31-js-parity-test-port.md tests/helpers.py tests/conftest.py
git commit -m "docs: add js parity implementation plan"
```

### Task 2: Port translated pytest files for the existing placeholder suite

**Files:**
- Modify: `tests/test_array_list.py`
- Modify: `tests/test_b_f_s_graph_matrix.py`
- Modify: `tests/test_b_t_b_f_s.py`
- Modify: `tests/test_b_t_in_order.py`
- Modify: `tests/test_b_t_post_order.py`
- Modify: `tests/test_b_t_pre_order.py`
- Modify: `tests/test_binary_search_list.py`
- Modify: `tests/test_compare_binary_trees.py`
- Modify: `tests/test_d_f_s_graph_list.py`
- Modify: `tests/test_d_f_s_on_b_s_t.py`
- Modify: `tests/test_dijkstra.py`
- Modify: `tests/test_doubly_linked_list.py`
- Modify: `tests/test_insertion_sort.py`
- Modify: `tests/test_l_r_u.py`
- Modify: `tests/test_map.py`
- Modify: `tests/test_merge_sort.py`
- Modify: `tests/test_prims_list.py`
- Modify: `tests/test_queue.py`
- Modify: `tests/test_quick_sort.py`
- Modify: `tests/test_singly_linked_list.py`
- Modify: `tests/test_stack.py`
- Modify: `tests/test_trie.py`
- Modify: `tests/test_two_crystal_balls.py`

**Step 1: Write the failing test**

```python
def test_binary_search_array(import_algorithm):
    binary_search_list = import_algorithm("BinarySearchList")
    data = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert binary_search_list(data, 69) is True
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_binary_search_list.py -q`
Expected: FAIL because the placeholder skip is replaced and the implementation is missing or incorrect.

**Step 3: Write minimal implementation**

```python
# Replace each placeholder file with a close translation of the corresponding JS
# assertions, reusing shared helpers where JS uses tree/graph/list fixtures.
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_binary_search_list.py -q`
Expected: PASS for the translated test once the implementation is present.

**Step 5: Commit**

```bash
git add tests/test_*.py
git commit -m "test: translate js parity suite into pytest"
```

### Task 3: Add missing pytest files for JS-covered algorithms absent in Python

**Files:**
- Create: `tests/test_b_f_s_graph_list.py`
- Create: `tests/test_maze_solver.py`
- Create: `tests/test_min_heap.py`
- Create: `tests/test_ring_buffer.py`

**Step 1: Write the failing test**

```python
def test_min_heap(import_algorithm):
    heap_cls = import_algorithm("MinHeap")
    heap = heap_cls()
    assert heap.length == 0
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_min_heap.py -q`
Expected: FAIL because the test file or algorithm target does not yet exist.

**Step 3: Write minimal implementation**

```python
# Add new parity test files mirroring JS expectations for BFSGraphList,
# MazeSolver, MinHeap, and RingBuffer.
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_min_heap.py -q`
Expected: PASS after the algorithm implementation exists.

**Step 5: Commit**

```bash
git add tests/test_b_f_s_graph_list.py tests/test_maze_solver.py tests/test_min_heap.py tests/test_ring_buffer.py
git commit -m "test: add missing js parity files"
```

### Task 4: Fix runtime/config/import support for full parity coverage

**Files:**
- Modify: `kata.config.py`
- Modify: `tests/conftest.py`
- Modify: `scripts/daily.py`
- Modify: `scripts/generate.py`
- Modify: `scripts/generate_tests.py`
- Modify: `test_runner.py`

**Step 1: Write the failing test**

```python
def test_import_algorithm_returns_class_for_queue(import_algorithm):
    queue_cls = import_algorithm("Queue")
    queue = queue_cls()
    assert queue.length == 0
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_queue.py -q`
Expected: FAIL because `import_algorithm` currently assumes a function export.

**Step 3: Write minimal implementation**

```python
# Teach the loader to resolve either a function or a class/object by canonical
# algorithm name, and extend the configured progression so later `daily`
# generation can create placeholders for the full JS-visible suite.
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_queue.py -q`
Expected: PASS once loader/config support is in place.

**Step 5: Commit**

```bash
git add kata.config.py tests/conftest.py scripts/daily.py scripts/generate.py scripts/generate_tests.py test_runner.py
git commit -m "feat: support full js parity generation and imports"
```

### Task 5: Implement function-based algorithms required by parity tests

**Files:**
- Modify: `day1/linear_search.py`
- Modify: `day2/binary_search_list.py`
- Create: `python_kata_machine_algorithms.py`

**Step 1: Write the failing test**

```python
def test_two_crystal_balls(import_algorithm):
    fn = import_algorithm("TwoCrystalBalls")
    assert fn([False] * 821) == -1
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_two_crystal_balls.py -q`
Expected: FAIL because the implementation does not exist yet.

**Step 3: Write minimal implementation**

```python
# Implement function-style algorithms such as TwoCrystalBalls, BubbleSort,
# InsertionSort, MergeSort, QuickSort, tree traversals, graph traversals,
# Dijkstra, Prims, and MazeSolver in a stable module the loader can resolve.
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_two_crystal_balls.py -q`
Expected: PASS.

**Step 5: Commit**

```bash
git add day1/linear_search.py day2/binary_search_list.py python_kata_machine_algorithms.py
git commit -m "feat: add function algorithm parity implementations"
```

### Task 6: Implement class-based data structures required by parity tests

**Files:**
- Create: `python_kata_machine_structures.py`

**Step 1: Write the failing test**

```python
def test_stack(import_algorithm):
    stack_cls = import_algorithm("Stack")
    stack = stack_cls()
    stack.push(5)
    assert stack.pop() == 5
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_stack.py -q`
Expected: FAIL because the class does not exist or does not satisfy the JS contract.

**Step 3: Write minimal implementation**

```python
# Implement Queue, Stack, ArrayList, SinglyLinkedList, DoublyLinkedList, Trie,
# LRU, Map, MinHeap, and RingBuffer with Python APIs matching the translated
# JS tests.
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_stack.py -q`
Expected: PASS.

**Step 5: Commit**

```bash
git add python_kata_machine_structures.py
git commit -m "feat: add data structure parity implementations"
```

### Task 7: Verify parity suite and report remaining non-test gaps

**Files:**
- Modify: `README.md`

**Step 1: Write the failing test**

```python
# No new test. Verification task.
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests -q`
Expected: Any remaining failures identify missing parity work.

**Step 3: Write minimal implementation**

```python
# Fix remaining parity gaps, then document any non-test project mismatches found
# during the port.
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests -q`
Expected: PASS with zero skipped parity tests.

**Step 5: Commit**

```bash
git add README.md
git commit -m "docs: note js parity coverage and remaining repo gaps"
```
