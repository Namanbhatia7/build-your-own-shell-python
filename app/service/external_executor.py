import subprocess
import shlex

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            # Construct the full command safely
            full_command = shlex.join([command] + args)

            # Run in a shell to support redirection (`>` etc.)
            result = subprocess.run(full_command, shell=True, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # If there is stdout, print it (unless redirected)
            if result.stdout:
                print(result.stdout, end="")

            # If there is an error, print stderr (unless redirected)
            if result.stderr:
                print(result.stderr, end="")

        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
