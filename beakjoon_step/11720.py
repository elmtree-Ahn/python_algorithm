n = int(input())
number_list = list(map(int, str(input())))
result = 0


for i in number_list:
    result += i

print(result)