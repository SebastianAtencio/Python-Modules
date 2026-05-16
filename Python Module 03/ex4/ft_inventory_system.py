import sys


def dictionary() -> None:
    print("=== Inventory System Analysis ===")
    my_dct: dict[str, int] = {}
    for tupla in sys.argv[1:]:
        if ":" not in tupla:
            print(f"Error - invalid parameter '{tupla}'")
            continue
        line = tupla.split(':')
        if (len(line) != 2):
            print(f"Error - invalid parameter '{tupla}'")
            continue
        name = line[0]
        qty1 = line[1]
        if name in my_dct.keys():
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            val = int(qty1)
            my_dct[name] = val
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
        except Exception:
            print(f"Error - invalid parameter {line[0]}")
    if my_dct:
        print(f"Got inventory: {my_dct}")
        name_list = list(my_dct.keys())
        print(f"Item list: {name_list}")
        tot = sum(my_dct.values())
        print(f"Total quantity of the {len(my_dct)} items: {tot}")
        for item, qty in my_dct.items():
            print(f"Item {item} represents {(qty/tot*100):.1f}%")
        min = name_list[0]
        max = name_list[0]
        for items in name_list:
            if my_dct[items] > my_dct[max]:
                max = items
            if my_dct[items] < my_dct[min]:
                min = items
        print(f"Item most abundant: {max} with quantity {my_dct[max]}")
        print(f"Item least abundant: {min} with quantity {my_dct[min]}")
    else:
        pass
    my_dct.update({'magic_item': 1})
    print(f"Updated inventory: {my_dct}")


if __name__ == "__main__":
    dictionary()
