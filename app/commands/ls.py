import os
from app.commands.base import BaseCommand

class LSCommand(BaseCommand):
    def execute(self, args):
        path = "."  # Default directory
        output_file = None
        stderr_file = None
        stdout_append = False  # Flag for `>>` or `1>>`
        stderr_append = False  # Flag for `2>>`

        # Handling stdout redirection (`>`, `1>`, `>>`, `1>>`)
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
                path = dir_args[0]  # Take first argument as directory
        
        elif "2>>" in args:
            stderr_index = args.index("2>>")
            stderr_file = args[stderr_index + 1]
            stderr_append = True

            dir_args = [arg for arg in args[:stderr_index] if arg != "-1"]
            if dir_args:
                path = dir_args[0]

        elif "2>" in args:
            stderr_index = args.index("2>")
            stderr_file = args[stderr_index + 1]

            dir_args = [arg for arg in args[:stderr_index] if arg != "-1"]
            if dir_args:
                path = dir_args[0]

        else:
            filtered_args = [arg for arg in args if arg != "-1"]
            if filtered_args:
                path = filtered_args[0]

        try:
            # Get sorted directory contents (like `ls` does)
            contents = sorted(os.listdir(path))
            output_text = "\n".join(contents) + "\n"

            if output_file:
                output_dir = os.path.dirname(output_file)
                if output_dir and not os.path.exists(output_dir):
                    error_message = f'Failed to read file ("{output_file}"): open {output_file}: no such file or directory\n'
                    print(error_message, end="")
                    return

                mode = "a" if stdout_append else "w"  # Append if `>>`, overwrite if `>`
                with open(output_file, mode) as f:
                    f.write(output_text)
            else:
                print(output_text.strip())  # Avoid extra newline

        except FileNotFoundError:
            error_message = f"ls: {path}: No such file or directory\n"

            if stderr_file:
                os.makedirs(os.path.dirname(stderr_file), exist_ok=True)
                mode = "a" if stderr_append else "w"  # Append if `2>>`, overwrite if `2>`
                with open(stderr_file, mode) as f:
                    f.write(error_message)
            else:
                print(error_message, end="")
