import os
import sys
from app.commands.base import BaseCommand

class LSCommand(BaseCommand):
    def execute(self, args):
        path = "."  # Default directory
        output_file = None
        stdout_append = False  # Flag for `>>` or `1>>`

        # Handling stdout redirection (`>>`, `1>>`)
        if ">>" in args or "1>>" in args:
            redirect_symbol = ">>" if ">>" in args else "1>>"
            split_index = args.index(redirect_symbol)
            output_file = args[split_index + 1]
            stdout_append = True
            dir_args = [arg for arg in args[:split_index] if arg != "-1"]
            if dir_args:
                path = dir_args[0]

        elif ">" in args or "1>" in args:
            redirect_symbol = ">" if ">" in args else "1>"
            split_index = args.index(redirect_symbol)
            output_file = args[split_index + 1]
            dir_args = [arg for arg in args[:split_index] if arg != "-1"]
            if dir_args:
                path = dir_args[0]

        else:
            filtered_args = [arg for arg in args if arg != "-1"]
            if filtered_args:
                path = filtered_args[0]

        if not self.validate_paths(path, output_file):
            sys.exit(1)

        try:
            contents = sorted(os.listdir(path))
            output_text = "\n".join(contents) + "\n"

            if output_file:
                mode = "a" if stdout_append else "w"
                with open(output_file, mode) as f:
                    f.write(output_text)
            else:
                print(output_text.strip())  # Avoid extra newline

        except FileNotFoundError:
            print(f"ls: {path}: No such file or directory", end="")

    def validate_paths(self, path, output_file):
        """
        Common function to validate the existence of output_file and path.
        Ensures the directory of `output_file` exists before writing.
        Ensures `path` exists before listing its contents.
        """
        # # Check if the path to list exists
        # if not os.path.exists(path):
        #     print(f"ls: cannot access '{path}': No such file or directory", file=sys.stderr)
        #     return False

        # Check if the directory for the output file exists (if redirection is used)
        if output_file:
            print(output_file)
            output_dir = os.path.dirname(output_file)
            if output_dir and not os.path.exists(output_dir):
                try:
                    os.makedirs(output_dir, exist_ok=True)
                    return False
                except OSError:
                    print(f'Failed to read file ("{output_file}"): open {output_file}: no such file or directory', file=sys.stderr)
                    return False
            else:
                print(f'Failed to read file ("{output_file}"): open {output_file}: no such file or directory', file=sys.stderr)
                return False

        return True
