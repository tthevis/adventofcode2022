from adventofcode2022 import Day


class Day10(Day):

    def part1(self):
        cycles = [1]
        for line in self.input:
            if line == 'noop':
                cycles.append(cycles[-1])
            elif line.startswith('addx '):
                cycles.append(cycles[-1])
                cycles.append(cycles[-1] + int(line[5:]))

        sum = 0
        for cycle in [20, 60, 100, 140, 180, 220]:
            sum += cycle * cycles[cycle - 1]
        return sum

    def draw_pixel(self, cycles, reg_x):
        if abs(reg_x - len(cycles) % 40) > 1:
            cycles.append('.')
        else:
            cycles.append('#')

    def to_string(self, cycles):
        res = []
        for i in range(6):
            res.append("".join(cycles[i * 40:(i + 1) * 40]))
        return "\n".join(res)

    def part2(self):
        reg_x = 1
        cycles = []
        for line in self.input:
            if line == 'noop':
                self.draw_pixel(cycles, reg_x)
            elif line.startswith('addx '):
                self.draw_pixel(cycles, reg_x)
                self.draw_pixel(cycles, reg_x)
                reg_x += int(line[5:])
            else:
                assert False

        return self.to_string(cycles)
