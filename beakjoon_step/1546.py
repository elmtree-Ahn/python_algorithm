n = int(input())
li = input().split()
for i in range(n):
    li[i] = int(li[i])

my_max = max(li)

sum = 0

for j in range(len(li)):
    sum += li[j] / my_max * 100

result = sum / n

print(result)
