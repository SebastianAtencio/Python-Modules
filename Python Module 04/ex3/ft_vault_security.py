def secure_archive(name: str, action: str = "r", content: str = ""
                   ) -> tuple[bool, str]:
    try:
        with open(name, action) as arc:
            if action == "r":
                return (True, arc.read())
            if action == "w":
                arc.write(content)
                return (True, 'Content successfully written to file')
    except Exception as e:
        return (False, str(e))
    return (False, "Invalid action")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd'))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt'))
    print()
    print("Using 'secure archive' to write previous content to a new file:")
    print(secure_archive("new_archive", "w", "I did it!!"))


if __name__ == "__main__":
    main()
