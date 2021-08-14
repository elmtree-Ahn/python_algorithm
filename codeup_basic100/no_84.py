# h - 체크 횟수
# b - 횟수당 비트수
# c - 채널의 개수
# s - 시간

# 위는 비트
# 출력은 MB 8 / 1024 / 1024

h, b, c, s = input().split()
h, b, c, s = int(h), int(b), int(c), int(s)
result = h * b * c * s / 8 / 1024 / 1024
print(round(result, 1), "MB")
