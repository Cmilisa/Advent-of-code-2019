from itertools import chain, permutations

f = open("program.txt", "r")

codes = f.readline().split(",")
"""codes = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,\
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(",")"""
codes = [int(i) for i in codes]

params = {'01' : 'rrw', '02' : 'rrw', '03' : 'w', '04' : 'r',
          '05' : 'rr', '06' : 'rr', '07' : 'rrw', '08' : 'rrw',
          '99' : ''}

def run(input_list):
    output = 0
    rpi = 0
    while True:
        inst = str(codes[rpi])
        opcode = ('0' + inst)[-2:]
        opsize = len(params[opcode])
        inst = '0' * (opsize + 2 - len(inst)) + inst
        modes = list(inst[:-2])[::-1]

        if opcode == '99':
            #print("[*] Program halted")
            break

        args = []
        
        for i in range(0, opsize):
            if params[opcode][i] == 'r':
                if modes[i] == '1':
                    args.append(codes[rpi + 1 + i ])
                elif modes[i] == '0':
                    args.append(codes[codes[rpi + 1 + i]])
            elif params[opcode][i] == 'w':
                args.append(codes[rpi + 1 + i])

        """print("rpi : ", rpi)
        print("code : ", codes[rpi:rpi+6])
        print("opcode : ", opcode)
        print("r/w : ", params[opcode])
        print("modes : ", modes)
        print("args : ", args)
        input(">")"""

        if opcode == '01':
            codes[args[2]] = args[0] + args[1]

        elif opcode == '02':
            codes[args[2]] = args[0] * args[1]
            
        elif opcode == '03':
            if input_list == []:
                inp = input("[*] Program has requested an input : ")
            else:
                """inp = input_list[0]
                input_list.remove(inp)"""
                inp = next(input_list)
                
            codes[args[0]] = int(inp)

        elif opcode == '04':
            #print("[*] Output", args[0])
            output = args[0]
            yield output

        elif opcode == '05':
            if args[0] != 0:
                rpi = args[1]
                continue

        elif opcode == '06':
            if args[0] == 0:
                rpi = args[1]
                continue       

        elif opcode == '07':
            if args[0] < args[1]:
                codes[args[2]] = 1
            else:
                codes[args[2]] = 0

        elif opcode == '08':
            if args[0] == args[1]:
                codes[args[2]] = 1
            else:
                codes[args[2]] = 0

        else:
            print("[*] Debug output, wrong opcode : ", inst)

        rpi += opsize + 1

    #return output


max_amp = 0

#Part 1
"""for phases in itertools.permutations([0,1,2,3,4]):
    amplitude = 0
    for p in phases:
        vm = run(iter([p, amplitude]))
        amplitude = next(vm)

    max_amp = max(max_amp, amplitude)"""

#Part 2
for phases in permutations([5, 6, 7, 8, 9]):
    amplitude = 0

    def amp1():
        yield from run(chain(iter([phases[0], 0]), amp5()))

    def amp2():
        yield from run(chain(iter([phases[1]]), amp1()))

    def amp3():
        yield from run(chain(iter([phases[2]]), amp2()))

    def amp4():
        yield from run(chain(iter([phases[3]]), amp3()))

    def amp5():
        yield from run(chain(iter([phases[4]]), amp4()))

    outputs = list(amp5())
    max_amp = max(max_amp, outputs[-1])

print(max_amp)
