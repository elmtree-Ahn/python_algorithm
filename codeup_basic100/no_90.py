a, m, d, n = input().split()
a, m, d, n = int(a), int(m), int(d), int(n)
for i in range(1, n):
    a = (a * m) + d
print(a)
