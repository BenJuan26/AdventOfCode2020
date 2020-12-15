import re
import sys

child_regex = re.compile(r"(\d+) (.+) bag")
required_children = {}

def count_children(color):
    local_total = 0
    if color not in required_children:
        return 0
    else:
        for child in required_children[color]:
            local_total += child["count"] + child["count"]*count_children(child["color"])
        return local_total

f = open("input.txt", mode="r", encoding="utf-8-sig")
for l in f:
    line = l.strip()
    parent, children_string = line.split(" bags contain ", 1)
    
    children = children_string.split(", ")
    children[len(children)-1] = children[len(children)-1][0:-1]

    local_children = []
    for c in children:
        if c == "no other bags":
            continue

        m = child_regex.match(c)
        if m is None:
            print("child regex didn't match for string {}".format(c))
            sys.exit(1)
        count = int(m.group(1))
        color = m.group(2)
        local_children.append({"count": count, "color": color})
    required_children[parent] = local_children

print(count_children("shiny gold"))
    