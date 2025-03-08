class HistoryManager:
    """Manages shell command history."""

    def __init__(self):
        self.history = []

    def add(self, command):
        self.history.append(command)

    def show(self):
        for i, command in enumerate(self.history, start=1):
            print(f"{i}: {command}")
