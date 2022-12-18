import unittest
from day11 import Monkey


class MonkeyTestCase(unittest.TestCase):
    def test_pase_numbers_from_string(self):
        result = Monkey.parse_numbers_from_string("61, 70, 76, 69, 82, 56")
        self.assertEqual(result, [61, 70, 76, 69, 82, 56])

    def test_change_item_1(self):
        monkey = Monkey("m1", "61, 70, 76, 69, 82, 56", "new = old + 2", "divisible by 17 If true then throw to monkey 5 If false then throw to monkey 3")
        result = monkey.inspect(14)
        self.assertEqual(result, 16)

    def test_change_item_2(self):
        monkey = Monkey("m1", "61, 70, 76, 69, 82, 56", "new = old * old", "divisible by 17 If true then throw to monkey 5 If false then throw to monkey 3")
        result = monkey.inspect(12)
        self.assertEqual(result, 144)

    def test_next_monkey_true(self):
        monkey = Monkey("m1", "61, 70, 76, 69, 82, 56", "new = old * old", "divisible by 17 If true then throw to monkey 5 If false then throw to monkey 3")
        result = monkey.next_monkey(34)
        self.assertEqual(result, 5)

    def test_next_monkey_false(self):
        monkey = Monkey("m1", "61, 70, 76, 69, 82, 56", "new = old * old",
                        "divisible by 17 If true then throw to monkey 5 If false then throw to monkey 3")
        result = monkey.next_monkey(33)
        self.assertEqual(result, 3)



if __name__ == '__main__':
    unittest.main()
