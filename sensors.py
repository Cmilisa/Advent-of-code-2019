from collections import defaultdict

f = open("program.txt", "r")

codes = f.readline().split(",")
#codes = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(",")
codes = [int(i) for i in codes]

params = {'01' : 'rrw', '02' : 'rrw', '03' : 'w', '04' : 'r',
          '05' : 'rr', '06' : 'rr', '07' : 'rrw', '08' : 'rrw',
          '99' : '', '09' : 'r'}

def run(prog, input_list):
    output = 0
    rpi = 0
    rel_base = 0
    memory = defaultdict(int, enumerate(map(int, prog)))
    while True:
        inst = str(memory[rpi])
        opcode = ('0' + inst)[-2:]
        opsize = len(params[opcode])
        inst = '0' * (opsize + 2 - len(inst)) + inst
        modes = list(inst[:-2])[::-1]

        if opcode == '99':
            print("[*] Program halted")
            break

        args = []
        
        for i in range(0, opsize):
            if params[opcode][i] == 'r':
                if modes[i] == '1':
                    args.append(memory[rpi + 1 + i ])
                elif modes[i] == '2':
                    args.append(memory[memory[rpi + 1 + i] + rel_base])
                elif modes[i] == '0':
                    args.append(memory[memory[rpi + 1 + i]])
            elif params[opcode][i] == 'w':
                if modes[i] == '2':
                    args.append(memory[rpi + 1 + i] + rel_base)
                else:
                    args.append(memory[rpi + 1 + i])

        """print("rpi : ", rpi)
        print("rel_base : ", rel_base)
        print("code : ", memory[rpi:rpi+6])
        print("opcode : ", opcode)
        print("r/w : ", params[opcode])
        print("modes : ", modes)
        print("args : ", args)
        input(">")"""

        if opcode == '01':
            memory[args[2]] = args[0] + args[1]

        elif opcode == '02':
            memory[args[2]] = args[0] * args[1]
            
        elif opcode == '03':
            if input_list == []:
                inp = input("[*] Program has requested an input : ")
            else:
                """inp = input_list[0]
                input_list.remove(inp)"""
                inp = next(input_list)
                
            memory[args[0]] = int(inp)

        elif opcode == '04':
            print("[*] Output", args[0])
            output = args[0]
            #yield output

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
                memory[args[2]] = 1
            else:
                memory[args[2]] = 0

        elif opcode == '08':
            if args[0] == args[1]:
                memory[args[2]] = 1
            else:
                memory[args[2]] = 0

        elif opcode == '09':
            rel_base += args[0]

        else:
            print("[*] Debug output, wrong opcode : ", inst)

        rpi += opsize + 1

    return output

run(codes, [])
