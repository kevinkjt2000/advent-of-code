def parse_file(filename="2022/day8.input"):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    return [[int(c) for c in line] for line in lines]


def part1():
    tree_grid = parse_file()
    columns = len(tree_grid[0])
    rows = len(tree_grid)
    visible = [[False] * columns for _ in range(rows)]

    for y in range(rows):
        # left
        visible[y][columns - 1] = True
        tallest_tree = tree_grid[y][columns - 1]
        for x in range(columns - 2, 0, -1):
            if (tree := tree_grid[y][x]) > tallest_tree:
                tallest_tree = tree
                visible[y][x] = True
        # right
        visible[y][0] = True
        tallest_tree = tree_grid[y][0]
        for x in range(1, columns):
            if (tree := tree_grid[y][x]) > tallest_tree:
                tallest_tree = tree
                visible[y][x] = True

    for x in range(columns):
        # up
        visible[rows - 1][x] = True
        tallest_tree = tree_grid[rows - 1][x]
        for y in range(rows - 2, 0, -1):
            if (tree := tree_grid[y][x]) > tallest_tree:
                tallest_tree = tree
                visible[y][x] = True
        # down
        visible[0][x] = True
        tallest_tree = tree_grid[0][x]
        for y in range(1, rows):
            if (tree := tree_grid[y][x]) > tallest_tree:
                tallest_tree = tree
                visible[y][x] = True

    print(sum(row.count(True) for row in visible))


def part2():
    tree_grid = parse_file()
    columns = len(tree_grid[0])
    rows = len(tree_grid)
    may_visibility_score = 0

    for x in range(columns):
        for y in range(rows):
            tree_under_consideration = tree_grid[y][x]
            visibility_score = 1
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                viewing_distance = 0
                cx, cy = x + dx, y + dy
                while cx in range(columns) and cy in range(rows):
                    viewing_distance += 1
                    if tree_grid[cy][cx] >= tree_under_consideration:
                        break
                    cx += dx
                    cy += dy
                visibility_score *= viewing_distance
            may_visibility_score = max(visibility_score, may_visibility_score)

    print(may_visibility_score)


def main():
    part2()


if __name__ == "__main__":
    main()
