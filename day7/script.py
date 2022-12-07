#!/usr/bin/env python3
import re
from pathlib import Path


def get_locations(contents) -> dict:
    locs = dict()  # to return

    lines = map(str.strip, contents.split("\n"))
    curr_filepath_stack = []
    curr_files = []
    for line in lines:
        if line.startswith("$ cd"):
            # print(curr_filepath_stack)
            # for f in curr_files:
            #     print(f)
            # print("*" * 10)
            curr_filepath_stack_copy = curr_filepath_stack.copy()
            while curr_filepath_stack_copy:
                k = "/".join(curr_filepath_stack_copy)
                if k.startswith("//"):
                    k = k[1:]
                locs[k] = curr_files.copy()
                curr_filepath_stack_copy.pop()
            curr_files = []

            if line.endswith(".."):
                curr_filepath_stack.pop()
            else:
                curr_filepath_stack.append(line.split()[-1])
        else:
            if re.search(r"^(\d+)", line):
                curr_files.append(line)

    if curr_files:
        k = "/".join(curr_filepath_stack)
        if k.startswith("//"):
            k = k[1:]
        locs[k] = curr_files.copy()

    # __import__("pprint").pprint(locs)
    return locs


def part1(contents):
    p1_size = 0
    locs = get_locations(contents)
    for abs_filapth, files_arr in locs.items():
        dir_files_size = 0
        for k in locs.keys():
            if k.startswith(abs_filapth):
                dir_files_size += sum(int(f.split()[0]) for f in locs[k])

        if dir_files_size <= 100_000:
            # print("FOUND: ", abs_filapth, dir_files_size)
            p1_size += dir_files_size

    print(f"Part1: {p1_size}")


if __name__ == "__main__":
    contents = Path("input.txt").read_text().strip()
    part1(contents)
    # part2(contents)
