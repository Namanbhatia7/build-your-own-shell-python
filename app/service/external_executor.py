import subprocess
import shlex
import sys

class ExternalExecutor:
    """Handles execution of external commands with proper redirections."""

    def execute(self, command_str):
        """
        Parses and executes a shell command with support for stdout and stderr redirections.
        """

        # Use `shlex.split()` to properly handle quotes (e.g., 'filename with spaces')
        args = shlex.split(command_str)
        stdout_file = None
        stderr_file = None
        append_mode = False

        # Handle output redirection (`>`, `>>`, `2>`)
        if ">" in args or "2>" in args:
            new_args = []
            i = 0
            while i < len(args):
                if args[i] in (">", ">>"):  # Handle stdout redirection
                    append_mode = args[i] == ">>"
                    stdout_file = args[i + 1]  # Next argument is the filename
                    i += 1
                elif args[i] == "2>":  # Handle stderr redirection
                    stderr_file = args[i + 1]
                    i += 1
                else:
                    new_args.append(args[i])
                i += 1
            args = new_args

        try:
            # Run the external command
            with subprocess.Popen(
                args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            ) as process:
                stdout, stderr = process.communicate()

                # Handle stdout redirection
                if stdout_file:
                    mode = "a" if append_mode else "w"
                    with open(stdout_file, mode) as f:
                        f.write(stdout)
                else:
                    sys.stdout.write(stdout)

                # Handle stderr redirection
                if stderr_file:
                    with open(stderr_file, "w") as f:
                        f.write(stderr)
                else:
                    sys.stderr.write(stderr)

        except FileNotFoundError:
            sys.stderr.write(f"{args[0]}: command not found\n")
        except Exception as e:
            sys.stderr.write(f"Error executing command: {str(e)}\n")
