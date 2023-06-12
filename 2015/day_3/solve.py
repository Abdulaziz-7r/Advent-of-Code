import sys


def solve_1(path):
    with open(path) as f:
        input = f.read().strip()
    x = 0
    y = 0
    houses_grid = [[0, 0]]
    for move in input:
        if move == ">":
            x += 1
        elif move == "<":
            x -= 1
        elif move == "^":
            y += 1
        else:
            y -= 1

        if [x, y] not in houses_grid:
            houses_grid.append([x, y])

    print(len(houses_grid))


def solve_2(path):
    with open(path) as f:
        input = f.read().strip()
    santa_x = 0
    santa_y = 0
    robot_x = 0
    robot_y = 0
    houses_grid = [[0, 0]]
    for i in range(len(input)):
        if input[i] == ">":
            if (i + 1) % 2 == 1:
                santa_x += 1
            else:
                robot_x += 1
        elif input[i] == "<":
            if (i + 1) % 2 == 1:
                santa_x -= 1
            else:
                robot_x -= 1
        elif input[i] == "^":
            if (i + 1) % 2 == 1:
                santa_y += 1
            else:
                robot_y += 1
        else:
            if (i + 1) % 2 == 1:
                santa_y -= 1
            else:
                robot_y -= 1

        if [santa_x, santa_y] not in houses_grid:
            houses_grid.append([santa_x, santa_y])
        if [robot_x, robot_y] not in houses_grid:
            houses_grid.append([robot_x, robot_y])
    print(len(houses_grid))


#################################################

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]

    if n == 1:
        solve_1(path)
    elif n == 2:
        solve_2(path)
