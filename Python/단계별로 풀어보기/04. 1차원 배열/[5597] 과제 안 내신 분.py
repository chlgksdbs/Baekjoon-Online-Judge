array = []

for _ in range(28):
    array.append(int(input()))

for x in range(1, 31):
    if x not in array:
        print(x)