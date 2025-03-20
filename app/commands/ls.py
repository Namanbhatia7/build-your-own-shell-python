import os
import sys
from app.commands.base import BaseCommand

class LSCommand(BaseCommand):
    def execute(self, args):
        path = "."  # Default directory
        stdout_file = None
        stderr_file = None
        stdout_append = False
        stderr_append = False

        # Handling stdout redirection (`>>`, `1>>`)
        if ">>" in args or "1>>" in args:
            redirect_symbol = ">>" if ">>" in args else "1>>"
            split_index = args.index(redirect_symbol)
            stdout_file = args[split_index + 1]
            stdout_append = True
            args = args[:split_index]  # Remove redirection part

        elif ">" in args or "1>" in args:
            redirect_symbol = ">" if ">" in args else "1>"
            split_index = args.index(redirect_symbol)
            stdout_file = args[split_index + 1]
            args = args[:split_index]  # Remove redirection part

        # Handling stderr redirection (`2>>`, `2>`)
        if "2>>" in args:
            split_index = args.index("2>>")
            stderr_file = args[split_index + 1]
            stderr_append = True
            args = args[:split_index]  # Remove redirection part

        elif "2>" in args:
            split_index = args.index("2>")
            stderr_file = args[split_index + 1]
            args = args[:split_index]  # Remove redirection part

        # Determine directory path
        filtered_args = [arg for arg in args if arg != "-1"]
        if filtered_args:
            path = filtered_args[0]

        # Ensure directories exist for stdout and stderr files
        for file in [stdout_file, stderr_file]:
            if file:
                output_dir = os.path.dirname(file)
                if output_dir and not os.path.exists(output_dir):
                    try:
                        os.makedirs(output_dir, exist_ok=True)
                    except OSError:
                        print(f'Failed to create directory for "{file}": No such file or directory', file=sys.stderr)
                        sys.exit(1)

        try:
            contents = sorted(os.listdir(path))
            output_text = "\n".join(contents) + "\n"

            if stdout_file:
                mode = "a" if stdout_append else "w"
                with open(stdout_file, mode) as f:
                    f.write(output_text)
            else:
                print(output_text.strip())  # Print to stdout if no redirection

        except FileNotFoundError as e:
            error_message = f"ls: {path}: No such file or directory\n"

            if stderr_file:
                mode = "a" if stderr_append else "w"
                with open(stderr_file, mode) as f:
                    f.write(error_message)
            else:
                print(error_message.strip(), file=sys.stderr)  # Print to stderr

            sys.exit(1)  # Ensure it exits with an error status
