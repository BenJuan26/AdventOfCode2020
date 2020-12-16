f = open("input.txt", mode="r", encoding="utf-8-sig")

x = 0
y = 0

w_x = 10
w_y = 1

def move_waypoint(direction, distance):
    global w_x
    global w_y
    if direction == "E":
        w_x += distance
    elif direction == "S":
        w_y -= distance
    elif direction == "W":
        w_x -= distance
    elif direction == "N":
        w_y += distance

def rotate_waypoint(degrees):
    global w_x
    global w_y
    if degrees == 90:
        temp_x = w_x
        w_x = w_y
        w_y = -temp_x
    elif degrees == 180:
        w_x = -w_x
        w_y = -w_y
    elif degrees == 270:
        temp_x = w_x
        w_x = -w_y
        w_y = temp_x

for l in f:
    line = l.strip()
    instruction = line[0]
    arg = int(line[1:])

    if instruction == "R":
        rotate_waypoint(arg)
    elif instruction == "L":
        rotate_waypoint(360-arg)
    elif instruction == "F":
        x += w_x * arg
        y += w_y * arg
    else:
        move_waypoint(instruction, arg)

print(abs(x) + abs(y))
