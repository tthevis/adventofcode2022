#
# This test suit picks up all expected results it can find in the 'expected_results' folder
# and runs the respective day/part algorithm based on filename conventions for that result
#

import unittest
import re
import os
from pathlib import Path

import adventofcode2022


class BlackboxTest(unittest.TestCase):
    longMessage = True

    @staticmethod
    def parse_day_part(path_name):
        filename_pattern = re.compile(".*_(\\d+)_(\\d+)")
        match = filename_pattern.search(path_name)
        day, part = match.groups()
        return day, part

    def test_expected_results(self):
        # need to change working directory in order to resolve paths from the main framework
        os.chdir("../")

        path_list = Path("test/expected_results").rglob('result_*')
        for path in path_list:
            path_to_expected_result = str(path)
            day, part = BlackboxTest.parse_day_part(path_to_expected_result)

            with self.subTest(expected_result=path_to_expected_result):
                result = adventofcode2022.main(int(day), int(part))
                f = open(path_to_expected_result, "r")
                expected_result = f.read()
                f.close()
                self.assertEqual(str(result), expected_result)


if __name__ == '__main__':
    unittest.main()
