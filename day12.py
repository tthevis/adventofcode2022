from adventofcode2022 import Day


class BFS:

    def __init__(self, adjacency_callback, target_validation_callback):
        self.adjacency_callback = adjacency_callback
        self.target_validation_callback = target_validation_callback

    def shortest_path(self, start):
        visited = set()
        queue = [start]
        trace_back = {}
        target = None

        while len(queue) > 0 and target is None:
            current_node = queue.pop(0)
            visited.add(current_node)

            for adjacent_node in self.adjacency_callback(current_node):
                if adjacent_node not in visited and adjacent_node not in queue:
                    trace_back[adjacent_node] = current_node
                    queue.append(adjacent_node)
                    if self.target_validation_callback(adjacent_node):
                        target = adjacent_node

        assert target in trace_back
        result = [target]
        while result[0] != start:
            result.insert(0, trace_back[result[0]])

        return result


class Day12(Day):

    @staticmethod
    def find_pos(character, grid, find_all=False):
        result = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == character:
                    result.append((row, col))
                    if not find_all:
                        return row, col
        # should never be reached
        return result

    def adjacent_nodes(self, pos: tuple, upwards=True):
        row, col = pos[0], pos[1]
        height = self.input[row][col]
        result = []
        for candidate in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            # check whether pos is in grid
            if not 0 <= candidate[0] < len(self.input) or not 0 <= candidate[1] < len(self.input[0]):
                continue
            # check whether transition is allowed due to height restriction
            if upwards and ord(self.input[candidate[0]][candidate[1]]) - ord(height) > 1:
                continue
            elif not upwards and ord(height) - ord(self.input[candidate[0]][candidate[1]]) > 1:
                continue
            result.append(candidate)
        return result

    def adjacent_nodes_upwards(self, pos: tuple):
        return self.adjacent_nodes(pos, upwards=True)

    def adjacent_nodes_downwards(self, pos: tuple):
        return self.adjacent_nodes(pos, upwards=False)

    def part1(self):
        start = Day12.find_pos('S', self.input)
        target = Day12.find_pos('E', self.input)
        self.input[start[0]] = self.input[start[0]].replace("S", "a")
        self.input[target[0]] = self.input[target[0]].replace("E", "z")

        path = BFS(self.adjacent_nodes_upwards, lambda x: x == target).shortest_path(start)
        return len(path) - 1

    def part2(self):
        start = Day12.find_pos('S', self.input)
        target = Day12.find_pos('E', self.input)
        self.input[start[0]] = self.input[start[0]].replace("S", "a")
        self.input[target[0]] = self.input[target[0]].replace("E", "z")

        path = BFS(self.adjacent_nodes_downwards, lambda x: self.input[x[0]][x[1]] == 'a').shortest_path(target)
        return len(path) - 1
