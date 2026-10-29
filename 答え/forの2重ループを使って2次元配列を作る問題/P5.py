import random

item = []

for i in range(3):
    row = []
    for j in range(3):
        num = random.randint(0, 1)
        row.append(num)
    item.append(row)

print(item)