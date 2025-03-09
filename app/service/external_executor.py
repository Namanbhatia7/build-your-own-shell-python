import subprocess
import shlex

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            # Construct a properly formatted shell command
            full_command = shlex.join([command] + args)

            # Run in a shell to handle redirections correctly
            result = subprocess.run(full_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            
            # Print stderr (errors should not be redirected)
            if result.stderr:
                print(result.stderr, end="")

            # Only print stdout if it's not redirected
            if result.stdout:
                print(result.stdout, end="")


        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
