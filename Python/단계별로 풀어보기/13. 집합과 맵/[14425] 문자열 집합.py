# n : 집합 S에 포함되어 있는 문자열의 개수, m : 검사해야 하는 문자열의 개수
n, m = map(int, input().split())

s = []
for _ in range(n):
    s.append(input())

s_check = []
for _ in range(m):
    s_check.append(input())

cnt = 0 # s_check 문자열 중에 총 몇 개가 s에 포함되어 있는지 저장
for x in s_check:
    if x in s:
        cnt += 1

print(cnt)

# 10,000 x 10,000 = 100,000,000 (1억)
# 문제 시간 제한 : 2초
