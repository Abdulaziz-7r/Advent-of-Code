import sys


def solve_1(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    nice_str = 0
    vowels = ["a", "e", "i", "o", "u"]
    avoided_string = ["ab", "cd", "pq", "xy"]
    for string in data:
        vowel_count = 0
        double_letter = False
        no_avoided_string = True
        for chr in vowels:
            vowel_count += string.count(chr)
            if vowel_count >= 3:
                break
        if vowel_count < 3:
            continue
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                double_letter = True
                break
        if double_letter == False:
            continue
        for avoid in avoided_string:
            if avoid in string:
                no_avoided_string = False
                break
        if no_avoided_string == False:
            continue

        nice_str += 1
    print(nice_str)


##########################################################


def has_double_pair(string):
    for i in range(len(string) - 1):
        pair = string[i] + string[i + 1]
        for j in range(i + 2, len(string) - 1):
            if pair == (string[j] + string[j + 1]):
                return True
    return False


def has_letter_between(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False


def solve_2(path):
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    count = 0
    for string in data:
        if has_double_pair(string) and has_letter_between(string):
            count += 1
    print(count)


#################################################

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]

    if n == 1:
        solve_1(path)
    elif n == 2:
        solve_2(path)
