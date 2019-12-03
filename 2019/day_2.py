"""Opcodes:
    - 1: Adds together numbers from 2 positions and stores in a 3rd; numbers after the opcode tell these positions. First 2 are positions to read from, 3rd is position to output to
    - 2: Multiplies together numbers from 2 positions and stores in a 3rd 
    - Addr(1) = Noun
    - Addr(2) = Verb
"""
intcodes = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0]

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

if __name__ == '__main__':
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





