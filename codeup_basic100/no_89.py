a, r, n = input().split()
a, r, n = int(a), int(r), int(n)
s = a
for i in range(2, n + 1):
  s = (s * r)

print(s)


