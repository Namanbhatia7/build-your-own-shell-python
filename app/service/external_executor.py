import subprocess

class ExternalExecutor:
    """Handles execution of external commands, including redirections."""

    def execute(self, command, args):
        try:
            # Convert args list to space-separated string
            args_str = " ".join(args)

            # Full command as string
            full_command = f"{command} {args_str}"

            # Run with shell=True so it can handle redirections
            result = subprocess.run(full_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Print stderr (errors should always be shown)
            if result.stderr:
                print(result.stderr, end="")

            # Print stdout only if it's not redirected
            if result.stdout and ">" not in args_str:
                print(result.stdout, end="")

        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
