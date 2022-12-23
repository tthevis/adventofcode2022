import json

from adventofcode2022 import Day
from functools import cmp_to_key


class Day13(Day):

    @staticmethod
    def compare(packet_1, packet_2):
        if isinstance(packet_1, int) and isinstance(packet_2, int):
            return packet_2 - packet_1
        if isinstance(packet_1, list) and isinstance(packet_2, list):
            for i in range(min(len(packet_1), len(packet_2))):
                if Day13.compare(packet_1[i], packet_2[i]) != 0:
                    return Day13.compare(packet_1[i], packet_2[i])
            return len(packet_2) - len(packet_1)
        if isinstance(packet_1, int) and isinstance(packet_2, list):
            return Day13.compare([packet_1], packet_2)
        if isinstance(packet_1, list) and isinstance(packet_2, int):
            return Day13.compare(packet_1, [packet_2])

        # should never be reached
        assert False

    def __init__(self, input):
        super().__init__(input)
        self.packet_pairs = []
        for i in range((len(input) // 3) + 1):
            packet_1 = json.loads(input[i * 3])
            packet_2 = json.loads(input[i * 3 + 1])
            self.packet_pairs.append((packet_1, packet_2))

    def part1(self):
        idx = 0
        idx_lst = []
        for pair in self.packet_pairs:
            idx += 1
            if Day13.compare(pair[0], pair[1]) > 0:
                idx_lst.append(idx)
        return sum(idx_lst)

    def part2(self):
        items = []
        items.append([[2]])
        items.append([[6]])
        for pair in self.packet_pairs:
            items.append(pair[0])
            items.append(pair[1])
        items = sorted(items, key=cmp_to_key(Day13.compare), reverse=True)

        return (items.index([[2]]) + 1) * (items.index([[6]]) + 1)
