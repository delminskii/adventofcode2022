#!/usr/bin/env python3
import operator
from functools import reduce
from pathlib import Path


def part1(contents):
    visible_trees_counter = 0
    grid = [[x for x in row] for row in contents.split("\n")]
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if i not in (0, n - 1) and j not in (0, m - 1):
                # inner
                visible_trees_counter += any(
                    (
                        all(grid[i][j] > grid[k][j] for k in range(0, i)),
                        all(grid[i][j] > grid[k][j] for k in range(i + 1, n)),
                        all(grid[i][j] > grid[i][k] for k in range(0, j)),
                        all(grid[i][j] > grid[i][k] for k in range(j + 1, m)),
                    )
                )
            else:
                # edge
                visible_trees_counter += 1

    print(f"Part1: {visible_trees_counter}")


def part2(contents):
    max_scenic_score = 0
    grid = [[x for x in row] for row in contents.split("\n")]
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            # we do not review edges: multiply by 0 - no sense
            if i not in (0, n - 1) and j not in (0, m - 1):
                counters = [0, 0, 0, 0]  # left, top, right, botton

                # move left
                k = j - 1
                while k > -1:
                    counters[0] += 1
                    if grid[i][k] >= grid[i][j]:
                        break
                    k -= 1

                # move top
                k = i - 1
                while k > -1:
                    counters[1] += 1
                    if grid[k][j] >= grid[i][j]:
                        break
                    k -= 1

                # move right
                k = j + 1
                while k < m:
                    counters[2] += 1
                    if grid[i][k] >= grid[i][j]:
                        break
                    k += 1

                # move down
                k = i + 1
                while k < n:
                    counters[3] += 1
                    if grid[k][j] >= grid[i][j]:
                        break
                    k += 1

                # print(
                #     f"elem: {grid[i][j]} ; counters: {counters} ;; {reduce(operator.mul, counters, 1)}"
                # )
                max_scenic_score = max(
                    max_scenic_score, reduce(operator.mul, counters, 1)
                )

    print(f"Part2: {max_scenic_score}")


if __name__ == "__main__":
    contents = Path("input.txt").read_text().strip()
    part1(contents)
    part2(contents)
