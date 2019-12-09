from os import sep
from itertools import permutations
with open(f'inputs{sep}day_7.txt') as rf: intcodes = [int(l) for l in rf.readline().split(",")]

phase_settings = [p for p in permutations("01234")]
feedback_settings = [p for p in permutations("56789")]

def execute_computer(values, initial, inp, iptr=0):
    jump_length = {
        1:4,
        2:4,
        3:2,
        4:2,
        5:3,
        6:3,
        7:4,
        8:4,
        99:0
    }
    opcodes = set(jump_length.keys())
    i = iptr
    has_jumped = False
    has_input = False
    while i < len(values):
        opcode = values[i]
        if opcode == 99: return None, i
        input_one = values[i+1]
        input_two = values[i+2] if i + 2 < len(values) - 1 else 0
        input_three = values[i + 3] if i + 3 < len(values) - 1 else 0
        if not opcode in opcodes:
            instruction = str(opcode)
            opcode = int(instruction[-2:])
            input_one = i+1 if int(instruction[-3]) == 1 else values[i+1]
            input_two = i+2 if len(instruction) >= 4 and int(instruction[-4]) == 1 else values[i+2]
            input_three = i+3 if len(instruction) >= 5 and int(instruction[-5]) == 1 else values[i+3]

        if opcode == 1: values[input_three] = values[input_one] + values[input_two]
        elif opcode == 2: values[input_three] = values[input_one] * values[input_two]
        elif opcode == 3:
            if not has_input:
                values[input_one] = initial
                has_input = True
            else:
                values[input_one] = inp
        elif opcode == 4:
            return values[input_one], i+2
        elif opcode == 5:
            if values[input_one] != 0:
                i = values[input_two]
                has_jumped = True
        elif opcode == 6:
            if values[input_one] == 0:
                i = values[input_two]
                has_jumped = True
            pass
        elif opcode == 7:
            if values[input_one] < values[input_two]:
                values[input_three] = 1
            else:
                values[input_three] = 0
        elif opcode == 8:
            if values[input_one] == values[input_two]:
                values[input_three] = 1
            else:
                values[input_three] = 0
        elif opcode == 99:
            return None, i
        i += jump_length[opcode] if not has_jumped else 0
        has_jumped = False

#Part 1:
start = 0
outputs = set()
for setting in phase_settings:
    for n in range(len(setting)):
        start = execute_computer(intcodes.copy(), int(setting[n]), int(start))[0]
    outputs.add(start)
    start = 0
print(max(outputs))
#Answer: 21760
#Part 2:
start = 0
outputs = []
keep_looping = True

for setting in feedback_settings:
    amp_memory = [tc.copy()] * 5
    amp_pointer = [0]*5
    n = 0
    last_output = 0
    while keep_looping:
        out = execute_computer(amp_memory[n%5], int(setting[n%5]), int(start), iptr=amp_pointer[n%5])
        amp_pointer[n % 5] = out[1]

        if out[0]:
            start = out[0]
            if n % 5 == 4:
                last_output = start
        elif n % 5 == 4:
            outputs.append(last_output)
            break
        n += 1
    start = 0
print(max(outputs))
#Answer: