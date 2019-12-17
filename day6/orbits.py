f = open("orbits.txt", "r")

orbits = {}
deepness = {}

for line in f:
    l = line.strip(")")
    a = l[:3]
    b = l[4:7]
    orbits[b] = a

for e in orbits:
    element = e
    deep = 0
    
    while element in orbits:
        element = orbits[element]
        deep += 1

    deepness[e] = deep

total = 0

for e in deepness:
    total += deepness[e]

print("Part 1 : ", total)

you_element = orbits["YOU"]
san_element = orbits["SAN"]
jumps = 0

while you_element != san_element:
    you_deep = deepness[you_element]
    san_deep = deepness[san_element]

    if you_deep == san_deep:
        you_element = orbits[you_element]
        san_element = orbits[san_element]
        jumps += 2

    elif you_deep < san_deep:
        san_element = orbits[san_element]
        jumps += 1

    elif you_deep > san_deep:
        you_element = orbits[you_element]
        jumps += 1
    
print(jumps)
