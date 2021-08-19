li = []
for i in range(9):
    li.append(int(input()))

max = max(li)
print(max)
idx = li.index(max)
print(idx + 1)