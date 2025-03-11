import os
from app.commands.base import BaseCommand

class LSCommand(BaseCommand):
    def execute(self, args):
        path = "."  # Default directory
        output_file = None  # Default to stdout
        stderr_file = None  # Default to stderr

        # Handle stdout (`>` or `1>`) and stderr (`2>`) redirections
        if ">" in args or "1>" in args:
            redirect_symbol = ">" if ">" in args else "1>"
            split_index = args.index(redirect_symbol)

            dir_args = [arg for arg in args[:split_index] if arg != "-1"]  # Ignore `-1` flag
            output_file = args[split_index + 1]  # Extract output file

            if dir_args:
                path = dir_args[0]  # Take first argument as directory

        elif "2>" in args:
            stderr_index = args.index("2>")

            dir_args = [arg for arg in args[:stderr_index] if arg != "-1"]  # Ignore `-1` flag
            stderr_file = args[stderr_index + 1]  # Extract output file

            if dir_args:
                path = dir_args[0]  # Take first argument as directory

        else:
            filtered_args = [arg for arg in args if arg != "-1"]
            if filtered_args:
                path = filtered_args[0]

        try:
            # Get sorted directory contents (like `ls` does)
            contents = sorted(os.listdir(path))
            output_text = "\n".join(contents) + "\n"

            if output_file:
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                with open(output_file, "w") as f:
                    f.write(output_text)
            else:
                print(output_text.strip())  # Avoid extra newline

        except FileNotFoundError:
            error_message = f"ls: cannot access '{path}': No such file or directory\n"

            if stderr_file:
                os.makedirs(os.path.dirname(stderr_file), exist_ok=True)
                with open(stderr_file, "w") as f:
                    f.write(error_message)
            else:
                print(error_message, end="")
