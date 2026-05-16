import sys
import typing


def opening_archives() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            arc: typing.IO[str] = open(sys.argv[1], "r")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
            return
        print("---")
        print()
        cont = arc.read()
        print(cont)
        print("---")
        arc.close()
        print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    opening_archives()
