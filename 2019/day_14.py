from os import sep

with open(f"inputs{sep}day_14.txt") as rf:
    lines = [l.strip() for l in rf.readlines()]

def make_factory(inp):

    for l in inp:
        components = l.split("=>")
        inputs = [c.strip() for c in components[0].split(",")]
        outputs = components[1].strip()


class Factory:
    def __init__(self, reactions):
        self.reactions = reactions
        self.materials = {}


make_factory(lines)
