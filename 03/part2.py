def tree_count(x_step, y_step):
    x = 0
    y = 0
    trees = 0

    f = open("input.txt", mode="r", encoding="utf-8-sig")
    for l in f:
        if y % y_step != 0:
            y += 1
            continue
        line = l.strip()
        length = len(line)
        x = x % length
        if line[x] == "#":
            trees += 1
        x += x_step
        y += 1
    return trees

total = tree_count(1, 1)
total *= tree_count(3, 1)
total *= tree_count(5, 1)
total *= tree_count(7, 1)
total *= tree_count(1, 2)
print(total)
