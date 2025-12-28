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

        # Convolve with filter
        flt = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

        count_neighbors = correlate2d(array.astype(int), flt, mode="same", fillvalue=0)

        count_of_piles_to_move = np.logical_and(count_neighbors < 4, array).sum()

        logger.info(f"Number of piles that can be moved: {count_of_piles_to_move}")

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
            print
            input_as_list = [
                mapping_chr_to_bool[x] for x in curr_row.__iter__() if x != "\n"
            ]

            array[idx_row, :] = np.array(input_as_list, dtype=bool)

        return array


if __name__ == "__main__":
    sol = Solution()
    sol.solve_puzzle()
