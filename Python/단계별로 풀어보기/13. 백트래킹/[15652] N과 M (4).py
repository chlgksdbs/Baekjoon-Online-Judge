from itertools import combinations_with_replacement # 중복조합

# n : 1 ~ n까지의 수, m : m개를 고른 수열
n, m = map(int, input().split())

data = []
for i in range(1, n + 1):
    data.append(i) # 1 ~ n까지의 수를 data 리스트에 추가

result = list(combinations_with_replacement(data, m)) # m개를 뽑는 모든 조합 구하기(중복 허용)

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end = ' ')
    print()