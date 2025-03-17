import shlex
from app.commands.cd import CdCommand
from app.commands.echo import EchoCommand
from app.commands.exit import ExitCommand
from app.commands.type import TypeCommand
from app.commands.pwd import PwdCommand
from app.commands.ls import LSCommand
from app.service.external_executor import ExternalExecutor

class CommandHandler:
    """Handles command execution and dispatching."""

    def __init__(self):
        self.commands = {
            "cd": CdCommand(),
            "echo": EchoCommand(),
            "exit": ExitCommand(),
            "pwd": PwdCommand(),
            "type": TypeCommand(self),
            "ls": LSCommand(),
        }
        self.external_executor = ExternalExecutor()

    def execute(self, command_line):
        args = shlex.split(command_line)
        if not args:
            return
        
        command, args = args[0], args[1:]

        if command in self.commands:
            self.commands[command].execute(args)
        else:
            self.external_executor.execute(command, args)

