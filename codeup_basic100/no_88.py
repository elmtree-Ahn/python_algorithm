# 등차수열
# a = 시작하는 숫자
# d = 등차
# n = 번째

a, d, n = input().split()
a, d, n = int(a), int(d), int(n)
result = 0
for i in range(0, n):
    result = a + (d * i)

print(result)
