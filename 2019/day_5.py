from os import sep

with open(f'inputs{sep}day_5.txt') as rf:
    intcodes = [int(l) for l in rf.readline().split(",")]

def execute_computer(values, initial):
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
    i = 0
    has_jumped = False
    while i < len(values):
        opcode = values[i]
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
        elif opcode == 3: values[input_one] = initial
        elif opcode == 4: print(values[input_one])
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
            break
        i += jump_length[opcode] if not has_jumped else 0
        has_jumped = False

#Part 1:
execute_computer(intcodes.copy(), 1)
#Answer: 12896948
print("----")
#Part 2:
execute_computer(intcodes.copy(), 5)
#Answer: 7704130
