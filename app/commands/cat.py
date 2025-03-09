import os
from app.commands.base import BaseCommand

class CatCommand(BaseCommand):
    def execute(self, args):
        if not args:
            print("cat: missing file operand")
            return

        collected_output = []  # Store file contents

        # Check for redirection (`>` or `1>`)
        if ">" in args or "1>" in args:
            redirect_symbol = ">" if ">" in args else "1>"
            split_index = args.index(redirect_symbol)
            file_args = args[:split_index]  # Files to read
            output_file = args[split_index + 1]  # Output file
        else:
            file_args = args
            output_file = None  # Print to stdout

        for file in file_args:
            if os.path.exists(file):
                with open(file, "r") as f:
                    collected_output.append(f.read())  # No `.strip()` to retain formatting
            else:
                print(f"cat: {file}: No such file or directory")
                return  # Exit early if any file is missing

        result = "".join(collected_output)  # Join without extra newlines

        if output_file:
            with open(output_file, "w") as f:
                f.write(result)
        else:
            print(result, end="")  # Avoid adding extra newlines
