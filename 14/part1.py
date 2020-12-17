import re

f = open("input.txt", mode="r", encoding="utf-8-sig")
mem_regex = re.compile(r"mem\[(\d+)\] = (\d+)")

memory = {}

mask = "".join(["X"]*36)
for l in f:
    line = l.strip()
    
    if line[:4] == "mask":
        mask = line[7:]
        continue

    m = mem_regex.match(line)
    address = int(m.group(1))
    value = int(m.group(2))
    masked = value

    for i in range(36):
        bit = mask[35-i]
        if bit == "X":
            continue
        
        if bit == "1":
            masked |= (1<<i)
            continue

        masked &= ~(1<<i)

    memory[address] = masked

total = 0
for key in memory:
    total += memory[key]

print(total)