croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
data = input()

for alphabet in croatia:
    data = data.replace(alphabet, "!")

print(len(data))
