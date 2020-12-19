f = open("input.txt", mode="r", encoding="utf-8-sig")

any_valid = [False] * 1000

my_ticket = ""
field_ranges = {}
field_indices = {}
valid_tickets = []
final_fields = {}

# process the input
stage = "prep"
for l in f:
    line = l.strip()
    if line == "":
        continue
    elif line == "your ticket:":
        stage = "my_ticket"
        continue
    elif line == "nearby tickets:":
        stage = "nearby_tickets"
        continue

    if stage == "prep":
        field, ranges = line.split(": ", 1)
        ranges = ranges.split(" or ")
        field_ranges[field] = []
        for r in ranges:
            lower, upper = r.split("-")
            field_ranges[field].append((int(lower), int(upper)))
            for i in range(int(lower), int(upper)+1):
                any_valid[i] = True

    elif stage == "my_ticket":
        my_ticket = [int(f) for f in line.split(",")]

    elif stage == "nearby_tickets":
        values = [int(v) for v in line.split(",")]
        valid = True
        for value in values:
            if not any_valid[value]:
                valid = False
                break
        if not valid:
            continue

        valid_tickets.append(values)

# determine possible correct positions for each field
cols = len(valid_tickets[0])
for field in field_ranges:
    for i in range(cols):
        correct_col = True
        for ticket in valid_tickets:
            value = ticket[i]
            valid = False
            for r in field_ranges[field]:
                if value >= r[0] and value <= r[1]:
                    valid = True
                    break
            if not valid:
                correct_col = False
                break
        if correct_col:
            if field not in field_indices:
                field_indices[field] = {i: True}
            else:
                field_indices[field][i] = True

# process of elimination: narrow down which fields can only be one position and remove that possibility from the other fields
done = False
while not done:
    done = True
    to_delete = []
    for field in field_indices:
        indices = field_indices[field]
        done_this_round = False
        if len(indices) == 1:
            to_delete.append(field)
            i = next(iter(field_indices[field].keys()))
            final_fields[field] = i
            for field2 in field_indices:
                if field2 != field and i in field_indices[field2]:
                    del field_indices[field2][i]
        else:
            done = False
    for field in to_delete:
        del field_indices[field]

# multiply all fields of my ticket that start with "departure"
product = -1
for field in final_fields:
    if field[:9] == "departure":
        value = my_ticket[final_fields[field]]
        if product == -1:
            product = value
        else:
            product *= value

print(product)