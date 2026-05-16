import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        line = input("Enter new coordinates as floats "
                     "in format 'x,y,z': ")
        tupla = line.split(',')

        if len(tupla) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(tupla[0].strip())
            y = float(tupla[1].strip())
            z = float(tupla[2].strip())
            return (x, y, z)
        except ValueError:
            for p in tupla:
                p_clean = p.strip()
                try:
                    float(p_clean)
                except ValueError as e:
                    print(f"Error on parameter '{p_clean}': {e}")
                    break


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    dist1 = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Distance to center: {round(dist1, 4)}")
    print()
    print("Get a second set of coordinates")
    p2 = get_player_pos()
    dist2 = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(dist2, 4)}")


if __name__ == "__main__":
    main()
