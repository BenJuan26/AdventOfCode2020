f = open("input.txt", mode="r", encoding="utf-8-sig")

x = 0
y = 0

direction = 0
directions = ["E", "S", "W", "N"]

def move(current_x, current_y, direction, distance):
    if direction == "E":
        return (current_x+distance, current_y)
    if direction == "S":
        return (current_x, current_y-distance)
    if direction == "W":
        return (current_x-distance, current_y)
    if direction == "N":
        return (current_x, current_y+distance)

for l in f:
    line = l.strip()
    instruction = line[0]
    arg = int(line[1:])

    if instruction == "R":
        direction += int(arg/90)
        direction = direction % 4
    elif instruction == "L":
        direction -= int(arg/90)
        direction = direction % 4
    elif instruction == "F":
        (new_x, new_y) = move(x, y, directions[direction], arg)
        x = new_x
        y = new_y
    else:
        (new_x, new_y) = move(x, y, instruction, arg)
        x = new_x
        y = new_y

print(abs(x) + abs(y))
