data = int(input())
n = 0
s = 0
while True:
    n += 1
    s += n
    if s >= data:
        print(s)
        break
