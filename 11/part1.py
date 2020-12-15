f = open("input.txt", mode="r", encoding="utf-8-sig")
grid = [list(l.strip()) for l in f]

cols = len(grid[0])
rows = len(grid)

def deep_copy(seats):
    new_seats = [row[:] for row in seats]
    return new_seats

def should_empty(seats, target_x, target_y):
    total = 0
    for x in range(target_x-1, target_x+2):
        if x < 0 or x >= cols:
            continue
        for y in range(target_y-1, target_y+2):
            if y < 0 or y >= rows or (x == target_x and y == target_y):
                continue
            if seats[y][x] == "#":
                total += 1
                if total >= 4:
                    return True
    return False

def should_occupy(seats, target_x, target_y):
    total = 0
    for x in range(target_x-1, target_x+2):
        if x < 0 or x >= cols:
            continue
        for y in range(target_y-1, target_y+2):
            if y < 0 or y >= rows or (x == target_x and y == target_y):
                continue
            if seats[y][x] == "#":
                total += 1
    if total == 0:
        return True
    return False

def run(seats):
    new_seats = deep_copy(seats)
    changed = False
    for y in range(rows):
        for x in range(cols):
            current_seat = seats[y][x]
            if current_seat == ".":
                continue
            if current_seat == "#" and should_empty(seats, x, y):
                new_seats[y][x] = "L"
                changed = True
                continue
            if current_seat == "L" and should_occupy(seats, x, y):
                changed = True
                new_seats[y][x] = "#"
    return (new_seats, changed)

def count_occupied(seats):
    total = 0
    for y in range(rows):
        for x in range(cols):
            if seats[y][x] == "#":
                total += 1
    return total

# used for debugging but nice to have either way
def pretty_print(seats):
    for line in seats:
        print("".join(line))
    print("")

(new_seats, changed) = run(grid)
while changed:
    (new_seats, changed) = run(new_seats)
print(count_occupied(new_seats))