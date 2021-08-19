n = int(input())
result = n
c = 0
while True:
    ten = n // 10
    one = n % 10
    sum = ten + one
    c += 1
    n = int(str(n % 10) + str(sum % 10))
    if result == n:
        break

print(c)