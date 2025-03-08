from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    def execute(self, args):
        print(" ".join(args))