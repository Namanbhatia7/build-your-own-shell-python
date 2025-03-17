import subprocess
import shlex

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            has_redirection = any(op in args for op in [">", ">>", "1>>", "1>", "2>"])

            if has_redirection:
                full_command = " ".join([command] + args)
            else:
                full_command = shlex.join([command] + args)

            result = subprocess.run(full_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.stderr:
                cleaned_error = result.stderr.replace("/bin/sh: ", "", 1)  # Remove shell error prefix
                print(cleaned_error, end="")

            if result.stdout:
                print(result.stdout, end="")

        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
