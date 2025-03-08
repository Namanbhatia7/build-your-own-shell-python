import shlex
from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    def execute(self, args):
        original_command = " ".join(args)

        print(original_command)