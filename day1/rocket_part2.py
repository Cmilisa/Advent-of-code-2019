f = open("fuel_part2.txt", "r")

total_fuel = 0

for line in f:
    current_fuel = int(int(line) / 3) - 2
    total_fuel += current_fuel

    while current_fuel > 0:
        current_fuel = int(current_fuel / 3) - 2
        if current_fuel > 0:
            total_fuel += current_fuel

print(total_fuel)
