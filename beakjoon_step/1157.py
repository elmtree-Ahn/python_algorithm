data = input().upper()
count = {}

for i in data:
    try:
        count[i] += 1
    except:
        count[i] = 1

result = [k for k, v in count.items() if max(count.values()) == v]
if len(result) > 1:
    print("?")
elif len(result) == 1:
    print(result[0])
