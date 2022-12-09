from adventofcode2022 import Day
import re

class Day4(Day):

    regex = re.compile('(\d+)-(\d+),(\d+)-(\d+)')

    @staticmethod
    def parse_line(line: str) -> (int, int, int, int):
        match = Day4.regex.search(line)
        return tuple(map(lambda x: int(x), match.groups()))

    def part1(self):
        res = 0
        for line in self.input:
            f1, t1, f2, t2 = self.parse_line(line)
            if (f1 <= f2 and t1 >= t2) or (f1 >= f2 and t1 <= t2):
                res += 1
        return res

    def part2(self):
        res = 0
        for line in self.input:
            f1, t1, f2, t2 = self.parse_line(line)
            if (f1 <= f2 <= t1) or (f2 <= f1 <= t2):
                res += 1
        return res
