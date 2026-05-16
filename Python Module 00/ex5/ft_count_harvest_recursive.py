def harvest_helper(current, total):
    if (current > total):
        return
    print(f"Day {current}")
    harvest_helper(current + 1, total)


def ft_count_harvest_recursive():
    n = int(input("Days until harvest:"))
    harvest_helper(1, n)
    print("Harvest time!")
