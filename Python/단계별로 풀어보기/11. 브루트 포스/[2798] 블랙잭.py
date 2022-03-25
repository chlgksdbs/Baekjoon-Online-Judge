n, m = map(int, input().split()) # n, m값 입력
arr = list(map(int, input().split())) # 크기가 n인 배열
sum = 0 # 3장의 카드의 합계 중 가장 큰 값

for i in range(0,  n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            nsum = arr[i] + arr[j] + arr[k] # 3장의 카드 크기의 합
            if sum <= nsum and nsum <= m:
                sum = nsum
            if sum == m:
                break;

print(sum)
