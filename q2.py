from typing import List


def surviving_ships(ships: List[int]) -> List[int]:
    """
    Problem 2: Spaceship collisions.

    Given a list of ship engine powers (sign = direction: positive is
    right, negative is left), resolve all collisions between ships
    moving toward each other and return the engine powers (with sign)
    of the ships that remain.

    Args:
        ships: list of signed engine powers.

    Returns:
        List of signed engine powers of surviving ships, left to right.
    """
    for i in range(len(ships)):
        if i+1!= len(ships):
            if ships[i]>0 and ships[i+1]<0:
                if abs(ships[i])>abs(ships[i+1]):
                    ships=ships[:i+1]+ships[i+2:]
                    return surviving_ships(ships)
                elif abs(ships[i])<abs(ships[i+1]):
                    ships=ships[:i]+ships[i+1:]
                    return surviving_ships(ships)
                else:
                    ships=ships[:i]+ships[i+2:]
                    return surviving_ships(ships)
    else:
        return ships
pass


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
