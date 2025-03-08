import shlex
from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    def execute(self, args):
        parsed_args = shlex.split(" ".join(args))
        print(" ".join(parsed_args))