import shutil
from commands.base import BaseCommand

class TypeCommand(BaseCommand):
    def execute(self, args):
        """Checks if a command is a shell builtin or an executable in PATH."""
        if not args:
            print("Usage: type <command>")
            return

        input_command = args[0]  # Extract the command name

        # Check if the command is a built-in
        if input_command in self.commands:
            print(f"{input_command} is a shell builtin")
            return

        # Check if the command exists in PATH using shutil.which()
        command_path = shutil.which(input_command)
        if command_path:
            print(f"{input_command} is {command_path}")
        else:
            print(f"{input_command}: not found")