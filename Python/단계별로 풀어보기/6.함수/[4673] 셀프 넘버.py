def d(n):
    n = str(n)
    sum = int(n)
    for i in range(len(n)):
        sum += int(n[i])

    return sum

cnt = 1
arr = [] # 셀프 넘버가 아닌 숫자들의 리스트

while True:
    if cnt > 10000:
        break
    else:
        arr.append(d(cnt))
        cnt += 1

for j in range(1, 10000):
    if arr.count(j) == 0:
        print(j)
