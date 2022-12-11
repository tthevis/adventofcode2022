from adventofcode2022 import Day

class Day3(Day):

    @staticmethod
    def priority(x):
        if 'a' <= x <= 'z':
            return ord(x) - 96
        if 'A' <= x <= 'Z':
            return ord(x) - 38

    @staticmethod
    def intersection(l1: list, l2: list, l3: list):
        return list(set([x for x in l1 if x in l2 and x in l3]))

    def part1(self):
        result = []
        for line in self.input:
            line = line.strip()
            split_pos = int(len(line) / 2)
            result += list(set([self.priority(c) for c in line[:split_pos] if c in line[split_pos:]]))

        return sum(result)

    def part2(self):
        res = 0
        for i in range(0, len(self.input), 3):
            res += sum(list(map(lambda x: Day3.priority(x), Day3.intersection(self.input[i], self.input[i+1], self.input[i+2]))))
        return res
