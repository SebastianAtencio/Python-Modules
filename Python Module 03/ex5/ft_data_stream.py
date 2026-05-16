import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = ["alice", "bob", "charlie", "dylan"]
    action = ["run", "eat", "sleep", "grab",
              "move", "climb", "swim", "release"]
    while True:
        yield (random.choice(names), random.choice(action))


def consume_event(my_list: list[tuple[str, str]]) -> typing.Generator[
                                                tuple[str, str], None, None]:
    while my_list:
        index = random.randrange(len(my_list))
        event = my_list.pop(index)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    my_list = []
    event = gen_event()
    for i in range(1000):
        fir, sec = next(event)
        print(f"Event {i}: Player {fir} did action {sec}")
    for i in range(10):
        my_list.append(next(event))
    print(f"Built list of 10 events: {my_list}")
    for lucky in consume_event(my_list):
        print(f"Got event from list: {lucky}")
        print(f"Remains in list: {my_list}")


if __name__ == "__main__":
    main()
