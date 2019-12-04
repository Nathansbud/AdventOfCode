with open("day_2.txt") as rf:
    lines = [line.strip() for line in rf.readlines()]

def find_diff():
    def get_single_diff():
        diff = 0
        shared = (None, None)
        for line in lines:
            for l in lines:
                for a, b in zip(list(line), list(l)):
                    if a != b: diff += 1
                if diff == 1:
                    return line, l
                diff = 0
    f, s = get_single_diff()
    matches = []
    for i in range(len(f)):
        if f[i] == s[i]: matches.append(f[i])
    return "".join(matches)

if __name__ == '__main__':
    #Part 1:
    counts = {"2":0, "3":0}
    for line in lines:
        vals = {c:line.count(c) for c in line}.values()
        if 2 in vals: counts["2"]+=1
        if 3 in vals: counts["3"]+=1
    print(counts["2"]*counts["3"])
    #Answer: 5658
    #Part 2:
    # jesus christ this is inelegant code
    print(find_diff())
    #Answer: nmgyjkpruszlbaqwficavxneo




