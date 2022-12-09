#
# This test suit picks up all expected results it can find in the 'expected_results' folder
# and runs the respective day/part algorithm based on filename conventions for that result
#

import unittest
from pathlib import Path
import os
import re

import adventofcode2022


class MyTestCase(unittest.TestCase):

    def parse_day_part(self, path_name):
        pattern = re.compile('.*_(\d+)_(\d+)')
        match = pattern.search(path_name)
        day, part = match.groups()
        return day, part

    def test_expected_results(self):
        # need to change working directory in order to resolve paths from the main framework
        os.chdir("../")
        pathlist = Path("test/expected_results").rglob('result_*')
        for path in pathlist:
            # because path is object not string
            path_in_str = str(path)
            day, part = self.parse_day_part(path_in_str)
            result = adventofcode2022.main(int(day), int(part))

            f = open(path_in_str, "r")
            expected_result = f.read()
            f.close()
            print("run black box test for day {} part {}".format(day, part))
            assert str(result) == str(expected_result), "result '{}' does not match expected result '{}'".format(result, expected_result)
            print("OK")


if __name__ == '__main__':
    unittest.main()
