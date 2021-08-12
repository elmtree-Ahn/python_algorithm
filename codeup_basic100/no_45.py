a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
d = a + b + c
e = "{:.2f}".format(d / 3)
print(d, e)