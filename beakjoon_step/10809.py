s = input()
alphabet_list = 'abcdefghijklmnopqrstuvwxyz'
result = list()

for i in alphabet_list:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print("-1", end=' ')
