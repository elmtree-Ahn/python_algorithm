data = int(input())
sum = 0
num = 0
while True:
    num += 1
    sum += num
    if sum >= data:
        print(num)
        break
