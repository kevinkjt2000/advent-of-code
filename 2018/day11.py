data = 7672

def power_level(x, y, sn):
    rack_id = x + 10
    power = rack_id * y
    power += sn
    power *= rack_id
    power = int(power / 100) % 10
    power -= 5
    return power


def solve(number):
    import numpy
    grid = numpy.zeros(shape=(300, 300))
    for x in range(0, 300):
        for y in range(0, 300):
            grid[y,x] = power_level(x+1, y+1, number)

    maxes = []
    for sizex in range(1, 301):
        sizey = sizex
        sums = numpy.zeros(shape=(300-sizex, 300-sizey))
        for x in range(0, 300 - sizex):
            for y in range(0, 300 - sizey):
                sums[y,x] = numpy.sum(grid[y:y+sizey,x:x+sizex])

        if sizex != 300:
            ay, ax = numpy.unravel_index(sums.argmax(), sums.shape)
            maxes.append((sums[ay,ax], ax+1, ay+1, sizex))
        else:
            ay, ax = (0, 0)
            maxes.append((numpy.sum(grid), ax+1, ay+1, sizex))

    max_thing = max(maxes, key=lambda p: p[0])
    return (max_thing[1], max_thing[2], max_thing[3])



assert power_level(3, 5, sn=8) == 4
assert power_level(122, 79, sn=57) == -5

print(solve(data))
