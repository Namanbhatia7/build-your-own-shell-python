from abc import ABC, abstractmethod

class BaseCommand(ABC):
    """Abstract base class for shell commands."""

    @abstractmethod
    def execute(self, args):
        """Execute the command with given arguments."""
        pass
