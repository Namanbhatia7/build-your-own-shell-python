import os
from app.commands.base import BaseCommand

class CdCommand(BaseCommand):
    def execute(self, args):
        if not args:
            print("cd: missing argument")
            return

        path = os.path.expanduser(args[0])
        if os.path.isdir(path):
            os.chdir(path)
        else:
            print(f"cd: {path}: No such file or directory")
