f = open("fuel.txt", "r")

total_sum = 0

for line in f:
    total_sum += int(int(line) / 3) - 2

print(total_sum)
