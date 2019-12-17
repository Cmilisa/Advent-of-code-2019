low = 130254
high = 678275

total = 0

def chains(s):
    chains = []
    prev = 0

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            chains.append(s[prev:i])
            prev = i

    chains.append(s[prev:len(s)])

    return chains

for i in range(7):
    for j in range(i,10):
        for k in range(j,10):
            for l in range(k,10):
                for m in range(l,10):
                    for n in range(m,10):
                        cont = False
                        nstring = str(i)+str(j)+str(k)+str(l)+str(m)+str(n)
                        
                        for c in chains(nstring):
                            if len(c) == 2:
                                cont = True
                                break

                        if cont:
                            number = int(nstring)
                            if number >= low and number <= high:
                                total += 1

print(total)





