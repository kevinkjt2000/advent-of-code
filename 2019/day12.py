import re


def solve(data):
    moons = list(map(parse_moon_position, data))
    moon_velocities = [[0, 0, 0] for i in range(len(moons))]
    already_encountered = set(str(moons) + str(moon_velocities))
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    time_step = 0
    while True:
        for i, j in pairs:
            for xyz in range(3):
                if moons[i][xyz] < moons[j][xyz]:
                    moon_velocities[i][xyz] += 1
                    moon_velocities[j][xyz] -= 1
                elif moons[i][xyz] > moons[j][xyz]:
                    moon_velocities[i][xyz] -= 1
                    moon_velocities[j][xyz] += 1
        for i in range(len(moons)):
            for xyz in range(3):
                moons[i][xyz] += moon_velocities[i][xyz]
        if str(moons) + str(moon_velocities) in already_encountered:
            print(time_step)
            break
        already_encountered.add(str(moons) + str(moon_velocities))
        time_step += 1
    total_energy = 0
    for i in range(len(moons)):
        potential_energy = sum(abs(xyz) for xyz in moons[i])
        kinetic_energy = sum(abs(xyz) for xyz in moon_velocities[i])
        total_energy += potential_energy * kinetic_energy
    print(total_energy)


def parse_moon_position(string):
    m = re.search("<x=(?P<x>-?[0-9]+), y=(?P<y>-?[0-9]+), z=(?P<z>-?[0-9]+)>", string)
    return [int(m.group("x")), int(m.group("y")), int(m.group("z"))]


def main():
    solve("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""".splitlines())
    # solve(open("day12.input").read().splitlines())


if __name__ == "__main__":
    main()
