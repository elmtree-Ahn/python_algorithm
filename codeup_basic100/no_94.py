n = int(input())
d = input().split()

for i in range(n):
  d[i] = int(d[i])

d.sort()
print(d[0])