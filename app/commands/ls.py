import os
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

        if output_file:
            output_dir = os.path.dirname(output_file)
            if output_dir and not os.path.exists(output_dir):
                # Expected error format
                error_message = f'Failed to read file ("{output_file}"): open {output_file}: no such file or directory\n'
                print(error_message, end="")
                return

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
