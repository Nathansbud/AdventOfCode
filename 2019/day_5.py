from os import sep

with open(f'inputs{sep}day_5.txt') as rf:
    intcodes = [int(l) for l in rf.readline().split(",")]

#okay this needs work, this is just abysmal lmfao
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
    i = 0
    has_jumped = False
    while i < len(values):
        opcode = values[i]
        if opcode == 1: values[values[i+3]] = values[values[i+1]] + values[values[i + 2]]
        elif opcode == 2: values[values[i+3]] = values[values[i + 1]] * values[values[i + 2]]
        elif opcode == 3: values[values[i+1]] = initial
        elif opcode == 4: print(values[values[i+1]])
        elif opcode == 5:
            if values[values[i+1]] != 0:
                i = values[values[i+2]]
                has_jumped = True
        elif opcode == 6:
            if values[values[i+1]] == 0:
                i = values[values[i+2]]
                has_jumped = True
            pass
        elif opcode == 7:
            if values[values[i+1]] < values[values[i+2]]:
                values[values[i+3]] = 1
            else:
                values[values[i+3]] = 0
        elif opcode == 8:
            if values[values[i+1]] == values[values[i+2]]:
                values[values[i+3]] = 1
            else:
                values[values[i + 3]] = 0
        elif opcode == 99:
            break
        else:
            instruction = str(opcode)
            opcode = int(instruction[-2:])
            mode_one = int(instruction[-3])
            mode_two = int(instruction[-4]) if len(instruction) >= 4 else 0
            mode_three = int(instruction[-5]) if len(instruction) >= 5 else 0
            # print(instruction, opcode, mode_one, mode_two, mode_three)

            if opcode == 1:
                values[(i+3) if mode_three == 1 else values[i+3]] = (values[i+1] if mode_one == 1 else values[values[i+1]]) + (values[i+2] if mode_two == 1 else values[values[i+2]])
            elif opcode == 2:
                values[(i+3) if mode_three == 1 else values[i+3]] = (values[i+1] if mode_one == 1 else values[values[i+1]]) * (values[i+2] if mode_two == 1 else values[values[i+2]])
            elif opcode == 3: values[(i+1) if mode_one == 1 else values[i+1]] = initial
            elif opcode == 4: print(values[(i+1) if mode_one == 1 else values[i+1]])
            elif opcode == 5:
                if values[(i + 1) if mode_one == 1 else values[i+1]] != 0:
                    i = values[(i+2) if mode_two == 1 else values[i + 2]]
                    has_jumped = True
            elif opcode == 6:
                if values[(i + 1) if mode_one == 1 else values[i+1]] == 0:
                    i = values[(i+2) if mode_two == 1 else values[i + 2]]
                    has_jumped = True
                pass
            elif opcode == 7:
                if values[(i + 1) if mode_one == 1 else values[i+1]] < values[(i+2) if mode_two == 1 else values[i + 2]]:
                    values[(i+3) if mode_three == 1 else values[i+3]] = 1
                else:
                    values[(i+3) if mode_three == 1 else values[i+3]] = 0
            elif opcode == 8:
                if values[(i + 1) if mode_one == 1 else values[i+1]] == values[(i+2) if mode_two == 1 else values[i + 2]]:
                    values[(i+3) if mode_three == 1 else values[i+3]] = 1
                else:
                    values[(i+3) if mode_three == 1 else values[i+3]] = 0
            elif opcode == 99:
                break

        i += jump_length[opcode] if not has_jumped else 0
        has_jumped = False


if __name__ == '__main__':
    #Part 1:
    execute_computer(intcodes.copy(), 1)
    #Answer: 12896948
    print("----")
    #Part 2:
    execute_computer(intcodes.copy(), 5)
    #Answer: 7704130
    pass
