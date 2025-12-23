from abc import ABC, abstractmethod
import os.path as osp


class BaseSolution(ABC):
    """Base class for solutions."""

    def __init__(self, name: str, input_path: str = "inputs"):
        self.name = name
        self.input_path = input_path
        self.inputs = self.load_input_file()

    def load_input_file(self) -> list[str]:
        """Load the input file."""

        with open(osp.join(self.input_path, f"{self.name}.txt"), "r") as file:
            inputs = file.readlines()

        return inputs

    @abstractmethod
    def solve_puzzle(self):
        return NotImplementedError
