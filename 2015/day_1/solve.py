import sys

def solve_1(path):
    with open(path) as f:
        input = f.read().strip()
    print(input.count('(') - input.count(')')) 

def solve_2(path):
    with open(path) as f:
        input = f.read().strip()    
    output = 0
    for i in range(len(input)):
        if input[i] == '(':
            output += 1
        else:
            output -= 1
        if output == -1:
            print(i + 1)
            return 

#################################################

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]

    if n == 1:
        solve_1(path)
    elif n == 2:
        solve_2(path)