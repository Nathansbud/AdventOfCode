from os import sep

with open(f'inputs{sep}day_9.txt') as rf:
    value_set = rf.readline().split(",")
    mem = {n:int(l) for l, n in zip(value_set, range(len(value_set)))}
    mem["ptr"] = 0
    mem["rel"] = 0

jump_length = {
    1:4,
    2:4,
    3:2,
    4:2,
    5:3,
    6:3,
    7:4,
    8:4,
    9:2,
    99:0
}

def execute_computer(values, initial):
    opcodes = set(jump_length.keys())
    i = 0
    while True:
        has_jumped = False
        ptr = values["ptr"]
        rel = values["rel"]

        opcode = values[values["ptr"]]

        if ptr not in values: values[ptr] = 0
        if ptr + 1 not in values: values[ptr + 1] = 0
        if ptr + 2 not in values: values[ptr + 2] = 0
        if ptr + 3 not in values: values[ptr + 3] = 0

        if values[ptr] not in values: values[values[ptr]] = 0
        if values[ptr + 1] not in values: values[values[ptr + 1]] = 0
        if values[ptr + 2] not in values: values[values[ptr + 2]] = 0
        if values[ptr + 3] not in values: values[values[ptr + 3]] = 0

        if rel + values[ptr] not in values: values[rel + values[ptr]] = 0
        if rel + values[ptr + 1] not in values: values[rel + values[ptr + 1]] = 0
        if rel + values[ptr + 2] not in values: values[rel + values[ptr + 2]] = 0
        if rel + values[ptr + 3] not in values: values[rel + values[ptr + 3]] = 0

        instruction = "00000"
        if not opcode in opcodes:
            instruction = str(opcode)
            opcode = int(instruction[-2:])

        if not len(instruction) >= 3: i1 = values[ptr+1]
        else: i1 = values[ptr+1] if instruction[-3] == 0 else ptr + 1 if instruction[-3] == 1 else values[rel+values[ptr+1]]

        if not len(instruction) >= 4: i2 = values[ptr+2]
        else: i2 = values[ptr+2] if instruction[-4] == 0 else ptr + 2 if instruction[-4] == 1 else values[rel+values[ptr+2]]

        if not len(instruction) >= 5: i3 = values[ptr+3]
        else: i3 = values[ptr+3] if instruction[-5] == 0 else ptr + 3 if instruction[-5] == 1 else values[rel+values[ptr+3]]

        if i1 not in values: values[i1] = 0
        if i2 not in values: values[i2] = 0
        if i3 not in values: values[i3] = 0

        if opcode == 1:
            values[i3] = values[i1] + values[i2]
        elif opcode == 2: values[i3] = values[i1] * values[i2]
        elif opcode == 3: values[i1] = initial
        elif opcode == 4: print(values[i1])
        elif opcode == 5:
            if values[i1] != 0:
                values["ptr"] = values[i2]
                has_jumped = True
        elif opcode == 6:
            if values[i1] == 0:
                values["ptr"] = values[i2]
                has_jumped = True
        elif opcode == 7: values[i3] = 1 if values[i1] < values[i2] else 0
        elif opcode == 8: values[i3] = 1 if values[i1] == values[i2] else 0
        elif opcode == 9: values["rel"] += values[i1]
        elif opcode == 99: break
        values["ptr"] += jump_length[opcode] if not has_jumped else 0

#Part 1:
execute_computer(mem.copy(), 1)
#Answer: 12896948