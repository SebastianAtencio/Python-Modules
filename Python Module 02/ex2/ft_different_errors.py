#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("text.txt", "r")
    elif operation_number == 3:
        "hola" + 5


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except (ValueError) as mstk:
            print(f"Caught ValueError: {mstk}")
        except ZeroDivisionError as mstk:
            print(f"Caught ZeroDivisionError: {mstk}")
        except FileNotFoundError as mstk:
            print(f"Caught FileNotFoundError: {mstk}")
        except TypeError as mstk:
            print(f"Caught TypeError: {mstk}")
    print()
    print("All error types tested successfully")


if __name__ == "__main__":
    test_error_types()
