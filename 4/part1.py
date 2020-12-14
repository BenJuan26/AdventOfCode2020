template = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False
}
passport = template.copy()
valid = 0

f = open("input.txt", mode="r", encoding="utf-8-sig")
for l in f:
    line = l.strip()
    
    if len(line) == 0:
        current_valid = True
        for key in passport:
            if passport[key] == False:
                current_valid = False
        if current_valid == True:
            valid += 1
        passport = template.copy()
        continue

    fields = line.split(" ")
    for field in fields:
        key, value = field.split(":", 1)
        passport[key] = True

print(valid)
