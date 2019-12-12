from os import sep

class Planet:
    def __init__(self, x=0, y=0, z=0):
        self.position = [x, y, z]
        self.velocity = [0, 0, 0]

    def pull(self, p):
        for i in range(len(self.position)):
            if p.position[i] == self.position[i]: continue
            elif p.position[i] > self.position[i]:
                p.velocity[i] -= 1
                self.velocity[i] += 1
            elif p.position[i] < self.position[i]:
                p.velocity[i] += 1
                self.velocity[i] -= 1

    def move(self):
        for i in range(len(self.velocity)):
            self.position[i] += self.velocity[i]

    def get_kinetic(self):
        return sum([abs(n) for n in self.velocity])

    def get_potential(self):
        return sum([abs(n) for n in self.position])

    def get_total(self):
        return self.get_kinetic() * self.get_potential()

    def get_hash(self):
        return ",".join(map(str, self.position + self.velocity))


    def __repr__(self):
        return f"Position: {self.position} | Velocity: {self.velocity}"

with open(f"inputs{sep}day_12.txt") as rf: lines = [l.replace("<", "").replace(">", "").strip().split("=")[1:] for l in rf.readlines()]
planets = [Planet(x=int(coords[0].split(",")[0]), y=int(coords[1].split(",")[0]), z=int(coords[2].split(",")[0])) for coords in lines]

def update_planets(ps):
    for i in range(len(ps)):
        for j in range(i+1, len(ps)):
            ps[i].pull(ps[j])
    for planet in ps:
        planet.move()

#Part 1:
step_count = 1000
for step in range(step_count):
    update_planets(planets)

print(sum([p.get_total() for p in planets]))
#Answer: 9493
#Part 2:
universe_states = set()
count = 0
#This WILL work, just take...probably forever? Took ~5 mins to do 3.5 mil, and the output is likely in the trillions...based off Reddit data, this should take around 800 years.
def state_hash(ps):
    global count
    count+=1
    sh = "".join([p.get_hash() for p in ps])
    if not sh in universe_states:
        universe_states.add(sh)
    else:
        print(f"Done! Took {count} steps to repeat!")
        exit(0)

while True:
    update_planets(planets)
    state_hash(planets)
#Answer:

