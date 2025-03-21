import shlex
import sys
from app.commands.base import BaseCommand

class EchoCommand(BaseCommand):

    def has_stdout_redirection(self, redirections):
        return any(redirections[symbol] for symbol in self.REDIRECT_SYMBOLS if symbol != "2>")

    def handle_redirections(self, redirections, content_str):
        if redirections[">"] or redirections["1>"]:
            self.write_to_file(redirections[">"] or redirections["1>"], content_str, mode="w")

        if redirections[">>"] or redirections["1>>"]:
            self.write_to_file(redirections[">>"] or redirections["1>>"], content_str, mode="a")

        if redirections["2>"]:
            self.write_to_file(redirections["2>"] or redirections["2>>"], "", mode="w", empty_ok=True)

    def parse_arguments(self, args):
        """Parses command arguments and returns a tuple of content and redirections."""
        redirections = {symbol: None for symbol in self.REDIRECT_SYMBOLS}
        content = []

        for i, arg in enumerate(args):
            if arg in redirections and i + 1 < len(args):
                redirections[arg] = args[i + 1]
                break
            else:
                content.append(arg)
        
        return redirections, content

    def redirect(self, args):
        redirections, content = self.parse_arguments(args)
        content_str = " ".join(content)

        if redirections["2>>"]:
            print(content_str, file=sys.stderr)            
            

        # Print only if no stdout redirection
        if not self.has_stdout_redirection(redirections):
            print(content_str)

        self.handle_redirections(redirections, content_str)

    def write_to_file(self, file_path, content, mode="w", empty_ok=False):
        """Writes content to a file, ensuring parent directories exist."""
        if content or empty_ok:
            with open(file_path, mode) as f:
                f.write(content + ("\n" if content else ""))
    
    def execute(self, args):
        if any(symbol in args for symbol in self.REDIRECT_SYMBOLS):
            self.redirect(args)
        else:
            print(" ".join(args))
