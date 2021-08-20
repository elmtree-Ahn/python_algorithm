numbers = set(range(1, 10001))
unself_numbers = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    unself_numbers.add(i)

result = sorted(numbers - unself_numbers)

for i in result:
    print(i)