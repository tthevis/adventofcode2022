from adventofcode2022 import Day


class Day1(Day):

    def group_sums(self):
        sums = []
        curr_sum = 0
        for line in self.input:
            if len(line) == 0:
                sums.append(curr_sum)
                curr_sum = 0
            else:
                curr_sum += int(line)
        sums.append(curr_sum)
        return sums

    def part1(self):
        return max(self.group_sums())

    def part2(self):
        return sum(sorted(self.group_sums(), reverse=True)[0:3])
