from adventofcode2022 import Day


class Day8(Day):

    #
    #  Returns the trees to the left from a given position (i,j) as seen from the given position, i.e. the first
    #  tree in the resulting list is the one directly next to (i,j): (i, j-1)
    #
    def trees_left(self, i, j):
        return self.input[i][:j][::-1]

    #
    #  Returns the trees above given position (i,j) as seen from the given position, i.e. the first
    #  tree in the resulting list is the one directly next to (i,j): (i - 1, j)
    #
    def trees_above(self, i, j):
        return "".join([self.input[k][j] for k in range(i)])[::-1]

    def trees_right(self, i, j):
        return self.input[i][j + 1:]

    def trees_below(self, i, j):
        return "".join([self.input[k][j] for k in range(i + 1, len(self.input))])

    @staticmethod
    def max(trees):
        return max([int(t) for t in trees])

    def part1(self):
        visible_tree_count = 2 * len(self.input) + 2 * len(self.input[0]) - 4
        for i in range(1, len(self.input) - 1):
            for j in range(1, len(self.input[i]) - 1):
                height = int(self.input[i][j])
                if self.max(self.trees_left(i, j)) < height or \
                        self.max(self.trees_right(i, j)) < height or \
                        self.max(self.trees_above(i, j)) < height or \
                        self.max(self.trees_below(i, j)) < height:
                    visible_tree_count += 1
        return visible_tree_count

    @staticmethod
    def blocked_view(height, trees):
        dist = 0
        for t in trees:
            dist += 1
            if int(t) >= height:
                break
        return dist

    def scenic_score(self, i, j):
        height = int(self.input[i][j])
        return self.blocked_view(height, self.trees_left(i, j)) * \
            self.blocked_view(height, self.trees_right(i, j)) * \
            self.blocked_view(height, self.trees_above(i, j)) * \
            self.blocked_view(height, self.trees_below(i, j))

    def part2(self):
        return max([self.scenic_score(i, j) for i in range(1, len(self.input) - 1)
                    for j in range(1, len(self.input[i]) - 1)])
