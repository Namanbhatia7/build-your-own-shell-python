import subprocess

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            # Build the full command string
            full_command = " ".join([command] + args)

            # Run in shell mode to handle redirections properly
            result = subprocess.run(full_command, shell=True, check=True, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            print(result.stdout, end="")  # Print standard output
            print(result.stderr, end="")  # Print errors if any
        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
