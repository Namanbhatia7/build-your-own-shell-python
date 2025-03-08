import shlex
from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    def execute(self, args):
        original_command = " ".join(args)
        
        # Use shlex to properly parse quotes while keeping spaces inside single quotes
        tokens = shlex.split(original_command, posix=True)

        print(" ".join(tokens))