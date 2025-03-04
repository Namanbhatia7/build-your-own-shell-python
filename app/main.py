import sys

from app.service.command_handler import Shell

def execute_repl():
    while True:
        sys.stdout.write("$ ")
        command = input().strip()

        if command == "exit 0":
            sys.exit(0)  # Exit with status code 0

        if command.startswith("echo "):
            echo_statement = command[5:]
            print(echo_statement)
        else:
            print(f'{command}: command not found') # throw invalid command

def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    shell_executor = Shell()
    shell_executor.start()


if __name__ == "__main__":
    main()
