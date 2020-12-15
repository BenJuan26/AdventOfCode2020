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
    if password[lower-1] == letter:
        count += 1
    try:
        if password[upper-1] == letter:
            count += 1
    except IndexError:
        print("{} out of range for {}".format(upper+1, password))
    if count == 1:
        valid += 1

print(valid)
