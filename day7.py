import re

from adventofcode2022 import Day

class Day7(Day):

    def __init__(self, input):
        super().__init__(input)
        self.cur_path = []
        self.dir_sizes = {}
        self.cd_pattern = re.compile("\\$ cd (.+)$")
        self.file_pattern = re.compile("(\\d+) (.*)$")

    def change_directory(self, line):
        directory = self.cd_pattern.findall(line)[0]
        if directory == "/":
            self.cur_path = []
        elif directory == "..":
            self.cur_path.pop()
        else:
            self.cur_path.append(directory)

    def add_file(self, line):
        size, file_name = self.file_pattern.search(line).groups()
        for i in range(len(self.cur_path), 0, -1):
            dir_path = "/".join(self.cur_path[:i])
            self.dir_sizes[dir_path] = self.dir_sizes[dir_path] + int(size) if dir_path in self.dir_sizes else int(size)

    def part1(self):
        for line in self.input:
            if self.cd_pattern.match(line):
                self.change_directory(line)
            if self.file_pattern.match(line):
                self.add_file(line)

        return sum([self.dir_sizes[dir] for dir in self.dir_sizes if self.dir_sizes[dir] <= 100000])

    def part2(self):
        for line in self.input:
            if self.cd_pattern.match(line):
                self.change_directory(line)
            if self.file_pattern.match(line):
                self.add_file(line)

        total_size = sum([self.dir_sizes[dir] for dir in self.dir_sizes if not dir.__contains__("/")])
        free_up_space = 30000000 - (70000000 - total_size)

        return min([val for val in self.dir_sizes.values() if val >= free_up_space])