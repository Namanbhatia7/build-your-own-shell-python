import sys
import readline
import os
from app.service.command_handler import CommandHandler
from app.service.history_manager import HistoryManager
from app.utils.constants import BUILT_IN_COMMANDS

class Shell:
    """Main shell REPL loop."""

    def __init__(self):
        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()
        self.setup_tab_completion()

    def setup_tab_completion(self):
        """Sets up tab completion for built-in and external commands."""
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.completer)

    def get_executables_in_path(self):
        """Finds all executable files in directories listed in $PATH."""
        paths = os.environ.get("PATH", "").split(os.pathsep)
        executables = set()

        for path in paths:
            if os.path.isdir(path):
                try:
                    for file in os.listdir(path):
                        file_path = os.path.join(path, file)
                        if os.access(file_path, os.X_OK) and os.path.isfile(file_path):
                            executables.add(file)
                except PermissionError:
                    continue  # Skip directories without read access

        return executables

    def completer(self, text, state):
        """Auto-completes commands from built-in commands and system executables."""
        all_commands = BUILT_IN_COMMANDS.union(self.get_executables_in_path())
        matches = [cmd + " " for cmd in all_commands if cmd.startswith(text)]
        return matches[state] if state < len(matches) else None

    def start(self):
        """Starts the shell REPL loop."""
        while True:
            sys.stdout.write("$ ")
            sys.stdout.flush()

            try:
                command_line = input().strip()
                if command_line:
                    self.history_manager.add(command_line)
                    self.command_handler.execute(command_line)
            except KeyboardInterrupt:
                print("\nType 'exit' to quit.")
            except EOFError:
                print("\nExiting shell...")
                sys.exit(0)

def main():
    shell = Shell()
    shell.start()

if __name__ == "__main__":
    main()
