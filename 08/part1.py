import sys

f = open("input.txt", mode="r", encoding="utf-8-sig")
lines = f.readlines()

executed = {}
acc = 0
i = 0
while True:
    if i in executed:
        break

    executed[i] = True

    line = lines[i].strip()
    (instruction, value) = line.split(" ", 1)

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