f = open("program.txt", "r")

codes = f.readline().split(",")

param_nb = {'1' : 3, '2' : 3, '9' : 0, '3' : 1, '4' :  1, '5' : 2, '6' : 2, '7' : 3, '8' : 3}
rpi = 0

while True:
    inst = codes[rpi]
    inst = '0' * (param_nb[inst[-1]] + 2 - len(inst)) + inst

    if inst[-1] == '1':
        arg1 = 0
        arg2 = 0
        target = 0
        if inst[2] == '1':
            arg1 = int(codes[rpi + 1])
        elif inst[2] == '0':
            arg1 = int(codes[int(codes[rpi + 1])])

        if inst[1] == '1':
            arg2 = int(codes[rpi + 2])
        elif inst[1] == '0':
            arg2 = int(codes[int(codes[rpi + 2])])

        target = int(codes[rpi + 3])
        codes[target] = str(arg1 + arg2)
        rpi += param_nb['1'] + 1

    elif inst[-1] == '2':
        arg1 = 0
        arg2 = 0
        target = 0
        if inst[2] == '1':
            arg1 = int(codes[rpi + 1])
        elif inst[2] == '0':
            arg1 = int(codes[int(codes[rpi + 1])])

        if inst[1] == '1':
            arg2 = int(codes[rpi + 2])
        elif inst[1] == '0':
            arg2 = int(codes[int(codes[rpi + 2])])

        target = int(codes[rpi + 3])

        codes[target] = str(arg1 * arg2)
        rpi += param_nb['2'] + 1

    elif inst[-1] == '3':
        target = int(codes[rpi + 1])

        inp = input("[*] Program has requested an input : ")
        codes[target] = str(inp)
        rpi += param_nb['3'] + 1

    elif inst[-1] == '4':
        arg1 = 0

        if inst[0] == '1':
            arg1 = int(codes[rpi + 1])
        elif inst[0] == '0':
            arg1 = int(codes[int(codes[rpi + 1])])

        print("[*] ", arg1)
        rpi += param_nb['4'] + 1

    elif inst[-1] == '5':
        arg1 = 0

        if inst[1] == '1':
            arg1 = int(codes[rpi + 1])
        elif inst[1] == '0':
            arg1 = int(codes[int(codes[rpi + 1])])

        if arg1 != 0:
            target = int(codes[rpi + 2])
            rpi = target
        else:
            rpi += param_nb['5'] + 1

    elif inst[-1] == '6':
        arg1 = 0
        
        if inst[1] == '1':
            arg1 = int(codes[rpi + 1])
        elif inst[1] == '0':
            arg1 = int(codes[int(codes[rpi + 1])])

        if arg1 == 0:
            target = int(codes[rpi + 2])
            rpi = target
        else:
            rpi += param_nb['6'] + 1

    elif inst[-1] == '7':
        arg1 = 0
        arg2 = 0

        if inst[2] == '1':
            arg1 = int(codes[rpi + 1])
        elif inst[2] == '0':
            arg1 = int(codes[int(codes[rpi + 1])])

        if inst[1] == '1':
            arg2 = int(codes[rpi + 2])
        elif inst[1] == '0':
            arg2 = int(codes[int(codes[rpi + 2])])

        target = int(codes[rpi + 3])

        if arg1 < arg2:
            codes[target] = 1
        else:
            codes[target] = 0

        rpi += param_nb['7'] + 1

    elif inst[-1] == '8':
        arg1 = 0
        arg2 = 0

        if inst[2] == '1':
            arg1 = int(codes[rpi + 1])
        elif inst[2] == '0':
            arg1 = int(codes[int(codes[rpi + 1])])

        if inst[1] == '1':
            arg2 = int(codes[rpi + 2])
        elif inst[1] == '0':
            arg2 = int(codes[int(codes[rpi + 2])])

        target = int(codes[rpi + 3])

        if arg1 == arg2:
            codes[target] = 1
        else:
            codes[target] = 0

        rpi += param_nb['8'] + 1

    elif inst[-1] == '9':
        print("[*] Program halted")
        break

