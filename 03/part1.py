x = 0
trees = 0

f = open("input.txt", mode="r", encoding="utf-8-sig")
for l in f:
    line = l.strip()
    length = len(line)
    x = x % length
    if line[x] == "#":
        trees += 1
    x += 3

print(trees)
