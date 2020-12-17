# this was a hard one!
f = open("input.txt", mode="r", encoding="utf-8-sig")
lines = [l.strip() for l in f]

buses = lines[1].split(",")
indices = []
i = 0
while i < len(buses):
    if buses[i] != "x":
        indices.append(i)
    i += 1

step = int(buses[indices[0]])
t = 0
i = 1
while i < len(indices):
    freq = int(buses[indices[i]])
    while True:
        if (t+indices[i]) % freq == 0:
            step *= freq
            break
        t += step
    i += 1

print(t)
