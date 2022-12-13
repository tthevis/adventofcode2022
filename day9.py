from adventofcode2022 import Day


def init_rope(length):
    rope = []
    for i in range(length):
        rope.append((0, 0))
    return rope


class Day9(Day):

    direction = {
        "R": (1, 0),
        "U": (0, -1),
        "L": (-1, 0),
        "D": (0, 1)
    }

    @staticmethod
    def parse_line(line):
        return Day9.direction[line[0]], int(line[2:])

    @staticmethod
    def add(t1, t2):
        return tuple(map(sum, zip(t1, t2)))

    def move_one_step(self, rope, step):
        former_pos = rope[0]
        rope[0] = self.add(rope[0], step)

        for i in range(1, len(rope)):
            diff_x = rope[i - 1][0] - rope[i][0]
            diff_y = rope[i - 1][1] - rope[i][1]

            delta_x = int(diff_x / abs(diff_x)) if abs(diff_x) > 0 else 0
            delta_y = int(diff_y / abs(diff_y)) if abs(diff_y) > 0 else 0

            if abs(diff_x) > 1 or abs(diff_y) > 1:
                rope[i] = self.add(rope[i], (delta_x, delta_y))

    def move_rope(self, rope_length):
        rope = init_rope(rope_length)
        visited = set()

        for line in self.input:
            step, times = self.parse_line(line)
            for i in range(times):
                self.move_one_step(rope, step)
                visited.add(rope[-1])

        return len(visited)

    def part1(self):
        return self.move_rope(2)

    def part2(self):
        return self.move_rope(10)
