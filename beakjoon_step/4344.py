import sys
n = int(sys.stdin.readline())

for i in range(n):
    scores = list(map(int, input().split()))
    avg = (sum(scores) - scores[0]) / scores[0]
    count = 0
    for j in scores[1:]:
        if j > avg:
            count += 1
    result = count / scores[0] * 100
    print(f"{result:.3f}%")
