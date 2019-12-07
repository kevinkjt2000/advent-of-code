def sum_orbits(orbits, current="COM", dist=0):
    return dist + sum(sum_orbits(orbits, planet, dist+1) for planet in orbits[current])


def find_path(orbits, destination, current="COM"):
    if destination == current:
        return [current]
    for planet in orbits[current]:
        path = find_path(orbits, destination, planet)
        if path:
            return [current] + path
    return None


def main():
    lines = open("day6.input").read().strip().splitlines()
    orbits = {"COM": []}
    for line in lines:
        inner, outer = line.split(")")
        if inner not in orbits:
            orbits[inner] = []
        orbits[inner].append(outer)
        if outer not in orbits:
            orbits[outer] = []
    print(sum_orbits(orbits))
    you_path = find_path(orbits, "YOU")
    santa_path = find_path(orbits, "SAN")
    i = 0
    while you_path[i] == santa_path[i]:
        i += 1
    print(len(you_path) + len(santa_path) - 2 - i - i)

if __name__ == "__main__":
    main()
