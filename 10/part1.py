f = open("input.txt", mode="r", encoding="utf-8-sig")
numbers = [int(l.strip()) for l in f]
numbers.sort()

# add the device itself
numbers.append(numbers[-1] + 3)

prev = 0
ones = 0
twos = 0
threes = 0
for num in numbers:
    diff = num - prev
    if diff == 1:
        ones += 1
    elif diff == 2:
        twos += 1
    elif diff == 3:
        threes += 1
    prev = num

print(ones * threes)