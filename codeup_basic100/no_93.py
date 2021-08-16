n = int(input())
r = input().split()

for i in range(n):
    r[i] = int(r[i])

li = []
for i in range(n):
    li.append(r[i])

for i in range(n-1, -1, -1):
    print(li[i], end=" ")
