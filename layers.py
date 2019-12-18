import numpy as np

f = open("image.txt", "r")

image = f.readline()

f.close()

width = 25
height = 6

pixel_per_layer = width * height

def partition(lst, n):
    division = len(lst) / n
    return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]

layers = partition(image, 100)

fewest = pixel_per_layer
fewest_layer = 0

for i in range(len(layers)):
    zeros_count = 0
    for p in layers[i]:
        if p == '0':
            zeros_count += 1

    if zeros_count < fewest:
        fewest = zeros_count
        fewest_layer = i

one_count = 0
two_count = 0

for p in layers[fewest_layer]:
    if p == '1':
        one_count += 1
    elif p == '2':
        two_count += 1

print(one_count * two_count)

final_image = []

for i in range(len(layers[0])):
    for j in range(len(layers)):
        if layers[j][i] == '1' or layers[j][i] == '0':
            final_image.append(layers[j][i])
            break

for i in range(6):
    line = final_image[i*25:(i+1)*25]
    print([i.replace('0', ' ') for i in line])"""


