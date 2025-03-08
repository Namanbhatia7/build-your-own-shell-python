# import sys
# import os
# import subprocess
# import shutil

# class Shell:
#     def __init__(self):
#         """Initialize the shell with a command dispatcher."""
#         self.history = []
#         self.commands = {
#             "exit": self.handle_exit,
#             "echo": self.handle_echo,
#             "type": self.handle_type,
#             "history": self.handle_history,
#             "pwd": self.handle_pwd,
#             "cd": self.handle_cd,
#         }
    
#     def handle_cd(self, args):
#         input_path = "".join(args)
#         input_path = os.path.expanduser(input_path)
#         if os.path.exists(input_path):
#             os.chdir(input_path)
#         else:
#             print(f"cd: {input_path}: No such file or directory")

#         return
    
#     def handle_pwd(self, args):
#         """Displays current directory path"""
#         cwd = os.getcwd()

#         print(cwd)
#         return

#     def handle_type(self, args):
#         """Checks if a command is a shell builtin or an executable in PATH."""
#         if not args:
#             print("Usage: type <command>")
#             return

#         input_command = args[0]  # Extract the command name

#         # Check if the command is a built-in
#         if input_command in self.commands:
#             print(f"{input_command} is a shell builtin")
#             return

#         # Check if the command exists in PATH using shutil.which()
#         command_path = shutil.which(input_command)
#         if command_path:
#             print(f"{input_command} is {command_path}")
#         else:
#             print(f"{input_command}: not found")

#     def handle_exit(self, args):
#         """Exit the shell."""
#         exit_code = int(args[0]) if args and args[0].isdigit() else 0
#         sys.exit(exit_code)

#     def handle_echo(self, args):
#         """Echoes back the input."""
#         print(" ".join(args))

#     def handle_history(self, args):
#         """Displays command history."""
#         print("\n".join(self.history))

#     def execute_external_command(self, command, args):
#         """Tries to execute an external system command."""
#         try:
#             result = subprocess.run([command] + args, check=True, text=True, capture_output=True)
#             print(result.stdout, end="")
#         except FileNotFoundError:
#             print(f"{command}: command not found")
#         except subprocess.CalledProcessError as e:
#             print(e.stderr if e.stderr else f"{command}: error occurred")

#     def execute_command(self, command_line):
#         """Parses and executes a command."""
#         args = command_line.split()
#         if not args:
#             return  # Ignore empty input

#         command, args = args[0], args[1:]

#         if command in self.commands:
#             self.commands[command](args)
#         else:
#             self.execute_external_command(command, args)

#     def start(self):
#         """Starts the REPL loop."""
#         while True:
#             sys.stdout.write("$ ")
#             sys.stdout.flush()

#             try:
#                 command_line = input().strip()
#                 if command_line:
#                     self.history.append(command_line)
#                     self.execute_command(command_line)
#             except KeyboardInterrupt:
#                 print("\nType 'exit' to quit.")
#             except EOFError:
#                 print("\nExiting REPL...")
#                 sys.exit(0)


from app.commands.cd import CdCommand
from app.commands.echo import EchoCommand
from app.commands.exit import ExitCommand
from app.commands.pwd import PwdCommand
from app.service.external_executor import ExternalExecutor

class CommandHandler:
    """Handles command execution and dispatching."""

    def __init__(self):
        self.commands = {
            "cd": CdCommand(),
            "echo": EchoCommand(),
            "exit": ExitCommand(),
            "pwd": PwdCommand(),
            # "type": TypeCommand(),
        }
        self.external_executor = ExternalExecutor()

    def execute(self, command_line):
        args = command_line.split()
        if not args:
            return
        
        command, args = args[0], args[1:]

        if command in self.commands:
            self.commands[command].execute(args)
        else:
            self.external_executor.execute(command, args)

