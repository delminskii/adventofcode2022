#!/usr/bin/env python3
from pathlib import Path


def part1(contents):
    n = len(contents)
    pos = float("inf")
    for i in range(0, n - 3):
        window = contents[i : i + 4]
        if len(window) == len(set(window)):
            pos = min(pos, contents.index(window))
    print(f"Part1: {pos+len(window)}")


def part2(contents):
    n = len(contents)
    pos = float("inf")
    for i in range(0, n - 13):
        window = contents[i : i + 14]
        if len(window) == len(set(window)):
            pos = min(pos, contents.index(window))
    print(f"Part2: {pos+len(window)}")


if __name__ == "__main__":
    contents = Path("input.txt").read_text().strip()
    part1(contents)
    part2(contents)
