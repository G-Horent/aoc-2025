from aoc_solutions.base_solution import BaseSolution
from loguru import logger


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(name="day_2")

    def solve_puzzle(self, part: int = 1):
        """Solve today's puzzle."""
        total_invalid_ids = 0
        for current_range in self.inputs[0].split(","):
            # Interpret the range
            lower_range, upper_range = [int(x) for x in current_range.split("-")]

            # Check for invalid IDs in the given range
            for curr_value in range(lower_range, upper_range + 1):
                # Check if value is invalid
                if self.is_invalid_value(curr_value, part=part):
                    logger.success(f"Adding {curr_value} as invalid value.")
                    total_invalid_ids += curr_value

        print(f"Sum of invalid IDs: {total_invalid_ids}")

    def is_invalid_value(self, value: int, part: int) -> bool:
        """Check if a value is invalid or not."""
        # Build a list of all possible substrings of size N//2
        value_str = str(value)
        n = len(value_str)

        # logger.warning(f"Starting solving for part {part}")

        if part == 1:
            # If size is not pair, the value
            if n % 2 != 0:
                return False

            if value_str[: n // 2] == value_str[n // 2 :]:
                logger.info(
                    f"Found {value_str} as incorrect ID, pattern {value_str[: n // 2]} repeated twice."
                )
                return True
            return False
        else:
            # Check substrings of increasing size
            max_subtr_length = n // 2
            for sub_size in range(1, max_subtr_length + 1):
                sub_str = value_str[:sub_size]
                if (
                    all(
                        value_str[k : k + sub_size] == sub_str
                        for k in range(0, n, sub_size)
                    )
                    and n > 1
                ):
                    logger.info(
                        f"Found {value_str} as incorrect ID, pattern {sub_str} repeated all times."
                    )
                    return True

            return False


if __name__ == "__main__":
    sol = Solution()
    sol.solve_puzzle()
    sol.solve_puzzle(part=2)
