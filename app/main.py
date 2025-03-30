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
        """Finds all executable files in directories listed in $PATH dynamically."""
        PATH = os.environ["PATH"]
        paths = PATH.split(":")
        executable_commands = []
        for path in paths:
            try:
                for filename in os.listdir(path):
                    fullpath = os.path.join(path, filename)
                    if os.access(fullpath, os.X_OK):
                        executable_commands.append(filename)
            except FileNotFoundError:
                pass
        
        return set(executable_commands)

    def completer(self, text, state):
        """Auto-completes commands from built-in commands and external executables."""
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
