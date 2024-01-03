import sys


def solve_1(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    ...


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
