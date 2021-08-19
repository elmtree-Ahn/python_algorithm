li = []
result = []

for i in range(10):
    li.append(int(input()))

for j in range(len(li)):
    result.append(li[j] % 42)

my_set = set(result)
print(len(my_set))