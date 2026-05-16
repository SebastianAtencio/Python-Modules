import random


def comprehensions() -> None:
    raw_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                'Gregory', 'john', 'kevin', 'Liam']
    all_cap: list[str] = [name.capitalize() for name in raw_list]
    print(f"New list with all names capitalized: {all_cap}")
    list_cap: list[str] = [name for name in raw_list if name[0].isupper()]
    print(f"New list of capitalized names only: {list_cap}")
    my_dct = {name: random.randint(1, 1000) for name in all_cap}
    print(f"Score dict: {my_dct}")
    avg = sum(my_dct.values())/len(all_cap)
    print(f"Score average: {round(avg,2)}")
    high = {name: score for name, score in my_dct.items() if score > avg}
    print(f"High scores: {high}")


if __name__ == "__main__":
    comprehensions()
