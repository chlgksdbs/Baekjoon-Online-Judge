n = int(input()) # n : 포도주 잔의 개수
w = [0] # 포도주 잔에 들어있는 포도주의 양 ([0] 인덱스의 값은 0으로 초기화)

for _ in range(n):
    w.append(int(input()))

d = [0] * (n + 1) # dp 테이블 생성 ([0] 인덱스의 값은 사용하지 않는다.)

# 초기화 부분
d[1] = w[1]
if n > 1:
    d[2] = w[1] + w[2]

# 3가지 경우의 수
for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + w[i], d[i - 3] + w[i - 1] + w[i])

print(d[n])
