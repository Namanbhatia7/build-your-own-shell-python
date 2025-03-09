import os
from app.commands.base import BaseCommand

class LSCommand(BaseCommand):
    def execute(self, args):
        path = "."  # Default directory
        output_file = None  # Default to stdout

        # Handle output redirection (`>` or `1>`)
        if ">" in args or "1>" in args:
            redirect_symbol = ">" if ">" in args else "1>"
            split_index = args.index(redirect_symbol)

            dir_args = [arg for arg in args[:split_index] if arg != "-1"]  # Ignore `-1` flag
            output_file = args[split_index + 1]  # Extract output file

            if dir_args:
                path = dir_args[0]  # Take first argument as directory

        else:
            # Ignore `-1` if present in args
            filtered_args = [arg for arg in args if arg != "-1"]
            if filtered_args:
                path = filtered_args[0]  # Use directory argument if given

        try:
            # Get directory contents
            contents = os.listdir(path)
            contents.sort()  # Sort alphabetically like `ls`

            output_text = "\n".join(contents) + "\n"

            # Handle redirection or print to terminal
            if output_file:
                os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure parent dir exists
                with open(output_file, "w") as f:
                    f.write(output_text)
            else:
                print(output_text.strip())  # Avoid extra newline in terminal output

        except FileNotFoundError:
            print(f"ls: cannot access '{path}': No such file or directory")
