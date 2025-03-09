import shutil
from app.commands.base import BaseCommand

class TypeCommand(BaseCommand):
    def __init__(self, shell):
        """Accepts a reference to the Shell instance to check built-in commands."""
        self.shell = shell

    def execute(self, args):
        """Checks if a command is an external executable or a shell builtin."""
        if not args:
            print("Usage: type <command>")
            return

        input_command = args[0]  # Extract the command name

        # First, check if the command exists in PATH
        command_path = shutil.which(input_command)
        if command_path:
            print(f"{input_command} is {command_path}")
            return  # Stop here, do not check for built-in

        # If not found in PATH, check if it's a shell built-in
        if input_command in self.shell.commands:
            print(f"{input_command} is a shell builtin")
            return

        # If neither, command is not found
        print(f"{input_command}: not found")
