# About
Contains code for the puzzles of the 2022 edition of AdventOfCode (https://adventofcode.com/2022).

The idea is to have a simple framework that is able to dynamically instantiate and execute the solution
algorithms: `adventofcode2022.py`.
For each day a file `day{\n+}` is expected that contains a small class which knows how to handle the two
assignements `part1()` and `part2()` for the respective day.
The `input` directory stores the input files for each day. 
A generic unit test `test/blackboxtest.py` executes test runs for each file stored in the 
`test/expected_results` folder.
