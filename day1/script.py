#!/usr/bin/env python3
from pathlib import Path


def part1(contents):
    m = 0
    for elf_calories_batch in contents.split("\n\n"):
        xs = map(str.strip, elf_calories_batch.split("\n"))
        xs = filter(bool, xs)
        m = max(m, sum(map(int, xs)))
    print("Part 1:", m)


def part2(contents):
    calories_batch = []
    for elf_calories_batch in contents.split("\n\n"):
        xs = map(str.strip, elf_calories_batch.split("\n"))
        xs = filter(bool, xs)
        calories_batch.append(sum(map(int, xs)))
    calories_batch.sort()
    print("Part 2:", sum(calories_batch[-3:]))


if __name__ == "__main__":
    contents = Path("input.txt").read_text()
    part1(contents)
    part2(contents)
