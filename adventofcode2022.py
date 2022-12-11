#
# The main execution framework for the AdventOfCode 2022 challenges.
# It defines a base class that takes a list of strings as input and
# defines the function part1() and part2() that deliver computation results
# in accordance with the respective task(s) for the day.
# The idea is that for each day a simple class is defined which only provides
# the algorithms for the day and this framework script will take care about instantiating
# and running the algorithms based on respective command line arguments
#
import importlib

class Day:

    def __init__(self, input):
        self.input = input

    def part1(self):
        raise NotImplementedError("not implemented yet")

    def part2(self):
        raise NotImplementedError("not implemented yet")

    def part(self, part):
        if part == 1:
            return self.part1()
        return self.part2()


def parse_args():
    import argparse
    parser = argparse.ArgumentParser("expects a number for the day (1-25) and {1,2} for the part on that day")
    parser.add_argument("day", type=int)
    parser.add_argument("part", type=int)
    args = parser.parse_args()
    assert(1 <= args.day <= 25), "argument for day not in range"
    assert(1 <= args.part <= 2), "argument for part not in range"
    return args.day, args.part


def read_input(day):
    file = open("input/input_{}".format(day), "r")
    lines = list(map(lambda line: line.rstrip("\n"), file.readlines()))
    file.close()
    return lines


def main(day, part):
    lines = read_input(day)
    module = __import__("day{}".format(day))
    day_class = getattr(module, "Day{}".format(day))
    day_instance = day_class(lines)
    return day_instance.part(part)


if __name__ == '__main__':
    (day, part) = parse_args()
    result = main(day, part)
    print(result)
