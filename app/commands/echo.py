import shlex
from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    def redirect(self, args):
        split_index = args.index(">")
        content = " ".join(args[:split_index])  # Get echo content
        output_file = args[split_index + 1]  # Get filename

        # Write content to the file
        with open(output_file, "w") as f:
            f.write(content + "\n")

    def execute(self, args):
        original_command = " ".join(args)
        if ">" in args:
            self.redirect(args=args)
        else:
            print(original_command)
