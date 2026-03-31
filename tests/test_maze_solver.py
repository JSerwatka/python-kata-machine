"""Translated from `kata-machine-js/src/__tests__/MazeSolver.ts`."""

from tests.helpers import Point, draw_path


def test_maze_solver(import_algorithm):
    maze_solver = import_algorithm("MazeSolver")
    maze = [
        "xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx",
    ]
    maze_result = [
        Point(x=10, y=0),
        Point(x=10, y=1),
        Point(x=10, y=2),
        Point(x=10, y=3),
        Point(x=10, y=4),
        Point(x=9, y=4),
        Point(x=8, y=4),
        Point(x=7, y=4),
        Point(x=6, y=4),
        Point(x=5, y=4),
        Point(x=4, y=4),
        Point(x=3, y=4),
        Point(x=2, y=4),
        Point(x=1, y=4),
        Point(x=1, y=5),
    ]
    result = maze_solver(maze, "x", Point(x=10, y=0), Point(x=1, y=5))
    assert draw_path(maze, result) == draw_path(maze, maze_result)
