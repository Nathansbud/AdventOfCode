from os import sep
from math import sqrt, atan2, pi

with open(f'inputs{sep}day_10.txt') as rf:
    space_map = [[int(l) for l in list(line.replace("#", "1").replace(".", "0").strip())] for line in rf.readlines()]
    # asteroids = [[(j, i) for i, val in enumerate(row) if val == 1] for j, row in enumerate(space_map)] #Non-flattened
    asteroids = []
    for j, row in enumerate(space_map):
        for i, val in enumerate(row):
            if val == 1: asteroids.append((j, i))

def vector(a, b):
    return tuple([b[d] - a[d] for d in range(len(b))])

def magnitude(v):
    return sqrt(sum(d**2 for d in v))

def normalize(v):
    return tuple([d/magnitude(v) for d in v])

def argument(v):
    return atan2(v[1], v[0])

#Part 1:
def calculate_sums():
    seen = {}
    for asteroid in asteroids:
        distances = set()
        for comp in asteroids:
            if comp != asteroid:
                offset = vector(asteroid, comp)
                distances.add(argument(offset))
        seen[len(distances)] = asteroid
    return seen

performances = calculate_sums()

# print(max(performances), performances[max(performances)])
#Answer: 344
#Part 2:
def calculate_vaporized(ast):
    distances = {}
    print(ast)
    for comp in asteroids:
        if comp != ast:
            offset = vector(ast, comp)
            ao = argument(offset)
            translated_argument = -1*ao+pi if ao < 0 else ao
            if translated_argument in distances:
                distances[translated_argument].append(comp)
            else:
                distances[translated_argument] = [comp]
    sorted_distances = sorted([[k, distances[k]]for k in distances], key=lambda x: x[0], reverse=True)

    start_index = 0
    for ind in range(len(sorted_distances)):
        if sorted_distances[ind][0] == pi/2:
            start_index = ind
            break
    sorted_distances = sorted_distances[start_index:] + sorted_distances[0:start_index]
    destroy_order = []

    ai = 0
    while len(destroy_order) < 205:
        if ai == len(sorted_distances):
            ai = 0
        if not len(sorted_distances) == 0:
            if len(sorted_distances[ai][1]) == 1:
                destroy_order.append(sorted_distances[ai][1][0])
                sorted_distances[ai][1] = []
            else:
                v = sorted_distances[ai][1][0]
                dist = magnitude(vector(ast, v))
                for n in sorted_distances[ai][1][1:]:
                    if magnitude(vector(ast, n)) < dist:
                        v = n
                        dist = magnitude(vector(ast, v))
                destroy_order.append(v)
                sorted_distances[ai][1].remove(v)
        ai+=1

    destroy_200 = destroy_order[199]
    for d in destroy_order:
        print(d[0]*100 + d[1])

    print(destroy_order)
    print(destroy_200)
    print(destroy_200[0]*100 + destroy_200[1])


calculate_vaporized(performances[max(performances)])
#Answer: ???







