import subprocess
import shlex

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            # Check for redirections
            has_redirection = any(op in args for op in [">", ">>", "1>", "2>"])

            # Form command string
            full_command = " ".join([command] + args) if has_redirection else shlex.join([command] + args)

            # Run with Bash to get expected error message format
            result = subprocess.run(full_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")

            # Print stderr (errors should not be redirected)
            if result.stderr:
                print(result.stderr, end="")

            # Print stdout only if it's not redirected
            if result.stdout:
                print(result.stdout, end="")

        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
