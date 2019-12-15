f = open("opcode.txt", "r")

line = f.read().split(",")
codes = [int(i) for i in line]

codes[1] = 12
codes[2] = 2

i = 0
while i < len(codes):
    if codes[i] == 99:
        print("[*] Program halted with opcode 99")
        break

    arg1 = codes[codes[i + 1]]
    arg2 = codes[codes[i + 2]]
    target = codes[i + 3]


    result = 0

    if codes[i] == 1:
        result = arg1 + arg2
    elif codes[i] == 2:
        result = arg1 * arg2
    else:
        print("[*] Error wrong opcode")

    codes[target] = result
    i += 4

print("[*] Printing result")
print(codes)
