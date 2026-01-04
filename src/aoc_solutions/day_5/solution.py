"""Solution for day 5."""

from __future__ import annotations
from aoc_solutions.base_solution import BaseSolution
from loguru import logger
from typing import Optional


class Interval:
    def __init__(self, lower: int, upper: int):
        assert lower <= upper, (
            f"Lower value {lower} should be at lower than upper value {upper}"
        )
        self.lower = lower
        self.upper = upper

    def restrict_intersected_interval(
        self, inter: Interval
    ) -> Optional[list[Interval]]:
        """Restrict the current interval if the other interval is not"""

        # No intersection.
        if (inter.upper < self.lower) or (self.upper < inter.lower):
            return [self]

        # Incoming interval fully includes the current interval: return None
        elif (inter.lower <= self.lower) and (inter.upper >= self.upper):
            return None

        # Incoming interval is fully included in current interval
        elif (self.lower <= inter.lower) and (self.upper >= inter.upper):
            # Return two intervals
            if self.lower == inter.lower:
                return [Interval(inter.upper + 1, self.upper)]
            elif self.upper == inter.upper:
                return [Interval(self.lower, inter.lower - 1)]
            else:
                return [
                    Interval(self.lower, inter.lower - 1),
                    Interval(inter.upper + 1, self.upper),
                ]

        # Left intersection
        elif (inter.lower <= self.lower) and (inter.upper < self.upper):
            return [Interval(inter.upper + 1, self.upper)]

        # Right interval
        elif (inter.lower >= self.lower) and (inter.upper > self.upper):
            return [Interval(self.lower, inter.lower - 1)]

        else:
            raise ValueError(
                f"Unknown case.\nCurrent interval: [{self.lower} - {self.upper}]\nIncoming interval: [{inter.lower} - {inter.upper}]"
            )

    def interval_len(self) -> int:
        """Return the interval length."""
        return self.upper - self.lower + 1


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(name="day_5")

    def solve_puzzle(self, part: int = 1):
        """Solve puzzle for day 5."""
        # First, split and interpret the inputs
        idx_blank = self.inputs.index("\n")
        list_ranges_str = self.inputs[:idx_blank]
        list_ingredients_str = self.inputs[idx_blank + 1 :]

        all_ranges = [
            (int(x.split("-")[0]), int(x.split("-")[1][:-1])) for x in list_ranges_str
        ]
        all_ingredients = [int(x[:-1]) for x in list_ingredients_str]

        total_number_fresh_ingredients = 0

        if part == 1:
            for current_ingredient in all_ingredients:
                # Check all intervals to see if the ingredient is fresh
                for curr_range_low, curr_range_high in all_ranges:
                    if (curr_range_low <= current_ingredient) and (
                        current_ingredient <= curr_range_high
                    ):
                        logger.info(
                            f"Ingredient {current_ingredient} is in interval [{curr_range_low} - {curr_range_high}]"
                        )
                        total_number_fresh_ingredients += 1
                        break

            logger.success(
                f"Total number of fresh ingredients: {total_number_fresh_ingredients}"
            )
        elif part == 2:
            # Answer for part 2
            all_intervals = [Interval(rng[0], rng[1]) for rng in all_ranges]

            # Check all intervals
            checked_intervals: list[Interval] = []
            for curr_interval in all_intervals:
                if len(checked_intervals) == 0:
                    checked_intervals.append(curr_interval)

                for idx, previous_checked_interval in enumerate(checked_intervals):
                    if idx == 0:
                        curr_checked_interval = curr_interval
                    if isinstance(curr_checked_interval, list):
                        list_intersections = [
                            x.restrict_intersected_interval(previous_checked_interval)
                            for x in curr_checked_interval
                        ]
                        cleaned_list = []
                        for curr_list in list_intersections:
                            if isinstance(curr_list, Interval):
                                cleaned_list.append(curr_list)
                            elif curr_list is None:
                                continue
                            else:
                                cleaned_list.extend(curr_list)

                        curr_checked_interval = cleaned_list
                    else:
                        curr_checked_interval = (
                            curr_checked_interval.restrict_intersected_interval(
                                previous_checked_interval
                            )
                        )

                    if curr_checked_interval is None:
                        break

                if curr_checked_interval is None:
                    continue
                else:
                    checked_intervals.extend(curr_checked_interval)

            sum_all_ranges = sum([x.interval_len() for x in checked_intervals])

            logger.success(f"Final sum of all ranges: {sum_all_ranges}")


if __name__ == "__main__":
    sol = Solution()
    sol.solve_puzzle(part=1)
    sol.solve_puzzle(part=2)
