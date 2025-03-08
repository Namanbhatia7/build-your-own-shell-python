import subprocess

class ExternalExecutor:
    """Handles execution of external commands."""

    def execute(self, command, args):
        try:
            result = subprocess.run([command] + args, check=True, text=True, capture_output=True)
            print(result.stdout, end="")
        except FileNotFoundError:
            print(f"{command}: command not found")
        except subprocess.CalledProcessError as e:
            print(e.stderr if e.stderr else f"{command}: error occurred")
