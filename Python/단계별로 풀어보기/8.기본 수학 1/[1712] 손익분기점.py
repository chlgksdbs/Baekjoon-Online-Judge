n = input().split()
a = int(n[0]) # 고정 비용
b = int(n[1]) # 가변 비용
c = int(n[2]) # 노트북 가격
cnt = 0 # 이익이 발생하는 판매량

if b >= c:
    cnt = -1
else:
    i = a // (c - b) # 반복 횟수를 줄이기 위한 계산
    while True:
        if a + (b * i) < (c * i):
            cnt = i
            break
        else:
            i += 1
print(cnt)

# 이 문제의 key point는 반복 횟수를 줄이기 위해 i값을 계산하고 반복문을 돌려야 시간초과가 발생하지 않는다는 것이다.
