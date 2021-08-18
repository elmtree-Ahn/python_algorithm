import sys

n, x = map(int, sys.stdin.readline().split())
li = sys.stdin.readline().split()

for i in range(len(li)):
  li[i] = int(li[i])
  if li[i] < x:
    print(li[i], end=" ")
  
