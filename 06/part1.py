f = open("input.txt", mode="r", encoding="utf-8-sig")

yes = {}
total = 0
for l in f:
    line = l.strip()
    if line == "":
        total += len(yes)
        yes = {}
        continue

    for c in line:
        yes[c] = True

print(total)