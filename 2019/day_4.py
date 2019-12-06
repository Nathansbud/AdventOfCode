from os import sep
with open(f'inputs{sep}day_4.txt') as rf: lower, upper = rf.readline().strip("\n").split("-")

def calculate_passwords():
    matches = set()
    matches_part_2 = set()
    duplicate = False
    ascending = True
    dcount = []
    dc = 1

    for i in range(int(lower), int(upper)):
        si = str(i)

        for j in range(si.__len__() - 1):
            if not int(si[j+1]) - int(si[j]) >= 0:
                ascending = False
            if si[j] == si[j+1]:
                duplicate = True
                dc+=1
                if j + 1 == si.__len__() - 1: dcount.append(dc)
            elif duplicate and dc > 1:
                dcount.append(dc)
                dc = 1
        if ascending and duplicate:
            matches.add(i)
            if 2 in dcount:
                matches_part_2.add(i)
        ascending = True
        duplicate = False
        dcount = []
        dc = 1
    return matches, matches_part_2

#Part 1, 2:
print([len(l) for l in calculate_passwords()])
#Answer: 481, 299