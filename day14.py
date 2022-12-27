from adventofcode2022 import Day


class Cave:

    def __init__(self, rock_structure):
        self.occupied_positions = {}
        self.min_x = 500
        self.max_x = 500
        self.max_depth = 0
        for row in rock_structure:
            corners = row.split(" -> ")
            for i in range(len(corners) - 1):
                x1, y1 = corners[i].split(",")
                x2, y2 = corners[i + 1].split(",")
                for x in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
                    for y in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
                        self.occupied_positions[(x, y)] = '#'
                        self.min_x = min(self.min_x, x)
                        self.max_x = max(self.max_x, x)
                        self.max_depth = max(self.max_depth, y)

    def print(self):
        print("min x = {}, max x = {}, max depth = {}".format(self.min_x, self.max_x, self.max_depth))
        for j in range(self.max_depth + 1):
            row = []
            for i in range(self.min_x, self.max_x + 1):
                row.append('.' if (i, j) not in self.occupied_positions else self.occupied_positions[(i, j)])
            print("".join(row))

    def resting_position(self, pos):
        x, y = pos[:]
        if x < self.min_x or x > self.max_x or y > self.max_depth:
            return None

        for cand in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
            if cand not in self.occupied_positions:
                return self.resting_position(cand)

        return pos

    def resting_position_solid_ground(self, pos):
        x, y = pos[:]
        if y + 1 == self.max_depth + 2:
            return pos
        for cand in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
            if cand not in self.occupied_positions:
                return self.resting_position_solid_ground(cand)
        return pos

    def pour(self, pos, shape='o', solid=False, verbose=False):
        position = None
        if not solid:
            position = self.resting_position(pos)
        else:
            position = self.resting_position_solid_ground(pos)
        if position is not None:
            self.occupied_positions[position] = shape
            if verbose:
                self.print()
        return position


class Day14(Day):

    def part1(self):
        cave = Cave(self.input)
        i = 0
        while cave.pour((500, 0)) is not None:
            i += 1
        return i

    def part2(self):
        cave = Cave(self.input)
        i = 0
        while cave.pour((500, 0), solid=True) != (500, 0):
            i += 1
        return i + 1
