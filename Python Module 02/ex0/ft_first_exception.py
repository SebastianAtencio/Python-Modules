#!/usr/bin/env python3

def input_temperature(msg: str) -> int:
    return int(msg)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    data = '25'
    try:
        print(f"Input data is '{data}'")
        temp: int = input_temperature(data)
        print(f"Temperature is now {temp}ºC")
    except ValueError as mstk:
        print(f"Caught input_temperature error: {mstk}")
    except Exception as e:
        print(f"An unexpected error ocurred: {e}")
    print()
    data = 'abc'
    try:
        print(f"Input data is '{data}'")
        temp2: int = input_temperature(data)
        print(f"Temperature is now {temp2}ºC")
    except ValueError as mstk:
        print(f"Caught input_temperature error: {mstk}")
    except Exception as e:
        print(f"An unexpected error ocurred: {e}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
