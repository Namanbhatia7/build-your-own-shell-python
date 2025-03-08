from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    def execute(self, args):
        print(args)
        shell_print = " ".join(args)
        shell_print = shell_print.replace("'", "")
        print(shell_print)