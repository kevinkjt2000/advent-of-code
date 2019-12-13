from functools import reduce
import math
import re


def lcm(a, b):
    return a * b // math.gcd(a, b)


def transpose(data):
    return [[row[i] for row in data] for i in range(len(data[0]))]


def solve(data):
    moons = list(map(parse_moon_position, data))
    moons = transpose(moons)
    moon_velocities = [[0 for moon in range(len(moons[0]))] for i in range(3)]
    pairs = []
    for i in range(len(moons[0])):
        for j in range(i+1, len(moons[0])):
            if i != j:
                pairs.append((i, j))
    print(pairs)
    periods = [0] * 3
    for xyz in range(3):
        time_step = 0
        print(time_step, moons[xyz], moon_velocities[xyz])
        already_encountered = set()
        already_encountered.add(str(moons[xyz]) + str(moon_velocities[xyz]))
        while True:
            for i, j in pairs:
                if moons[xyz][i] < moons[xyz][j]:
                    moon_velocities[xyz][i] += 1
                    moon_velocities[xyz][j] -= 1
                elif moons[xyz][i] > moons[xyz][j]:
                    moon_velocities[xyz][i] -= 1
                    moon_velocities[xyz][j] += 1
            for i in range(len(moons[xyz])):
                moons[xyz][i] += moon_velocities[xyz][i]
            time_step += 1
            print(time_step, moons[xyz], moon_velocities[xyz])
            if str(moons[xyz]) + str(moon_velocities[xyz]) in already_encountered:
                periods[xyz] = time_step
                print(time_step)
                break
            already_encountered.add(str(moons[xyz]) + str(moon_velocities[xyz]))
    print(reduce(lcm, periods))
    # total_energy = 0
    # for i in range(len(moons)):
    #     potential_energy = sum(abs(xyz) for xyz in moons[i])
    #     kinetic_energy = sum(abs(xyz) for xyz in moon_velocities[i])
    #     total_energy += potential_energy * kinetic_energy
    # print(total_energy)


def parse_moon_position(string):
    m = re.search("<x=(?P<x>-?[0-9]+), y=(?P<y>-?[0-9]+), z=(?P<z>-?[0-9]+)>", string)
    return [int(m.group("x")), int(m.group("y")), int(m.group("z"))]


def main():
#     solve("""<x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>""".splitlines())
    solve(open("day12.input").read().splitlines())


if __name__ == "__main__":
    main()
