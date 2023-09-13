import random

randomlist = []
for i in range(1024):
    n = random.randint(-1000, 1000)
    randomlist.append(n)

randomlist.sort()

index = 0
while (index < len(randomlist)):
    if randomlist[index] < 0:
        randomlist.pop(index)
    else:
        index += 1


print(randomlist)
