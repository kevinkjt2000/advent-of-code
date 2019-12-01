from enum import Enum
from queue import Queue


def fuel_sum(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + fuel_sum(fuel)


def main():
    real_input = list(map(int, open("day1.input").read().strip().splitlines()))
    print(sum([fuel_sum(x) for x in real_input]))


main()
