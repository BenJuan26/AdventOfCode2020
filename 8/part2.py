import sys

f = open("input.txt", mode="r", encoding="utf-8-sig")
lines = [l.strip() for l in f]

executed = {}
acc = 0
i = 0
flip_index = 0

while i < len(lines):
    if i in executed:
        executed = {}
        i = 0
        acc = 0
        flip_index += 1
        continue

    executed[i] = True

    (instruction, value) = lines[i].split(" ", 1)
    if i == flip_index:
        if instruction == "jmp":
            instruction = "nop"
        elif instruction == "nop":
            instruction = "jmp"

    if instruction == "acc":
        num = int(value)
        acc += num
        i += 1
        continue
    
    if instruction == "jmp":
        num = int(value)
        i += num
        continue

    if instruction == "nop":
        i += 1
        continue

    print("unknown instruction {}".format(instruction))
    sys.exit(1)

print(acc)