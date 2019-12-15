f = open("opcode.txt", "r")

line = f.read().split(",")
opcodes = [int(i) for i in line]

def code_process(codes):
    i = 0
    temp_codes = codes[:]
    while i < len(temp_codes):
        if temp_codes[i] == 99:
            break

        arg1 = temp_codes[codes[i + 1]]
        arg2 = temp_codes[codes[i + 2]]
        target = temp_codes[i + 3]


        result = 0

        if temp_codes[i] == 1:
            result = arg1 + arg2
        elif temp_codes[i] == 2:
            result = arg1 * arg2
        else:
            #print("[*] Error wrong opcode")
            return([0])

        temp_codes[target] = result
        i += 4

    return(temp_codes)

num_goal = 19690720

for num1 in range(100):
    for num2 in range(100):
        new_codes = opcodes
        new_codes[1] = num1
        new_codes[2] = num2
        if code_process(new_codes)[0] == num_goal:
            val = 100 * num1 + num2
            print(val)
            break

