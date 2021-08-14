w, h, b = input().split()
w, h, b = int(w), int(h), int(b)
result = w * h * b / 8 / 1024 / 1024
print("%0.2f" % result, "MB")
