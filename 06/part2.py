f = open("input.txt", mode="r", encoding="utf-8-sig")

yes = {}
total = 0
first = True
for l in f:
    line = l.strip()
    if line == "":
        total += len(yes)
        yes = {}
        first = True
        continue

    if first == True:
        for c in line:
            yes[c] = True
        first = False
        continue
    
    local_yes = {}
    for c in line:
        local_yes[c] = True

    keys = yes.copy()
    for key in keys:
        if key not in local_yes:
            del yes[key]

print(total)