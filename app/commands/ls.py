import os
from app.commands.base import BaseCommand

class LSCommand(BaseCommand):
    def execute(self, args):
        path = "."  # Default to current directory
        output_file = None  # For redirection

        # Handle redirection (`>` or `1>`)
        if ">" in args or "1>" in args:
            redirect_symbol = ">" if ">" in args else "1>"
            split_index = args.index(redirect_symbol)

            # Directory to list
            dir_args = args[:split_index]
            if dir_args:
                path = dir_args[0]  # Take first argument as directory

            # Output file
            if split_index + 1 < len(args):
                output_file = args[split_index + 1]

        else:
            if args and args[0] not in [">", "1>"]:
                path = args[0]  # Set directory if provided

        try:
            contents = "\n".join(sorted(os.listdir(path))) + "\n"

            if output_file:
                os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure parent dir exists
                with open(output_file, "w") as f:
                    f.write(contents)
            else:
                print(contents.strip())  # Avoid extra newline on terminal

        except FileNotFoundError:
            print(f"ls: cannot access '{path}': No such file or directory")
    
        return 1
