import sys


def process_args() -> None:
    print("=== Command Quest ===")
    num = len(sys.argv)
    i = 0
    if (num == 1):
        print(f"Program name: {sys.argv[i]}")
        print("No arguments provided!")
    else:
        print(f"Program name: {sys.argv[i]}")
        i += 1
        print(f"Arguments received: {num - 1}")
        while (i < num):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {num}")


if __name__ == "__main__":
    process_args()
