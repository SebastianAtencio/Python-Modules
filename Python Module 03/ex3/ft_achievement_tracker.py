import random


def gen_player_achievements() -> set[str]:
    achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer']
    count = random.randint(5, 10)
    return set(random.sample(achievements, count))


def main() -> None:
    total_achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                          'Speed Runner', 'Survivor', 'Master Explorer',
                          'Treasure Hunter', 'Unstoppable', 'First Steps',
                          'Collector Supreme', 'Untouchable', 'Sharp Mind',
                          'Boss Slayer', 'Hidden Path Finder']
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }
    print("=== Achievement Tracker System ===")
    print()
    for people in players:
        features = players[people]
        print(f"Player {people} : {features}")
    all = set().union(*players.values())
    print()
    print(f"All distinct achievements: {all}")
    print()
    inter = set.intersection(*players.values())
    print(f"Common achievements: {inter}")
    print()
    for name in players:
        my_features = players[name]
        other_features: set[str] = set()
        for other_name in players:
            if other_name != name:
                other_features = other_features.union(players[other_name])
        mine = my_features.difference(other_features)
        print(f"Only {name} has: {mine}")
    print()
    for name in players:
        missing = set(total_achievements).difference(players[name])
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
