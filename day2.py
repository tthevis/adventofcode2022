from adventofcode2022 import Day


class Day2(Day):

    def play_game(self, game):
        return sum([game[x.strip()] for x in self.input])

    def part1(self):
        game = {
            "A X": 4,
            "A Y": 8,
            "A Z": 3,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 7,
            "C Y": 2,
            "C Z": 6
        }
        return self.play_game(game)

    def part2(self):
        game = {
            "A X": 3,
            "A Y": 4,
            "A Z": 8,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 2,
            "C Y": 6,
            "C Z": 7
        }
        return self.play_game(game)


