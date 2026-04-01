# Python Kata-Machine

A Python port of ThePrimeagen's [kata-machine](https://github.com/ThePrimeagen/kata-machine) for **daily algorithm practice** without TypeScript.

Fork of [https://github.com/nevermore23274/python-kata-machine](https://github.com/nevermore23274/python-kata-machine) with implemented all tests.

## What This Is

This project recreates the daily practice workflow from ThePrimeagen's "The Last Algorithms Course You'll Need" but using Python instead of TypeScript. **One algorithm per day**, following the course progression, building algorithmic thinking through spaced repetition.

## Quick Start

### Setup

```bash
git clone https://github.com/JSerwatka/python-kata-machine
```

**Daily Workflow:**

```bash
python kata.py daily              # ✅ Get today's algorithm
python kata.py test               # ✅ Test your implementation
python kata.py complete           # ✅ Mark done, advance to tomorrow

python test_runner.py --day <num_day> # Test previous day / specific one
```

**Progress & Utility:**

```bash
python kata.py progress           # ✅ See your progress through course
python kata.py config             # ✅ Check configuration
python kata.py clear              # ✅ Clean up practice files
python kata.py reset              # ✅ Start course over
```

## Quick Start, Simple and Fast

```bash
# 1. Clone and setup (one-time)
git clone https://github.com/JSerwatka/python-kata-machine
cd python-kata-machine

# 2. Daily practice routine
python kata.py daily                    # Generate today's algorithm
cd day1                                 # Navigate to practice folder
vim linear_search.py                   # Edit the algorithm file
# OR: code linear_search.py, nano linear_search.py, etc.

# 3. Test and complete
python kata.py test                     # Test your implementation
python kata.py complete                 # Mark done, advance to next day
```

## How It Works (Daily Practice System!)

1. **Get Today's Algorithm:** Run `python kata.py daily` to get one algorithm ✅
2. **Implement Algorithm:** Edit the generated file following ThePrimeagen's lesson ✅
3. **Test Your Code:** Run `python kata.py test` to verify correctness ✅
4. **Mark Complete:** Run `python kata.py complete` to advance to tomorrow ✅
5. **Repeat Daily:** Build algorithmic thinking through spaced repetition ✅

## Complete Daily Workflow

```bash
# 1. Get today's algorithm
python kata.py daily
# Output: "📅 Day 1 Practice - 🎯 Today's Algorithm: LinearSearch"

# 2. Implement the algorithm
cd day1
# Edit linear_search.py - follow ThePrimeagen's lesson

# 3. Test your implementation
python kata.py test
# See if your algorithm passes the tests!

# 4. Mark complete and get tomorrow's algorithm
python kata.py complete
# Advances to Day 2 with next algorithm

# 5. Check your progress anytime
python kata.py progress
# See: "Completed: 1/25 algorithms (4.0%)"
```

## What You Get When You Test

```bash
python kata.py test
# Shows:
# ✅ Tests PASS if your algorithm is correct
# ❌ Tests FAIL with helpful error messages if incorrect
# ⚠️  Message if no tests exist yet for this algorithm
# 📊 Clear feedback on your implementation
```

## Development Environment

The container includes:

- **Python 3.11** - Latest stable Python
- **pytest** - Testing framework (equivalent to Jest)
- **black** - Code formatter (equivalent to Prettier)
- **mypy** - Type checking (equivalent to TypeScript)
- **rich** - Beautiful console output
- **pyyaml** - Configuration file support

## Project Structure (Daily Practice)

```
python-kata-machine/
├── kata.config.py            # Course progression & config ✅
├── config_loader.py          # Configuration system ✅
├── check_config.py           # Config validation ✅
├── kata.py                   # Main daily practice interface ✅
├── test_runner.py            # Test runner for daily practice ✅
├── pytest.ini               # Pytest configuration ✅
├── scripts/
│   ├── daily.py             # Daily practice generator ✅
│   └── clear.py             # Clean up utility ✅
├── tests/                   # Essential test examples ✅
│   ├── conftest.py          # Pytest fixtures ✅
│   ├── test_linear_search.py # Complete test example ✅
│   ├── test_bubble_sort.py  # Complete test example ✅
│   └── test_queue.py        # Data structure test example ✅
├── day1/                    # Generated daily practice ✅
│   ├── __init__.py          # Python package setup ✅
│   └── linear_search.py     # Today's algorithm to implement ✅
├── day2/                    # Tomorrow's practice (after complete)
├── day3/                    # Next day...
├── .kata_progress.json      # Your progress (auto-generated) ✅
└── .gitignore               # Git exclusions ✅
```

## Course Progression (25 Algorithms)

**Week 1-2: Foundations**

- LinearSearch, BinarySearchList, TwoCrystalBalls
- BubbleSort, InsertionSort

**Week 3-4: Data Structures**

- Queue, Stack, ArrayList
- SinglyLinkedList, DoublyLinkedList

**Week 5-6: Advanced Sorting & Trees**

- MergeSort, QuickSort
- BTPreOrder, BTInOrder, BTPostOrder, BTBFS

**Week 7-8: Tree & Graph Operations**

- CompareBinaryTrees, DFSOnBST
- BFSGraphMatrix, DFSGraphList

**Week 9-10: Advanced Algorithms**

- Dijkstra, PrimsList
- Trie, LRU, Map

## Ready to Start!

This is a **complete daily practice system** - the TypeScript kata-machine workflow, perfected for Python learners.

**Perfect for:**

- Following ThePrimeagen's course with Python
- Building consistent daily coding habits
- Learning algorithms without language complexity
- Preparing for technical interviews
- Developing algorithmic thinking

**Next Steps:**

1. **2 minutes:** Set up the container
2. **Daily:** `python kata.py daily` → code → `python kata.py test` → `python kata.py complete`
3. **10 weeks:** Complete all 25 algorithms from the course
4. **Forever:** Solid algorithmic foundation 🎉

## Contributing

See [DEVELOPMENT.md](DEVELOPMENT.md) for development setup and contribution guidelines.

Happy coding! 🚀

---

_This project is inspired by and based on [ThePrimeagen's kata-machine](https://github.com/ThePrimeagen/kata-machine). All credit for the original concept and algorithm selection goes to ThePrimeagen._
