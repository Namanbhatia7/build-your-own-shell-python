import sys
import os
import subprocess

class Shell:
    def __init__(self):
        """Initialize the shell with a command dispatcher."""
        self.history = []
        self.commands = {
            "exit": self.handle_exit,
            "echo": self.handle_echo,
            "type": self.handle_type,
            "history": self.handle_history,
        }

    def handle_type(self, args):
        does_command_exist = lambda: args in self.commands.keys()
        input_command = " ".join(args)

        if does_command_exist:
            print(f"{input_command} is a shell builtin")
        else:
            print(f"{input_command}: not found")

    def handle_exit(self, args):
        """Exit the shell."""
        exit_code = int(args[0]) if args and args[0].isdigit() else 0
        print(f"Exiting with code {exit_code}...")
        sys.exit(exit_code)

    def handle_echo(self, args):
        """Echoes back the input."""
        print(" ".join(args))

    def handle_history(self, args):
        """Displays command history."""
        print("\n".join(self.history))

    def execute_external_command(self, command, args):
        """Tries to execute an external system command."""
        try:
            result = subprocess.run([command] + args, check=True, text=True, capture_output=True)
            print(result.stdout, end="")
        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")

    def execute_command(self, command_line):
        """Parses and executes a command."""
        args = command_line.split()
        if not args:
            return  # Ignore empty input

        command, args = args[0], args[1:]

        if command in self.commands:
            self.commands[command](args)
        else:
            #TODO: Commenting
            # self.execute_external_command(command, args)
            ...

    def start(self):
        """Starts the REPL loop."""
        while True:
            sys.stdout.write("$ ")
            sys.stdout.flush()

            try:
                command_line = input().strip()
                if command_line:
                    self.history.append(command_line)
                    self.execute_command(command_line)
            except KeyboardInterrupt:
                print("\nType 'exit' to quit.")
            except EOFError:
                print("\nExiting REPL...")
                sys.exit(0)
