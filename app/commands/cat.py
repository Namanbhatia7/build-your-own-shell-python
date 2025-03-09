import os
from app.commands.base import BaseCommand

class CatCommand(BaseCommand):
    def execute(self, args):
        if not args:
            print("cat: missing file operand")
            return

        # Check for redirection
        if ">" in args or "1>" in args:
            redirect_symbol = ">" if ">" in args else "1>"
            split_index = args.index(redirect_symbol)
            file_args = args[:split_index]  # Files to read
            output_file = args[split_index + 1]  # Output file

            collected_output = []

            for file in file_args:
                if os.path.exists(file):
                    with open(file, "r") as f:
                        collected_output.append(f.read().strip())
                else:
                    print(f"cat: {file}: No such file or directory")

            if collected_output:
                with open(output_file, "w") as f:
                    f.write("\n".join(collected_output) + "\n")

        else:
            for file in args:
                if os.path.exists(file):
                    with open(file, "r") as f:
                        print(f.read().strip())
                else:
                    print(f"cat: {file}: No such file or directory")
