#!/usr/bin/env python3
import string
from functools import reduce
from pathlib import Path


def part1(contents):
    priorities = dict((l, i + 1) for i, l in enumerate(string.ascii_lowercase))
    priorities_sum = 0

    lines = filter(bool, map(str.strip, contents.split("\n")))
    for line in lines:
        mid = len(line) // 2
        priority = sum(
            priorities[x] if x in priorities else priorities[x.lower()] + 26
            for x in set(line[:mid]) & set(line[mid:])
        )
        priorities_sum += priority
    print(f"Part1: {priorities_sum}")


def part2(contents):
    priorities = dict((l, i + 1) for i, l in enumerate(string.ascii_lowercase))
    priorities_sum = 0

    lines = filter(bool, map(str.strip, contents.split("\n")))
    threes = []
    for line in lines:
        threes.append(line)
        if len(threes) == 3:
            common_item_set = reduce(
                set.__and__, map(set, threes), set(string.ascii_letters)
            )
            priorities_sum += sum(
                priorities[x]
                if x in priorities
                else priorities[x.lower()] + 26
                for x in common_item_set
            )

            threes = []
    print(f"Part2: {priorities_sum}")


if __name__ == "__main__":
    contents = Path("input.txt").read_text().strip()
    part1(contents)
    part2(contents)
