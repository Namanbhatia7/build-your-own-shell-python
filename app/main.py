import sys

def execute_repl():
    while True:
        sys.stdout.write("$ ")
        command = input()
        print(f'{command}: command not found') # throw invalid command


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")

    # execute_repl()

    sys.stdout.write("$ ")
    command = input()
    print(f'{command}: command not found')
    sys.exit()


if __name__ == "__main__":
    main()
