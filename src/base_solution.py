from abc import ABC, abstractmethod


class BaseSolution(ABC):
    """Base class for solutions."""

    def __init__(self, input_path: str):
        self.input_path = input_path

    def load_input_file(self) -> list[str]:
        """Load the input file."""

    @abstractmethod
    def solve_puzzle(self):
        return NotImplementedError
