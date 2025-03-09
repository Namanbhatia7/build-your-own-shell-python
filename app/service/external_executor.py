import subprocess

class ExternalExecutor:
    """Handles execution of external commands."""

    def execute(self, command, args):
        try:
            # Combine command and args into a single shell-executed string
            full_command = " ".join([command] + args)

            # Use shell=True to allow redirections (>, >>, 2>)
            result = subprocess.run(full_command, shell=True, check=True, text=True, capture_output=True)

            print(result.stdout, end="")

        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
