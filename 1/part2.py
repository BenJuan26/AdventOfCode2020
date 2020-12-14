import sys

f = open("input.txt", mode="r", encoding="utf-8-sig")

entries = []
for line in f:
    number = int(line.strip())
    entries.append(number)

for i in range(len(entries)):
    for j in range(i, len(entries)):
        for k in range(j, len(entries)):
            if entries[i] + entries[j] + entries[k] == 2020:
                print(entries[i]*entries[j]*entries[k])
                sys.exit(0)

print("something went wrong")      
