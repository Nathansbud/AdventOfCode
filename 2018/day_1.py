from os import sep
with open(f"inputs{sep}day_1.txt") as inf:
    lines = [line.strip() for line in inf.readlines()]

def get_freq():
    reached = set() #Set instead of array as array has O(n) access for unknown key, vs O(1)ish for dict/set
    s = 0
    count = 0
    while not s in reached:
        for line in lines:
            count += 1
            reached.add(s)
            s += int(line)
            if s in reached:
                return s

if __name__ == '__main__':
    #Part 1:
    print(sum([int(l) for l in lines]))
    #Answer: 477
    #Part 2:
    print(get_freq())
    #Answer: 390


