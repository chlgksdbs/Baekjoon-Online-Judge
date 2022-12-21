n = int(input()) # n : 길이가 n인 계단 수

d = [[0] * 10 for _ in range(n)] # 2차원 dp 테이블 생성
for i in range(1, 10): # 첫 번째 자리 수를 1로 초기화(0은 제외)
    d[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0: # 값이 0인 경우는 계단 수가 하나밖에 없음
            d[i][j] = d[i - 1][j + 1]
        elif j == 9: # 값이 9인 경우는 계단 수가 하나밖에 없음
            d[i][j] = d[i - 1][j - 1]
        else: # 값이 0, 9인 경우를 제외한 수는 계단 수가 두개씩 있음
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

sum = 0
for i in range(10):
    sum += d[n - 1][i]
print(sum % 1000000000) # 마지막 dp 테이블 값들의 합
