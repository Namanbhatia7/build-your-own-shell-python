import sys
from commands.base import BaseCommand

class ExitCommand(BaseCommand):
    def execute(self, args):
        exit_code = int(args[0]) if args and args[0].isdigit() else 0
        sys.exit(exit_code)
