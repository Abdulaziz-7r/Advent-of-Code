import sys


def solve_1(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    total = 0 
    for line in data:
        l, w, h = map(int, line.split("x"))
        surface = 2 * (l * w + w * h + h * l)
        slack = min(l * w, w * h, h * l)
        total += surface + slack
    print (total)


def solve_2(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    total = 0
    for line in data:
        l, w, h = map(int, line.split("x"))
        warp = 2 * min(l + w, w + h, h + l)
        bow = l * w * h
        total += warp + bow
    print (total)


#################################################

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]

    if n == 1:
        solve_1(path)
    elif n == 2:
        solve_2(path)
