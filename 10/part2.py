f = open("input.txt", mode="r", encoding="utf-8-sig")
numbers = [int(l.strip()) for l in f]
numbers.sort()

# add wall outlet
numbers.insert(0, 0)

pre_computes = {}

def count_arrangements(start):
    if start == len(numbers)-1:
        return 1
    total = 0
    for i in range(start+1, min(start+4, len(numbers))):
        if numbers[i] - numbers[start] <= 3:
            if numbers[i] not in pre_computes:
                arr = count_arrangements(i)
                total += arr
                pre_computes[numbers[i]] = arr
            else:
                total += pre_computes[numbers[i]]
    return total

print(count_arrangements(0))