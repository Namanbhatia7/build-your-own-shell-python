from app.commands.base import BaseCommand

class echoCommand(BaseCommand):
    def execute(self, args):
        print(" ".join(args))