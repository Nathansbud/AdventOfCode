from os import sep
with open(f'inputs{sep}day_3.txt') as rf: left_wire, right_wire = [l.strip("\n").split(",") for l in rf.readlines()]

def compute_path(wire_moves):
    moves = [(0, 0)]
    tiles_covered = []

    index = 0
    for move in wire_moves:
        instruction = move[0]

        if instruction == "U":
            moves.append((moves[index][0], moves[index][1]+int(move[1:])))
            for i in range(moves[index][1], moves[index+1][1]):
                tiles_covered.append((moves[index][0], i))
        elif instruction == "D":
            moves.append((moves[index][0], moves[index][1]-int(move[1:])))
            for i in range(moves[index][1], moves[index + 1][1], -1):
                tiles_covered.append((moves[index][0], i))
        elif instruction == "R":
            moves.append((moves[index][0]+int(move[1:]), moves[index][1]))
            for i in range(moves[index][0], moves[index+1][0]):
                tiles_covered.append((i, moves[index][1]))
        elif instruction == "L":
            moves.append((moves[index][0]-int(move[1:]), moves[index][1]))
            for i in range(moves[index][0], moves[index+1][0], -1):
                tiles_covered.append((i, moves[index][1]))
        index+=1

    return moves, tiles_covered

def shortest_overlaps(a, b):
    left_ends, left_covered = compute_path(a)
    right_ends, right_covered = compute_path(b)
    intersections = set(left_covered).intersection(right_covered)

    minimum, m_intersect, signal, s_intersect = None, None, None, None

    for point in intersections:
        if point != (0, 0):
            dist = abs(point[0]) + abs(point[1])
            sig = left_covered.index(point) + right_covered.index(point)

            if not minimum or minimum > dist:
                minimum = dist
                m_intersect = point

            if not signal or signal > sig:
                signal = sig
                s_intersect = point
    return minimum, m_intersect, signal, s_intersect

#Part 1 & 2:
print(shortest_overlaps(left_wire, right_wire))
#Answer:
# P1: (1983, (81, 1902))
# P2: (107754, (1668, 321))
