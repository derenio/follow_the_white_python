#!/usr/bin/env python
import os

from utils import MazeSolver


def main():
    solver = MazeSolver(
        maze_path=os.path.join(os.path.dirname(__file__), 'maze.htm'))
    solver.solve()


if __name__ == '__main__':
    main()
