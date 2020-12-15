f = open("input.txt", mode="r", encoding="utf-8-sig")
i = 0
prev = []
for l in f:
    line = l.strip()
    num = int(line)

    if i < 25:
        prev.append(num)
        i += 1
        continue

    correct = False
    for x in range(25):
        for y in range(x, 25):
            if prev[x] + prev[y] == num:
                correct = True
                break
    
    if not correct:
        print(num)
        quit()

    prev = prev[1:]
    prev.append(num)
    