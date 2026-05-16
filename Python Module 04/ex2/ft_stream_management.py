import sys
import typing


def opening_archives() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>", file=sys.stderr)
        return
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            arc: typing.IO[str] = open(sys.argv[1], "r")
            cont = arc.read()
            arc.close()
        except Exception as e:
            print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
                  file=sys.stderr)
            return
        print("---")
        print()
        print(cont)
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
        print()
        print("Transform data:")
        new_cont = ""
        temporary = ""
        for char in cont:
            if char == '\n':
                new_cont += temporary + "#\n"
                temporary = ""
            else:
                temporary += char
        if temporary:
            new_cont += temporary + "#\n"
        print("---")
        print()
        print(new_cont)
        print("---")
        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_name = sys.stdin.readline().strip()
        if not new_name:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_name}'")
            try:
                arc_save = open(new_name, "w")
                arc_save.write(new_cont)
                arc_save.close()
                print(f"Data saved in file '{new_name}'.")
            except Exception as e:
                print(f"[STDERR] Error opening file '{new_name}': {e}",
                      file=sys.stderr)
                print("Data not saved.")


if __name__ == "__main__":
    opening_archives()
