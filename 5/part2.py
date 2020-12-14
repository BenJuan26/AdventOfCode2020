seats = [False] * 1024
f = open("input.txt", mode="r", encoding="utf-8-sig")
for l in f:
    line = l.strip()

    lower = 0
    for i in range(7):
        if line[i] == "B":
            lower = lower + 2 ** (6-i)
    row = lower

    lower = 0
    for i in range(7,10):
        if line[i] == "R":
            lower = lower + 2 ** (2-i+7)
    col = lower
    seat_id = row * 8 + col
    seats[seat_id] = True

for i in range(1024):
    if seats[i] == False and seats[i-1] == True and seats[i+1] == True:
        print(i)
        break