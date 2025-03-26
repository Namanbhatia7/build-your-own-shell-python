from os import read
import sys
import readline
from app.service.command_handler import CommandHandler
from app.service.history_manager import HistoryManager
from app.utils.constants import BUILT_IN_COMMANDS

class Shell:
    """Main shell REPL loop."""

    def __init__(self):
        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()
        self.tab_completer()
    
    def tab_completer(self):
        readline.parse_and_bind("tab: complete")
        print(readline.set_completer(self.completer))

    
    def completer(self, text, state):
        matches = [cmd + " " for cmd in BUILT_IN_COMMANDS if cmd.startswith(text)]
        return matches[state] if state < len(matches) else None


    def start(self):
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
