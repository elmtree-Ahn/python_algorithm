a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
ab = a if (a <= b) else b
abc = ab if (ab <= c) else c
print(abc)