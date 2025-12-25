"""Solution for day 1."""

from aoc_solutions.base_solution import BaseSolution
from loguru import logger


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(name="day_1")

    def solve_puzzle(self):
        current_position = 50

        count_zeros = 0
        total_crossing_zeros = 0

        for current_change in self.inputs:
            former_position = current_position
            logger.debug(f"Receiving input {current_change}")
            if current_change.startswith("L"):
                moving_input = int(current_change[1:])
                corrected_input = moving_input % 100
                logger.debug(f"Corrected input {corrected_input}")
                current_position = current_position - corrected_input
                logger.debug(f"New incorrected position: {current_position}")
            elif current_change.startswith("R"):
                moving_input = int(current_change[1:])
                corrected_input = moving_input % 100
                current_position = current_position + corrected_input
                logger.debug(f"Corrected input {corrected_input}")

            # Count the number of times we crossed zero
            number_of_crossing_zeros = moving_input // 100
            logger.debug(
                f"Number of times the lock crossed zero during the rotation: {number_of_crossing_zeros}"
            )

            # Reset the position if out of bounds
            if current_position == 0:
                count_zeros += 1
            elif current_position < 0:
                logger.debug("Position negative out of bounds")
                if former_position != 0:
                    number_of_crossing_zeros += 1
                current_position = 100 + current_position
                logger.debug(f"New corrected position: {current_position}")
            elif current_position >= 100:
                if current_position == 100:
                    logger.success("Reached 100, setting back to 0")
                    count_zeros += 1
                    current_position = 0
                else:
                    number_of_crossing_zeros += 1
                    current_position = current_position % 100
                    logger.debug(f"New corrected position: {current_position}")

            logger.info(f"Lock position at the end of this turn: {current_position}")

            total_crossing_zeros += number_of_crossing_zeros

        print(f"Final position: {current_position}")
        print(f"Number of zeros: {count_zeros}")
        print(f"Total crossing zeros: {total_crossing_zeros}")
        print(f"Final total count: {count_zeros + total_crossing_zeros}")


if __name__ == "__main__":
    sol = Solution()
    sol.solve_puzzle()
