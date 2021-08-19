# result = input().split("X")
# print(result)
# point = 0

# for i in range(len(result)):
#     s = 0
#     for j in range(len(result[i])):
#         if result[i][j] == "O":
#             s += 1
#         else:
#             continue
#         point += s

# print(point)


n = int(input())

for i in range(n):
    result = input().split("X")
    point = 0
    for j in range(len(result)):
        s = 0
        for k in range(len(result[j])):
            if result[j][k] == "O":
                s += 1
            else:
                continue
            point += s
    print(point)
