import re

f = open("input.txt", mode="r", encoding="utf-8-sig")
mem_regex = re.compile(r"mem\[(\d+)\] = (\d+)")

memory = {}

def float_write(index, floaters, address, value):
    if index >= len(floaters):
        memory[address] = value
        return
    masked = address | (1<<floaters[index])
    float_write(index+1, floaters, masked, value)
    masked = address & ~(1<<floaters[index])
    float_write(index+1, floaters, masked, value)

mask = "".join(["X"]*36)
for l in f:
    line = l.strip()
    
    if line[:4] == "mask":
        mask = line[7:]
        continue

    m = mem_regex.match(line)
    address = int(m.group(1))
    value = int(m.group(2))
    masked = address
    floaters = []

    for i in range(36):
        bit = mask[35-i]
        if bit == "0":
            continue
        
        if bit == "1":
            masked |= (1<<i)
            continue

        floaters.append(i)

    if len(floaters) == 0:
        memory[masked] = value
    else:
        float_write(0, floaters, masked, value)

total = 0
for key in memory:
    total += memory[key]

print(total)