#!/usr/bin/env python3
from pathlib import Path


def part1(contents):
    def get_calculated_points(op_opt, my_opt):
        ret_points = {"X": 1, "Y": 2, "Z": 3}[my_opt]
        if my_opt == "X":
            ret_points += {"A": 3, "B": 0, "C": 6}[op_opt]
        elif my_opt == "Y":
            ret_points += {"A": 6, "B": 3, "C": 0}[op_opt]
        elif my_opt == "Z":
            ret_points += {"A": 0, "B": 6, "C": 3}[op_opt]

        return ret_points

    total_points = 0
    for round_line in map(str.strip, contents.split("\n")):
        op_opt, my_opt = map(str.strip, round_line.split())
        round_points = get_calculated_points(op_opt, my_opt)
        total_points += round_points

        print(f"Round: {round_line} ;; round points: {round_points}")
    print(f"Part1: {total_points}")


def part2(contents):
    def get_calculated_points(op_opt, my_opt):
        ret_points = {"X": 0, "Y": 3, "Z": 6}[my_opt]
        if my_opt == "X":
            ret_points += {"A": 3, "B": 1, "C": 2}[op_opt]
        elif my_opt == "Y":
            ret_points += {"A": 1, "B": 2, "C": 3}[op_opt]
        elif my_opt == "Z":
            ret_points += {"A": 2, "B": 3, "C": 1}[op_opt]

        return ret_points

    total_points = 0
    for round_line in map(str.strip, contents.split("\n")):
        op_opt, my_opt = map(str.strip, round_line.split())
        round_points = get_calculated_points(op_opt, my_opt)
        total_points += round_points

        print(f"Round: {round_line} ;; round points: {round_points}")
    print(f"Part2: {total_points}")


if __name__ == "__main__":
    contents = Path("input.txt").read_text().strip()
    part1(contents)
    part2(contents)
