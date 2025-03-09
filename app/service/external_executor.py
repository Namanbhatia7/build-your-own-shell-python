import subprocess
import shlex

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            # Construct a properly formatted shell command
            full_command = shlex.join([command] + args)

            # Check if the command contains redirection (">", ">>", "1>", etc.)
            if any(op in args for op in [">", ">>", "1>", "2>"]):
                # Execute directly in the shell without capturing output
                result = subprocess.run(full_command, shell=True)
            else:
                # Capture stdout and stderr only when there's no redirection
                result = subprocess.run(full_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
