import sys

# k : 오영식이 이미 가지고 있는 랜선의 개수, n : 필요한 랜선의 개수
k, n = map(int, input().split())
data = []
for i in range(k):
    temp = int(sys.stdin.readline()) # 이미 가지고 있는 각 랜선의 길이
    data.append(temp)
data.sort() # 이분탐색을 위한 오름차순 정렬

start = 1 # 랜선을 자르는 최소 길이
end = data[-1] # 랜선을 자르는 최대 길이
answer = 0 # n개를 만들 수 있는 랜선의 최대 길이를 저장하는 변수

while start <= end:
    mid = (start + end) // 2
    wifi_count = 0 # 자르고 난 랜선의 갯수

    for x in data:
        wifi_count += x // mid # mid만큼 자르고 남은 랜선의 길이는 버림
    
    '''
    if wifi_count == n: # 자르고 난 랜선의 개수가 구하려는 랜선의 개수와 같은 경우
        answer = mid
        break
    
    # 랜선의 최댓값 길이를 구하야 하기 때문에 해당 조건은 불필요함
    '''

    if wifi_count < n: # 자르고 난 랜선의 개수가 구하려는 랜선의 개수보다 작은 경우
        end = mid - 1
    else: # 자르고 난 랜선의 개수가 구하려는 랜선의 개수보다 큰 경우
        answer = mid # 최적의 경우 저장
        start = mid + 1

print(answer)