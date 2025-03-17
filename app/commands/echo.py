import shlex
from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):
    def redirect(self, args):
        redirect_symbols = [">", "1>", "2>", ">>", "1>>"]
        redirections = {symbol: None for symbol in redirect_symbols}
        content = []

        # Identify redirections and extract target files
        for i, arg in enumerate(args):
            if arg in redirections and i + 1 < len(args):
                redirections[arg] = args[i + 1]
                break  # Stop processing content once redirection is found
            else:
                content.append(arg)

        content_str = " ".join(content)

        # Print only if no stdout redirection
        if not redirections[">"] and not redirections["1>"]:
            print(content_str)

        # Write to output file (stdout)
        output_file = redirections[">"] or redirections["1>"]
        if output_file:
            self.write_to_file(output_file, content_str)

        # Handle error redirection (stderr)
        if redirections["2>"]:
            self.write_to_file(redirections["2>"], "", empty_ok=True)

    def execute(self, args):
        if any(symbol in args for symbol in [">", "1>", "2>"]):
            self.redirect(args)
        else:
            print(" ".join(args))

    def write_to_file(self, file_path, content, empty_ok=False):
        """Writes content to a file, ensuring parent directories exist."""
        if content or empty_ok:
            with open(file_path, "w") as f:
                f.write(content + ("\n" if content else ""))
