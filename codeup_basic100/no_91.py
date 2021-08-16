a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
print(d)
