from os import sep
with open(f"inputs{sep}day_16.txt") as rf: ds = [int(c) for c in "".join(rf.readline().strip())]
pattern = [0, 1, 0, -1]

def fft(lines, phases=100):
    for i in range(phases):
        digits = []
        idx = 0
        for c in range(len(lines)):
            transform = []
            count = 0
            while len(transform) < len(lines) + 1:
                transform += [pattern[count % 4]] * (idx + 1)
                count+=1
            digits.append(sum([lines[c]*transform[c+1] for c in range(len(lines))]))
            idx+=1
        lines = digits
    return lines
print(fft(ds.copy()))