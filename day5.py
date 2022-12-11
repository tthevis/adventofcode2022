from adventofcode2022 import Day
import re


class Day5(Day):

    def __init__ (self, input):
        super().__init__(input)
        self.crates = [
            ['Q', 'M', 'G', 'C', 'L'],
            ['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'],
            ['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'],
            ['J', 'F', 'D', 'V', 'Q', 'P'],
            ['N', 'F', 'N', 'S', 'L', 'B', 'T'],
            ['R', 'N', 'V', 'H', 'C', 'D', 'P'],
            ['H', 'C', 'T'],
            ['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'],
            ['Z', 'F', 'H', 'G']
        ]
        self.move_pattern = re.compile("move (\\d+) from (\\d+) to (\\d+)")

    def execute_operation(self, line, batch=False):
        reps, source, target = self.move_pattern.search(line).groups()

        moving = self.crates[int(source) - 1][-int(reps):]
        if batch == False:
            moving = moving[::-1]
        self.crates[int(source) - 1] = self.crates[int(source) - 1][:-int(reps)]
        self.crates[int(target) - 1].extend(moving)


    def part1(self):
        for line in self.input:
            if self.move_pattern.match(line):
                self.execute_operation(line)
        return "".join(list(map(lambda l: l[-1], self.crates)))

    def part2(self):
        for line in self.input:
            if self.move_pattern.match(line):
                self.execute_operation(line, batch=True)
        return "".join(list(map(lambda l: l[-1], self.crates)))
