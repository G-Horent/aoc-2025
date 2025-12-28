"""Solution for day 4."""

from aoc_solutions.base_solution import BaseSolution
from loguru import logger
import numpy as np
from scipy.signal import correlate2d


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(name="day_4")

    def solve_puzzle(self, part: int = 1):
        """Solve puzzle for day 4."""

        array = self.convert_input_to_array()
        flt = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        if part == 1:
            # Convolve with filter
            count_neighbors = correlate2d(
                array.astype(int), flt, mode="same", fillvalue=0
            )

            count_of_piles_to_move = np.logical_and(count_neighbors < 4, array).sum()

            logger.info(f"Number of piles that can be moved: {count_of_piles_to_move}")

        elif part == 2:
            # Iteratively process.
            total_number_of_piles_removed = 0
            number_of_piles_removed_this_round = -1

            while number_of_piles_removed_this_round != 0:
                count_neighbors = correlate2d(
                    array.astype(int), flt, mode="same", fillvalue=0
                )
                piles_to_be_removed = np.logical_and(count_neighbors < 4, array)
                number_of_piles_removed_this_round = piles_to_be_removed.sum()

                # Update the current array of piles
                array = (array.astype(int) - piles_to_be_removed.astype(int)).astype(
                    bool
                )

                logger.info(
                    f"Number of piles removed this round: {number_of_piles_removed_this_round}"
                )

                total_number_of_piles_removed += number_of_piles_removed_this_round

            logger.success(
                f"Total number of piles removed: {total_number_of_piles_removed}"
            )

    def convert_input_to_array(self) -> np.ndarray:
        """Convert puzzle input to Numpy array.

        Returns
        -------
        np.ndarray
            The input converted as a boolean array.
        """
        mapping_chr_to_bool = {".": False, "@": True}
        n_rows, n_cols = len(self.inputs), len(self.inputs[0]) - 1

        array = np.zeros((n_rows, n_cols), dtype=bool)

        for idx_row, curr_row in enumerate(self.inputs):
            input_as_list = [
                mapping_chr_to_bool[x] for x in curr_row.__iter__() if x != "\n"
            ]

            array[idx_row, :] = np.array(input_as_list, dtype=bool)

        return array


if __name__ == "__main__":
    sol = Solution()
    sol.solve_puzzle(part=1)
    sol.solve_puzzle(part=2)
