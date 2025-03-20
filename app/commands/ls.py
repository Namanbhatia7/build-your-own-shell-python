import os
import sys
from app.commands.base import BaseCommand

class LSCommand(BaseCommand):
    def execute(self, args):
        path = "."  # Default directory
        output_file = None
        stderr_file = None
        stdout_append = False  # Flag for `>>` or `1>>`
        stderr_append = False  # Flag for `2>>`

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

        # Handling stderr redirection (`2>` and `2>>`)
        if "2>>" in args or "2>" in args:
            redirect_symbol = "2>>" if "2>>" in args else "2>"
            stderr_index = args.index(redirect_symbol)
            stderr_file = args[stderr_index + 1]
            stderr_append = "2>>" in args  # Set append flag

            dir_args = [arg for arg in args[:stderr_index] if arg != "-1"]
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
            error_message = f"ls: {path}: No such file or directory\n"

            if stderr_file:
                mode = "a" if stderr_append else "w"
                with open(stderr_file, mode) as f:
                    f.write(error_message)
            else:
                sys.stderr.write(error_message)

    def validate_paths(self, path, output_file):
        """
        Common function to validate the existence of output_file and path.
        Ensures the directory of `output_file` exists before writing.
        Ensures `path` exists before listing its contents.
        """

        # Check if the directory for the output file exists (if redirection is used)
        if output_file:
            output_dir = os.path.dirname(output_file)
            
            if not os.path.exists(output_dir):  # Ensure directory exists
                try:
                    os.makedirs(output_dir, exist_ok=True)
                except OSError:
                    print(f'Failed to create directory: {output_dir}', file=sys.stderr)
                    return False
            
            # Ensure output file exists before reading**
            if not os.path.exists(output_file):
                try:
                    open(output_file, 'a').close()  # Create an empty file
                except OSError:
                    print(f'Failed to create file: {output_file}', file=sys.stderr)
                    return False

        # # Check if the path to list exists
        # if not os.path.exists(path):
        #     print(f"ls: cannot access '{path}': No such file or directory", file=sys.stderr)
        #     return False

        return True