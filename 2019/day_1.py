from math import floor
from os import sep
with open(f'inputs{sep}day_1.txt') as rf: components = [int(l) for l in rf.readlines()]

def fuel_from_mass(mass):
    return floor(mass / 3) - 2

def fuel_for_mass_including_fuel(mass):
    fuel = fuel_from_mass(mass)

    fuel_extra = fuel
    while fuel_extra >= 0:
        fuel_extra = fuel_from_mass(fuel_extra)
        fuel += fuel_extra if fuel_extra > 0 else 0
    return fuel

#Part 1:
print(sum([fuel_from_mass(c) for c in components]))
#Part 2:
print(sum([fuel_for_mass_including_fuel(c) for c in components]))




