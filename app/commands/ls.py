import os
from app.commands.base import BaseCommand

class LSCommand(BaseCommand):
    def execute(self, args):
       def execute(self, args):
        path = args[0] if args and args[0] not in [">", "1>"] else "."

        # Check if redirection (`>` or `1>`) is used
        if ">" in args or "1>" in args:
            redirect_symbol = ">" if ">" in args else "1>"
            split_index = args.index(redirect_symbol)
            dir_path = args[:split_index]  # Directory to list
            output_file = args[split_index + 1]  # Output file

            os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure parent dir exists

            try:
                contents = "\n".join(os.listdir(dir_path[0] if dir_path else "."))
                with open(output_file, "w") as f:
                    f.write(contents + "\n")
            except FileNotFoundError:
                print(f"ls: cannot access '{dir_path[0]}': No such file or directory")
        else:
            try:
                print("\n".join(os.listdir(path)))
            except FileNotFoundError:
                print(f"ls: cannot access '{path}': No such file or directory")