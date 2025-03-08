# import sys

# from app.service.command_handler import Shell

# def execute_repl():
#     while True:
#         sys.stdout.write("$ ")
#         command = input().strip()

#         if command == "exit 0":
#             sys.exit(0)  # Exit with status code 0

#         if command.startswith("echo "):
#             echo_statement = command[5:]
#             print(echo_statement)
#         else:
#             print(f'{command}: command not found') # throw invalid command

# def main():
#     # Uncomment this block to pass the first stage
#     # sys.stdout.write("$ ")
#     shell_executor = Shell()
#     shell_executor.start()


# if __name__ == "__main__":
#     main()

import sys
from app.service.command_handler import CommandHandler
from app.service.history_manager import HistoryManager

class Shell:
    """Main shell REPL loop."""

    def __init__(self):
        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()

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
