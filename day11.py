import yaml
import re
import math

from adventofcode2022 import Day


class Monkey:

    @staticmethod
    def parse_numbers_from_string(string):
        return list(map(int, re.findall('\\d+', str(string))))

    def parse_test_string(self, test_string):
        numbers = Monkey.parse_numbers_from_string(test_string)
        self.divider = numbers[0]
        return "{} if item % {} == 0 else {}".format(numbers[1], numbers[0], numbers[2])

    def __init__(self, name: str, starting_items: list, operation: str, test_string: str):
        self.name = name
        self.divider = -1
        self.items = self.parse_numbers_from_string(starting_items)
        self.operation = operation.split("=")[1].strip()
        self.test_operation = self.parse_test_string(test_string)
        self.inspection_count = 0
        assert self.divider != -1

    def inspect(self, item):
        self.inspection_count += 1
        return eval(self.operation, {"old": item})

    def next_monkey(self, item):
        return eval(self.test_operation, {"item": item})


class Day11(Day):

    def __init__(self, input):
        super().__init__(input)
        self.monkeys = []
        dct = yaml.safe_load("\n".join([line.replace("true:", "true then").replace("false:", "false then") for line in input]))
        for m in dct:
            self.monkeys.append(Monkey(m, dct[m]['Starting items'], dct[m]['Operation'], dct[m]['Test']))

    @staticmethod
    def print_monkeys(monkeys):
        for monkey in monkeys:
            print("{}: {} - {}".format(monkey.name, monkey.items, monkey.inspection_count))

    @staticmethod
    def monkey_business(monkeys):
        sorted_counts = sorted([monkey.inspection_count for monkey in monkeys], reverse=True)
        return sorted_counts[0] * sorted_counts[1]

    def execute(self, number_iterations, stress_reduction, verbose=False):
        for i in range(number_iterations):
            for monkey in self.monkeys:
                while len(monkey.items) > 0:
                    item = monkey.items.pop(0)
                    item = stress_reduction(monkey.inspect(item))
                    self.monkeys[monkey.next_monkey(item)].items.append(item)
        if verbose:
            self.print_monkeys(self.monkeys)
        return self.monkey_business(self.monkeys)

    def part1(self):
        return self.execute(20, lambda x: x // 3)

    def part2(self):
        mod_prod = math.prod([monkey.divider for monkey in self.monkeys])
        return self.execute(10000, lambda x: x % mod_prod)
