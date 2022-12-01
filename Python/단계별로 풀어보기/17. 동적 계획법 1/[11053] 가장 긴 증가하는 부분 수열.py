n = int(input()) # n : 수열의 크기
array = list(map(int, input().split())) # n만큼의 크기의 수열 입력

d = [1] * n # dp 테이블 생성

# LIS(Longest Increasing Subsequence) 알고리즘 (시간복잡도 : O(N^2))
for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))