import shlex
from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    def redirect(self, args):
        redirect_symbol = ">" if ">" in args else "1>"
        split_index = args.index(redirect_symbol)
        content = " ".join(args[:split_index])  # Content to echo
        output_file = args[split_index + 1]  # Filename

        # Write content to the file
        with open(output_file, "w") as f:
            f.write(content + "\n")

    def execute(self, args):
        original_command = " ".join(args)
        if ">" in args or "1>" in args:
            self.redirect(args=args)
        else:
            print(original_command)
