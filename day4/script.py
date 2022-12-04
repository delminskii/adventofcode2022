#!/usr/bin/env python3
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Pair:
    left: int
    right: int

    def __post_init__(self):
        self.left = int(self.left)
        self.right = int(self.right)

    def is_fully_within(self, other) -> bool:
        if self.right - self.left + 1 <= other.right - other.left + 1:
            return self.left >= other.left and self.right <= other.right
        return False

    def is_partially_within(self, other) -> bool:
        return any(self.left >= x for x in (other.left, other.right)) or any(
            self.right >= x for x in (other.left, other.right)
        )


def part1(contents):
    lines = filter(bool, map(str.strip, contents.split("\n")))
    assignments_number = 0
    for line in lines:
        pairs = [
            Pair(*map(str.strip, x.split("-")))
            for x in map(str.strip, line.split(","))
        ]
        assignments_number += bool(
            pairs[0].is_fully_within(pairs[1])
            or pairs[1].is_fully_within(pairs[0])
        )
    print(f"Part1: {assignments_number}")


def part2(contents):
    lines = filter(bool, map(str.strip, contents.split("\n")))
    assignments_number = 0
    for line in lines:
        pairs = [
            Pair(*map(str.strip, x.split("-")))
            for x in map(str.strip, line.split(","))
        ]
        assignments_number += bool(
            pairs[0].is_partially_within(pairs[1])
            and pairs[1].is_partially_within(pairs[0])
        )
    print(f"Part2: {assignments_number}")


if __name__ == "__main__":
    contents = Path("input.txt").read_text().strip()
    part1(contents)
    part2(contents)
