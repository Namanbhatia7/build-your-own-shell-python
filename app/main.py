import sys

def execute_repl():
    while True:
        sys.stdout.write("$ ")
        command = input()
        print(f'{command}: command not found') # throw invalid command

        if command == "exit 0":
            sys.exit(0)  # Exit with status code 0


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")

    execute_repl()


if __name__ == "__main__":
    main()
