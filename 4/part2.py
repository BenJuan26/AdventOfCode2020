import sys
import re

running_passport = {}
valid = 0

hgtRegex = re.compile(r"([0-9]+)(cm|in)")
hclRegex = re.compile(r"#[0-9a-f]{6}")
eclRegex = re.compile(r"amb|blu|brn|gry|grn|hzl|oth")
pidRegex = re.compile(r"[0-9]{9}")

f = open("input.txt", mode="r", encoding="utf-8-sig")
for l in f:
    line = l.strip()
    
    if len(line) == 0:
        passport = running_passport.copy()
        running_passport = {}
        byr = 0
        try:
            try:
                byr = int(passport["byr"])
            except ValueError:
                continue
            if byr < 1920 or byr > 2002:
                continue

            iyr = 0
            try:
                iyr = int(passport["iyr"])
            except ValueError:
                continue
            if iyr < 2010 or iyr > 2020:
                continue

            eyr = 0
            try:
                eyr = int(passport["eyr"])
            except ValueError:
                continue
            if eyr < 2020 or eyr > 2030:
                continue

            m = hgtRegex.match(passport["hgt"])
            if m is None:
                continue
            heightValue, heightUnit = m.group(1, 2)
            heightValue = int(heightValue)
            if heightUnit == "cm":
                if heightValue < 150 or heightValue > 193:
                    continue
            if heightUnit == "in":
                if heightValue < 59 or heightValue > 76:
                    continue

            m = hclRegex.match(passport["hcl"])
            if m is None:
                continue

            m = eclRegex.match(passport["ecl"])
            if m is None:
                continue

            m = pidRegex.match(passport["pid"])
            if m is None:
                continue
            
            valid += 1
        except KeyError:
            continue

    fields = line.split(" ")
    for field in fields:
        if field == "":
            continue
        key, value = field.split(":", 1)
        running_passport[key] = value

print(valid)
