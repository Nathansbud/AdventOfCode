from os import sep

with open(f'inputs{sep}day_3.txt') as rf:
    lines = [line.strip() for line in rf.readlines()]

class Claim:
    def __init__(self, owner=None, origin=None, span=None):
        self.owner = owner
        self.origin = origin
        self.x = int(origin[0])
        self.w = int(span[0])
        self.y = int(origin[1])
        self.h = int(span[1])
        self.span = span

    def get_area(self):
        return int(self.span[0])*int(self.span[1])

def make_claims(claim_set):
    claims = set()
    for c in claim_set:
        cs = c.split()
        owner = int(cs[0][1:])
        origin = tuple(cs[2][:-1].split(","))
        span = tuple(cs[3].split("x"))
        claims.add(Claim(owner, origin, span))
    return claims

if __name__ == '__main__':
    elf_claims = make_claims(lines)
    #Part 1:
    def make_board(claim_set):
        tiles = {}
        for claim in elf_claims:
            for i in range(claim.x, claim.x + claim.w):
                for j in range(claim.y, claim.y + claim.h):
                    if not f"{i},{j}" in tiles: tiles[f"{i},{j}"] = 1
                    else: tiles[f"{i},{j}"] += 1
        return tiles, len([v for v in tiles.values() if v > 1])
    print(make_board(elf_claims)[1])
    #Answer: 100595
    #Part 2:
    def get_lonely_claim(claim_set):
        tiles = make_board(elf_claims)[0]
        all_alone = True
        for claim in claim_set:
            for i in range(claim.x, claim.x + claim.w):
                for j in range(claim.y, claim.y + claim.h):
                    if tiles[f"{i},{j}"] != 1:
                        all_alone = False
                    if not all_alone: break
                if not all_alone: break
            if all_alone: return claim.owner
            all_alone = True
    print(get_lonely_claim(elf_claims))
    #Answer: 415
