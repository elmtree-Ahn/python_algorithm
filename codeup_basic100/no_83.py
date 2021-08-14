r, g, b = input().split()
r, g, b = int(r), int(g), int(b)
total = 0
for i in range(0, r):
  for j in range(0, g):
    for k in range(0, b):
      print(i, j, k)
      total += 1
print(total)
