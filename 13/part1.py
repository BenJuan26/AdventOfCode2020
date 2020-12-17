f = open("input.txt", mode="r", encoding="utf-8-sig")
lines = [l.strip() for l in f]

earliest = int(lines[0])
buses = lines[1].split(",")
actual = earliest
while True:
    for bus in buses:
        if bus == "x":
            continue
        freq = int(bus)
        if actual % freq == 0:
            print((actual - earliest)*freq)
            quit()
    actual += 1
