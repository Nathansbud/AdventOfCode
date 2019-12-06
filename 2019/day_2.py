from os import sep
with open(f"inputs{sep}day_2.txt") as rf: intcodes = [int(d) for d in rf.readline().split(",")]

def solve_intcodes(ints, noun_init=None, verb_init=None):
    mem = ints.copy()
    if noun_init:
        mem[1] = noun_init
    if verb_init:
        mem[2] = verb_init

    for i in range(0, len(mem), 4):
        if mem[i] == 1: mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
        elif mem[i] == 2: mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
        elif mem[i] == 99: break
    return mem

#Part 1:
solved = solve_intcodes(intcodes, 12, 2)
#Answer: 4138687
#Part 2
ideal_value = 19690720
for x in range(0, 99):
    for y in range(0, 99):
        test_list = solve_intcodes(intcodes, x, y)
        if test_list[0] == ideal_value:
            print(x, y, 100 * x + y)
#Answer: 66, 35, 6635





