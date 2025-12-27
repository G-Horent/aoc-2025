from aoc_solutions.base_solution import BaseSolution
from loguru import logger
import numpy as np


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(name="day_3")

    def solve_puzzle(self, part: int = 1):
        """Solve puzzle for day 3."""
        total_jolts = 0

        for current_input in self.inputs:
            # Turn the input into a list of ints
            input_as_list = [int(x) for x in current_input.__iter__() if x != "\n"]
            if part == 1:
                idx_max_value = np.argmax(input_as_list)
                if idx_max_value == len(input_as_list) - 1:
                    second_max_value = np.max(input_as_list[:idx_max_value])
                    guess = 10 * second_max_value + input_as_list[idx_max_value]
                    total_jolts += guess
                else:
                    # Find the next value that is
                    first_value = input_as_list[idx_max_value]
                    second_value = np.max(input_as_list[idx_max_value + 1 :])
                    guess = first_value * 10 + second_value
                    total_jolts += guess
                logger.debug(f"Max value for row: {guess}")
            elif part == 2:
                # Same logic but we have to find the twelve combination that works
                # Find the largest number in the list which satisfies the inequality
                # idx < len(list)- 1 - #(remaining digits we have to pick)
                list_of_selected_inputs = []
                latest_selected_index = -1
                number_values_to_select = 12
                for idx_value in range(number_values_to_select):
                    idx_max_curr_selection = (
                        len(input_as_list)
                        - 1
                        - (number_values_to_select - idx_value - 1)
                    )
                    curr_index_selected = np.argmax(
                        input_as_list[
                            latest_selected_index + 1 : idx_max_curr_selection + 1
                        ]
                    )
                    list_of_selected_inputs.append(
                        input_as_list[latest_selected_index + 1 + curr_index_selected]
                    )
                    latest_selected_index = (
                        latest_selected_index + 1 + curr_index_selected
                    )

                print(list_of_selected_inputs)

                # Reconstruct the selected value
                guess = sum(
                    [
                        val * (10 ** (number_values_to_select - idx - 1))
                        for idx, val in enumerate(list_of_selected_inputs)
                    ]
                )
                logger.debug(f"Max value for row: {guess}")
                total_jolts += guess

        logger.success(f"Total number of jolts: {total_jolts}")


if __name__ == "__main__":
    sol = Solution()
    sol.solve_puzzle(part=1)
    sol.solve_puzzle(part=2)
