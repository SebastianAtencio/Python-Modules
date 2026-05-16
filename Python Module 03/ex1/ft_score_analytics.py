import sys


def process_args() -> None:
    print("=== Player Score Analytics ===")
    num = len(sys.argv)
    if (num <= 1):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    i = 1
    lista: list[int] = []
    while i < num:
        try:
            dato = int(sys.argv[i])
            lista = lista + [dato]
        except Exception:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        finally:
            i += 1
    if lista != []:
        tot = sum(lista)
        count = len(lista)
        print(f"Scores processed: {lista}")
        print(f"Total players: {count}")
        print(f"Total score: {tot}")
        print(f"Average score: {tot/count}")
        print(f"High score: {max(lista)}")
        print(f"Low score: {min(lista)}")
        print(f"Score range: {(max(lista) - min(lista))}")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")


if __name__ == "__main__":
    process_args()
