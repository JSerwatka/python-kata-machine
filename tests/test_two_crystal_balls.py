"""Translated from `kata-machine-js/src/__tests__/TwoCrystalBalls.ts`."""

import random


def test_two_crystal_balls(import_algorithm):
    two_crystal_balls = import_algorithm("TwoCrystalBalls")
    idx = random.randrange(0, 10000)
    data = [False] * 10000
    for i in range(idx, 10000):
        data[i] = True
    assert two_crystal_balls(data) == idx
    assert two_crystal_balls([False] * 821) == -1
