data = """
81, 157
209, 355
111, 78
179, 211
224, 268
93, 268
237, 120
345, 203
72, 189
298, 265
190, 67
319, 233
328, 40
323, 292
125, 187
343, 186
46, 331
106, 350
247, 332
349, 145
217, 329
48, 177
105, 170
257, 166
225, 113
44, 98
358, 92
251, 209
206, 215
115, 283
206, 195
144, 157
246, 302
306, 157
185, 353
117, 344
251, 155
160, 48
119, 131
343, 349
223, 291
256, 89
133, 96
240, 271
322, 73
324, 56
149, 272
161, 107
172, 171
301, 291
""".strip()

class Point(object):
    def __init__(self, coord):
        self.x, self.y = [int(c) for c in coord]

    def __str__(self):
        return str((self.x, self.y))

    __repr__ = __str__

points = [Point(line.split(", ")) for line in data.split("\n")]

minx = min(points, key=lambda p: p.x).x
miny = min(points, key=lambda p: p.y).y
maxx = max(points, key=lambda p: p.x).x - minx
maxy = max(points, key=lambda p: p.y).y - miny

for i, p in enumerate(points):
    points[i].x -= minx
    points[i].y -= miny

grid = [x[:] for x in [[0] * (maxx+1)] * (maxy+1)]
grid2 = [x[:] for x in [[0] * (maxx+1)] * (maxy+1)]

def manhattan_distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

for y, row in enumerate(grid):
    for x, col in enumerate(row):
        dists = [manhattan_distance(Point([x, y]), p) for p in points]
        min_dist = min(dists)
        if dists.count(min_dist) == 1:
            grid[y][x] = dists.index(min_dist)
        else:
            grid[y][x] = -1
        if sum(dists) < 10000:
            grid2[y][x] = 1
        else:
            grid2[y][x] = -1

import itertools
from collections import Counter
c = Counter(list(itertools.chain.from_iterable(grid)))
c.pop(-1)

for col in grid[0]:
    c.pop(col, None)
for col in grid[-1]:
    c.pop(col, None)
for row in grid:
    c.pop(row[0], None)
    c.pop(row[-1], None)

print(c.most_common(1)[0])

c2 = Counter(list(itertools.chain.from_iterable(grid2)))
c2.pop(-1)
print(c2)
