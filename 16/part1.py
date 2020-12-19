f = open("input.txt", mode="r", encoding="utf-8-sig")

valid = [False] * 1000
total = 0

stage = "prep"
for l in f:
    line = l.strip()
    if line == "":
        continue
    elif line == "your ticket:":
        stage = "my_ticket"
        continue
    elif line == "nearby tickets:":
        stage = "nearby_tickets"
        continue

    if stage == "prep":
        ranges = line.split(": ")[1].split(" or ")
        for r in ranges:
            lower, upper = r.split("-")
            for i in range(int(lower), int(upper)+1):
                valid[i] = True

    elif stage == "my_ticket":
        continue

    elif stage == "nearby_tickets":
        values = line.split(",")
        for v in values:
            value = int(v)
            if not valid[value]:
                total += value

print(total)