import re
import sys

from adventofcode2022 import Day


class Day15(Day):

    sensor_beacon_regex = re.compile("Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)")

    @staticmethod
    def manhattan_distance(xy_1, xy_2):
        return abs(xy_1[0] - xy_2[0]) + abs(xy_1[1] - xy_2[1])

    def __init__(self, input):
        super().__init__(input)
        self.occupied = {}
        self.sensor2beacon = {}
        for line in self.input:
            xs, ys, xb, yb = [int(x) for x in Day15.sensor_beacon_regex.search(line).groups()]
            self.sensor2beacon[(xs, ys)] = (xb, yb)

    # returns all the x coordinates as a list for a given row that are covered by a given signal
    # and can therefore not contain a beacon
    def sensor_coverage(self, sensor_pos, target_row):
        sensor_range = Day15.manhattan_distance(sensor_pos, self.sensor2beacon[sensor_pos])
        row_distance = abs(sensor_pos[1] - target_row)
        if sensor_range < row_distance:
            return []
        else:
            row_coverage = sensor_range - row_distance
            return [i for i in range(sensor_pos[0] - row_coverage, sensor_pos[0] + row_coverage + 1)]

    def part1(self):
        result = set([])
        y = 2000000
        for sensor in self.sensor2beacon:
            result.update(self.sensor_coverage(sensor, y))
        for sensor, beacon in self.sensor2beacon.items():
            if sensor[1] == y and sensor[0] in result:
                result.remove(sensor[0])
            if beacon[1] == y and beacon[0] in result:
                result.remove(beacon[0])

        return len(result)

    @staticmethod
    def intersection(p1, p2, p3, p4):
        x = ((p1[0] * p2[1] - p1[1] * p2[0]) * (p3[0] - p4[0]) - (p1[0] - p2[0]) * (p3[0] * p4[1] - p3[1] * p4[0])) / (
                (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]))
        y = ((p1[0] * p2[1] - p1[1] * p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] * p4[1] - p3[1] * p4[0])) / (
                (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0]))

        return x, y

    def part2(self):
        search_range = range(0, 4000000)
        lines = []
        for s1 in self.sensor2beacon:
            for s2 in [s for s in self.sensor2beacon if s[0] >= s1[0]]:
                sensor_dist = Day15.manhattan_distance(s1, s2)
                if sensor_dist == 2 + Day15.manhattan_distance(s1, self.sensor2beacon[s1]) + \
                        Day15.manhattan_distance(s2, self.sensor2beacon[s2]):
                    line_p1 = (s1[0] + Day15.manhattan_distance(s1, self.sensor2beacon[s1]) + 1, s1[1])
                    line_p2 = (s1[0], s1[1] + Day15.manhattan_distance(s1, self.sensor2beacon[s1]) + 1 if s2[1] >
                        s1[1] else s1[1] - Day15.manhattan_distance(s1, self.sensor2beacon[s1]) - 1)
                    lines.append((line_p1, line_p2))
        assert len(lines) == 2

        x, y = self.intersection(lines[0][0], lines[0][1], lines[1][0], lines[1][1])

        return 4000000 * int(x) + int(y)
