import sys


def solve_1(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]

    red = 12
    green = 13
    blue = 14
    game_num = 1
    id_sum = 0

    for game in data:
        flag = False
        game = game[(game.index(":") + 2) :]
        sets = game.split(";")
        for set in sets:
            set = set.strip().replace(",", "")
            cubes = set.split(" ")
            for i in range(0, len(cubes), 2):
                if cubes[i + 1] == "red":
                    if int(cubes[i]) > red:
                        flag = True
                        break
                elif cubes[i + 1] == "green":
                    if int(cubes[i]) > green:
                        flag = True
                        break
                elif cubes[i + 1] == "blue":
                    if int(cubes[i]) > blue:
                        flag = True
                        break
            if flag:
                break
        if flag:
            game_num += 1
            continue
        id_sum += game_num
        game_num += 1
    
    print(id_sum)

def solve_2(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    ...


#################################################

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]

    if n == 1:
        solve_1(path)
    elif n == 2:
        solve_2(path)
