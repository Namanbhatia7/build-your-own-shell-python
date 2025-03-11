import shlex
from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    def redirect(self, args):
        if "2>" in args:
            redirect_symbol = "2>"
            split_index = args.index(redirect_symbol)
            output_file = args[split_index + 1]
            content = ""  # Since `echo` has no error output, writing an empty string
        else:
            redirect_symbol = ">" if ">" in args else "1>"
            split_index = args.index(redirect_symbol)
            output_file = args[split_index + 1]
            content = " ".join(args[:split_index])

        # Write content to the file
        with open(output_file, "w") as f:
            f.write(content + "\n")

    def execute(self, args):
        if ">" in args or "1>" in args or "2>" in args:
            self.redirect(args=args)
        else:
            print(" ".join(args))
