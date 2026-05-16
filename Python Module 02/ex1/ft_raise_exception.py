#!/usr/bin/env python3

def input_temperature(msg: str) -> int:
    temp = int(msg)
    if temp < 0:
        raise ValueError(f"{temp}ºC is too cold for plants (min 0ºC)")
    elif temp > 40:
        raise ValueError(f"{temp}ºC is too hot for plants (max 40ªC)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    group = ['25', 'abc', '100', '-50']
    for data in group:
        try:
            print(f"Input data is '{data}'")
            temp: int = input_temperature(data)
            print(f"Temperature is now {temp}ºC")
        except ValueError as mstk:
            print(f"Caught input_temperature error: {mstk}")
        except Exception as e:
            print(f"An unexpected error ocurred: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
