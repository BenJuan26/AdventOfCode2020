valid = 0

f = open("input.txt", mode="r", encoding="utf-8-sig")
for line in f:
    sections = line.strip().split(" ")
    limits = sections[0]
    letter = sections[1][0]
    password = sections[2]
    
    lower, upper = limits.split("-", 1)
    lower = int(lower)
    upper = int(upper)

    count = 0
    for char in password:
        if char == letter:
            count += 1
    if count >= lower and count <= upper:
        valid += 1

print(valid)
