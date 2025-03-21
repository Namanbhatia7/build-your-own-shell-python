from abc import ABC, abstractmethod

class BaseCommand(ABC):
    """Abstract base class for shell commands."""
    REDIRECT_SYMBOLS = [">", "1>", "2>", ">>", "1>>", "2>>"]

    @abstractmethod
    def execute(self, args):
        """Execute the command with given arguments."""
        pass
