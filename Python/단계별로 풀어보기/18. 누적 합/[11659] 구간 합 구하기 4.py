# n : 수의 개수, m : 합을 구해야 하는 횟수
n, m = map(int, input().split())
data = list(map(int, input().split()))

for _ in range(m):
    # i : 합을 구해야 하는 시작 구간, j : 합을 구해야 하는 끝 구간
    i, j = map(int, input().split())
    data_sum = 0 # 구간 합을 저장하는 변수
    for x in range(i - 1, j):
        data_sum += data[x]
    
    print(data_sum) # 구간 합 출력