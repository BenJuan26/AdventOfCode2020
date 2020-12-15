import math

f = open("input.txt", mode="r", encoding="utf-8-sig")
numbers = [int(l.strip()) for l in f]

invalid = 41682220 # from part1

start = 0
while start < len(numbers):
    total = numbers[start]
    for end in range(start+1, len(numbers)):
        total += numbers[end]
        if total > invalid:
            start += 1
            break

        if total == invalid:
            small = math.inf
            big = 0
            for i in range(start, end+1):
                small = min(small, numbers[i])
                big = max(big, numbers[i])
            
            print(small + big)
            quit()
