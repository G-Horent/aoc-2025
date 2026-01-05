"""Solution for day 6."""

from aoc_solutions.base_solution import BaseSolution
from operator import mul
from functools import reduce
from loguru import logger


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(name="day_6")

    def solve_puzzle(self, part: int = 1):
        converted_lines = [
            [int(z) for z in x.split(" ") if z not in (" ", "")]
            for x in self.inputs[:-1]
        ]
        instructions = [x for x in self.inputs[-1].split(" ") if x not in (" ", "")]

        nb_cols = len(converted_lines[0])
        total = 0

        for curr_col in range(nb_cols):
            if instructions[curr_col] == "+":
                total += sum(x[curr_col] for x in converted_lines)
            elif instructions[curr_col] == "*":
                total += reduce(mul, [x[curr_col] for x in converted_lines], 1)
            else:
                raise ValueError("Unknown instruction")

        logger.success(f"Sum of all columns: {total}")


if __name__ == "__main__":
    sol = Solution()
    sol.solve_puzzle(part=1)
