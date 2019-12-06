from os import sep
with open(f"inputs{sep}day_6.txt") as rf:
    orbit_map = [l.strip("\n").split(")") for l in rf.readlines()]

planets = {}

for pair in orbit_map:
    if not pair[0] in planets:
        planets[pair[0]] = {'parent':'', 'children':set()}
    planets[pair[0]]['children'].add(pair[1])

    if not pair[1] in planets:
        planets[pair[1]] = {'parent':'', 'children':set()}
    planets[pair[1]]['parent'] = pair[0]

#Part 1:
direct_orbits = 0
indirect_orbits = 0
for planet in planets:
    direct_orbits += 1 if planets[planet]['parent'].__len__() > 0 else 0
    parent = planets[planet]['parent']
    while len(parent) > 0:
        parent = planets[parent]['parent']
        indirect_orbits += 1 if parent else 0
print(direct_orbits + indirect_orbits)
#Answer: 273985
#Part 2:
you, san = planets['YOU'], planets['SAN']
yp, sp = planets[you['parent']]['parent'], planets[san['parent']]['parent']
you_path, san_path = {}, {}

dist = 1
while len(yp) > 0:
    you_path[yp] = dist
    yp = planets[yp]['parent']
    dist += 1

print(you_path)

dist = 1
while len(sp) > 0:
    if sp in you_path:
        print(dist + you_path[sp])
        break
    else:
        sp = planets[sp]['parent']
        dist += 1
#Answer: 460


