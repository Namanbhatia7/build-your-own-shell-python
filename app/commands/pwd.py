import os
from app.commands.base import BaseCommand

class PwdCommand(BaseCommand):
    def execute(self, args):
        """Displays current directory path"""
        cwd = os.getcwd()

        print(cwd)
        return