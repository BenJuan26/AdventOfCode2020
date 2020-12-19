f = open("input.txt", mode="r", encoding="utf-8-sig")
starting = [int(num) for num in f.readline().strip().split(",")]

history = {}
last = starting[0]
history[last] = 0
i = 1
while i < len(starting):
    num = starting[i]
    history[num] = i
    last = num
    i += 1

current = last
while i < 30000:
    if last in history:
        current = i-1-history[last]
    else:
        current = 0
    history[last] = i-1
    last = current
    i += 1

print(current)