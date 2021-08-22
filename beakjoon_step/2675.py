case = int(input())

for i in range(case):
    repeat, s = input().split()
    repeat = int(repeat)
    r = str()
    for j in range(len(s)):
        r += s[j] * repeat
    print(r)
