repeat = int(input())
count = repeat

for i in range(0, repeat):
    data = input()
    for j in range(0, len(data) - 1):
        if data[j] == data[j+1]:
            pass
        elif data[j] in data[j+1:]:
            count -= 1
            break

print(count)
