import subprocess
import shlex

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            # Check if the command contains redirection (">", ">>", "1>", etc.)
            has_redirection = any(op in args for op in [">", ">>", "1>", "2>"])

            if has_redirection:
                # Execute directly in the shell without shlex.join()
                full_command = " ".join([command] + args)  # Direct join without escaping
            else:
                # Use shlex.join() for safe execution when no redirection
                full_command = shlex.join([command] + args)

            # Run the command in the shell
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
