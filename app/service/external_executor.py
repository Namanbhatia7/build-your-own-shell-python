import subprocess

class ExternalExecutor:
    """Handles execution of external commands."""

    def execute(self, command, args):
        try:
            # Convert command and args into a shell-like command string
            full_command = " ".join([command] + args)

            # Run with shell to support redirection (1>, >, etc.)
            result = subprocess.run(full_command, shell=True, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
                        # Print standard error (stderr) to ensure errors are visible
            if result.stderr:
                print(result.stderr, end="")

            # Print standard output (stdout)
            print(result.stdout, end="")

        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
