from os import sep
import re
from PIL import Image

w = 25
h = 6
with open(f"inputs{sep}day_8.txt") as rf: layers = re.findall(f'{"."*(w*h)}?',rf.readline().strip())

#Part 1:
zero_counts = [l.count("0") for l in layers]
min_index = zero_counts.index(min(zero_counts))
print(layers[min_index].count("1")*layers[min_index].count("2"))
#Answer: 1620
#Part 2:
pixels = {
    i:"" for i in range(w*h)
}
pixel_map = {
    "0":(0, 0, 0, 0),
    "1":(255, 255, 255, 0),
    "2":(0, 0, 0, 255)
}

for pixel in range(w*h):
    for layer in range(len(layers)):
        if layers[layer][pixel] != "2":
            pixels[pixel] = pixel_map[layers[layer][pixel]]
            break
    else:
        pixels[pixel] = pixel_map["2"]

output = Image.new("RGB", (w, h))
output.putdata([p for p in pixels.values()])
output.save(f"outputs{sep}day_8.png", "PNG")
#Answer: BCYEF
