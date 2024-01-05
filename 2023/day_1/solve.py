import sys

def solve_1(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    total = 0
    for calibration in data:
        first_digit = ""
        last_digit = ""
        for i in range(len(calibration)):
            if calibration[i].isdigit():
                first_digit = calibration[i]
                break
        for i in range(len(calibration) - 1, -1, -1):
            if calibration[i].isdigit():
                last_digit = calibration[i]
                break
        total += int(first_digit + last_digit)
    print(total)


def solve_2(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    number = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }
    total = 0
    for calibration in data:
        digits = []
        for i in range(len(calibration)):
            if calibration[i].isdigit():
                digits.append(calibration[i])
            else:
                for key in number.keys():
                    if calibration[i:].startswith(key):
                        digits.append(number[key])
        total += int(digits[0] + digits[-1])
    print(total)


#################################################

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]

    if n == 1:
        solve_1(path)
    elif n == 2:
        solve_2(path)
