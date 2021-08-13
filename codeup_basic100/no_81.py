data = int(input(), 16)
for i in range(1, 16):
    answer = data * i
    print("%X*%X=%X" % (data, i, answer))
