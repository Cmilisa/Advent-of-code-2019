import itertools

f = open("program.txt", "r")

#codes = f.readline().split(",")
codes = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,\
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(",")
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
            rpi += opsize + 1

        elif opcode == '02':
            codes[args[2]] = args[0] * args[1]
            rpi += opsize + 1
            
        elif opcode == '03':
            if input_list == []:
                inp = input("[*] Program has requested an input : ")
            else:
                inp = input_list[0]
                input_list.remove(inp)
                
            codes[args[0]] = int(inp)
            rpi += opsize + 1

        elif opcode == '04':
            #print("[*] Output", args[0])
            output = args[0]
            rpi += opsize + 1

        elif opcode == '05':
            if args[0] != 0:
                rpi = args[1]
            else:
                rpi += opsize + 1

        elif opcode == '06':
            if args[0] == 0:
                rpi = args[1]
            else:
                rpi += opsize + 1

        elif opcode == '07':
            if args[0] < args[1]:
                codes[args[2]] = 1
            else:
                codes[args[2]] = 0

            rpi += opsize + 1

        elif opcode == '08':
            if args[0] == args[1]:
                codes[args[2]] = 1
            else:
                codes[args[2]] = 0

            rpi += opsize + 1

        else:
            print("[*] Debug output, wrong opcode : ", inst)

    return output


max_amp = 0
max_phases = []

for phases in itertools.permutations([0,1,2,3,4]):
    amplitude = 0
    for p in phases:
        amplitude = run([p, amplitude])

    if amplitude > max_amp:
        max_amp = amplitude
        max_phases = phases
    
print(max_amp)
print(max_phases)
