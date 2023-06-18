import sys


def decorate_1(lights, instruction, grid):
    if "turn on" in instruction:
        for x in range(lights[0], lights[2] + 1):
            for y in range(lights[1], lights[3] + 1):
                grid[x][y] = 1

    elif "toggle" in instruction:
        for x in range(lights[0], lights[2] + 1):
            for y in range(lights[1], lights[3] + 1):
                if grid[x][y] == 0:
                    grid[x][y] = 1
                else:
                    grid[x][y] = 0

    else:
        for x in range(lights[0], lights[2] + 1):
            for y in range(lights[1], lights[3] + 1):
                grid[x][y] = 0

    return grid


def solve_1(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]

    grid = []
    for i in range(1000):
        grid.append([])
        for _ in range(1000):
            grid[i].append(0)

    for instruction in data:
        instruction = instruction.replace(",", " ")
        lights = [int(s) for s in instruction.split() if s.isdigit()]
        grid = decorate_1(lights, instruction, grid)

    count = 0
    for i in range(len(grid)):
        count += sum(grid[i])
    print(f"The number of lit lights: {count:,}")


#################################################

def decorate_2(lights, instruction, grid):
    if "turn on" in instruction:
        for x in range(lights[0], lights[2] + 1):
            for y in range(lights[1], lights[3] + 1):
                grid[x][y] += 1

    elif "toggle" in instruction:
        for x in range(lights[0], lights[2] + 1):
            for y in range(lights[1], lights[3] + 1):
                grid[x][y] += 2

    else:
        for x in range(lights[0], lights[2] + 1):
            for y in range(lights[1], lights[3] + 1):
                if grid[x][y] > 0:
                    grid[x][y] -= 1

    return grid

def solve_2(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    grid = []
    for i in range(1000):
        grid.append([])
        for _ in range(1000):
            grid[i].append(0)

    for instruction in data:
        instruction = instruction.replace(",", " ")
        lights = [int(s) for s in instruction.split() if s.isdigit()]
        grid = decorate_2(lights, instruction, grid)

    count = 0
    for i in range(len(grid)):
        count += sum(grid[i])
    print(f"The total brightness of all lights: {count:,}")


#################################################

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]

    if n == 1:
        solve_1(path)
    elif n == 2:
        solve_2(path)
