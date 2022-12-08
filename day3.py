from adventofcode2022 import Day

class Day3(Day):

    @staticmethod
    def priority(x):
        if 'a' <= x <= 'z':
            return ord(x) - 96
        if 'A' <= x <= 'Z':
            return ord(x) - 38

    def part1(self):
        result = []
        for line in self.input:
            line = line.strip()
            split_pos = int(len(line) / 2)
            result += list(set([self.priority(c) for c in line[:split_pos] if c in line[split_pos:]]))

        return sum(result)
