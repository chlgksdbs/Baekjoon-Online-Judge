c = int(input()) # test case

for i in range(c):
    sum = 0 # sum score
    cnt = 0 # count variable
    std = map(int, input().split()) # student number
    std = list(std) # map class => list (type casting)

    for j in range(1, std[0] + 1):
        sum += std[j]

    avg = sum / (len(std) - 1) # average score

    for k in range(1, std[0] + 1):
        if std[k] > avg:
            cnt += 1

    result = cnt/(len(std) - 1) * 100
    print("{:.3f}%".format(result))

# 파이썬에서 실수를 표현하는 방식에서 '.format'을 이용하는 방법으로 나타냄
