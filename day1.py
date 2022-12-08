from adventofcode2022 import Day


class Day1(Day):

    def group_sums(self):
        nested_groups = list(map(lambda sublst : sublst.split("\n"), "".join(self.input).split("\n\n")))
        group_sums = list(map(lambda group: sum([int(x) for x in group]), nested_groups))
        return group_sums

    def part1(self):
        return max(self.group_sums())

    def part2(self):
        return sum(sorted(self.group_sums(), reverse=True)[0:3])
