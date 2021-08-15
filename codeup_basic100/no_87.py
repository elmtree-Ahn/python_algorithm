data = int(input())
for i in range(1, data+1):
  if i % 3 == 0:
    continue
  else:
    print(i, end=" ")