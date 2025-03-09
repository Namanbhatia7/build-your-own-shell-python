import subprocess
import shlex

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            # Check if redirection exists
            has_redirection = any(op in args for op in [">", ">>", "1>", "2>"])

            # Construct the command properly
            full_command = " ".join([command] + args) if has_redirection else shlex.join([command] + args)

            # Execute the command using bash for proper redirection handling
            result = subprocess.run(full_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")

            # Print errors first (should not be redirected)
            if result.stderr:
                print(result.stderr, end="")

            # Print stdout only if it's not redirected
            if result.stdout and not has_redirection:
                print(result.stdout, end="")

        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
