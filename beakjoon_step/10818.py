n = int(input())
li = input().split()
for i in range(n):
    li[i] = int(li[i])
li.sort()
print(li[0], li[-1])