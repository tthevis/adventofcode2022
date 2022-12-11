from adventofcode2022 import Day

class Day6(Day):

    def find_marker(self, marker_length):
        for i in range(marker_length, len(self.input[0])):
            if len(set(self.input[0][i-marker_length:i])) == marker_length:
                return i
        return -1

    def part1(self):
        return self.find_marker(4)

    def part2(self):
        return self.find_marker(14)
