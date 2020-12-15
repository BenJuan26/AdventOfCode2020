import re
import sys

child_regex = re.compile(r"\d+ (.+) bag")
potential_parents = {}

total_parents = {}

def populate_parents(color):
    if color not in potential_parents:
        total_parents[color] = True
    else:
        for parent_color in potential_parents[color]:
            total_parents[color] = True
            populate_parents(parent_color)

f = open("input.txt", mode="r", encoding="utf-8-sig")
for l in f:
    line = l.strip()
    parent, children_string = line.split(" bags contain ", 1)
    
    children = children_string.split(", ")
    children[len(children)-1] = children[len(children)-1][0:-1]

    for c in children:
        if c == "no other bags":
            continue

        m = child_regex.match(c)
        if m is None:
            print("child regex didn't match for string {}".format(c))
            sys.exit(1)
        color = m.group(1)
        if color in potential_parents:
            potential_parents[color].append(parent)
        else:
            potential_parents[color] = [parent]

populate_parents("shiny gold")
# total_parents will include the target colour itself
print(len(total_parents) - 1)
    