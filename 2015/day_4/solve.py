import sys
import hashlib


def starting_zeros(num_zeros, input):
    num = 1
    while True:
        key = input + str(num)
        hashed = hashlib.md5(key.encode()).hexdigest()
        if hashed[:num_zeros] == num_zeros * "0":
            break
        num += 1
    print(num, key)


def solve_1(path):
    with open(path) as f:
        input = f.read().strip()
    starting_zeros(5, input)


def solve_2(path):
    with open(path) as f:
        input = f.read().strip()
    starting_zeros(6, input)


#################################################

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]

    if n == 1:
        solve_1(path)
    elif n == 2:
        solve_2(path)
