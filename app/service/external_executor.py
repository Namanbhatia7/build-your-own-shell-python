import subprocess
import shlex

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            # Handle commands with spaces properly
            command = shlex.quote(command)  

            # Convert args list to a properly formatted string
            args_str = " ".join(shlex.quote(arg) for arg in args)

            # Full command as string
            full_command = f"{command} {args_str}"

            # Run with shell=True so it can handle redirections
            result = subprocess.run(full_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Print stderr (errors should always be shown)
            if result.stderr:
                print(result.stderr, end="")

            # Print stdout only if it's not redirected
            if result.stdout and ">" not in args:
                print(result.stdout, end="")

        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
