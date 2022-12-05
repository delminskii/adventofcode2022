#!/usr/bin/env python3
import re
from pathlib import Path


def get_stacks_instructions(contents):
    # hell, dirty; just works
    ret_instructions, ret_stacks = [], []

    stack_lines = []
    go_instr = False
    for line in contents.split("\n"):
        if not go_instr and not line.strip().startswith("1"):
            stack_lines.append(line)
        elif line.strip().startswith("1"):
            go_instr = True
            continue

        if go_instr and line.strip():
            ret_instructions.append(line)

    temp = defaultdict(list)
    for stack_line in reversed(stack_lines):
        for i, ch in enumerate(stack_line):
            if ch == "[":
                temp[i].append(stack_line[i + 1])
    ret_stacks = list(temp.values())

    return ret_stacks, ret_instructions


def part1(contents):
    stacks, instructions = get_stacks_instructions(contents)
    for inst in instructions:
        n, from_i, to_i = map(
            int,
            re.search(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)", inst).groups(),
        )
        from_i -= 1
        to_i -= 1

        for _ in range(n):
            stacks[to_i].append(stacks[from_i].pop())

    print("Part1:", "".join(s[-1] for s in stacks))


def part2(contents):
    stacks, instructions = get_stacks_instructions(contents)
    for inst in instructions:
        n, from_i, to_i = map(
            int,
            re.search(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)", inst).groups(),
        )
        from_i -= 1
        to_i -= 1

        stacks[to_i].extend(reversed([stacks[from_i].pop() for _ in range(n)]))

    print("Part2:", "".join(s[-1] for s in stacks))


if __name__ == "__main__":
    contents = Path("input.txt").read_text()
    part1(contents)
    part2(contents)
