from collections import deque

# n : 수빈이가 있는 위치, k: 동생이 있는 위치
n, k = map(int, input().split())
data = [0 for _ in range(100001)] # 시간 체크 및 방문 처리를 위한 리스트 (범위는 100,000 까지)

queue = deque()
queue.append(n) # n을 출발지점으로 하는 queue 생성

while True:
    v = queue.popleft()
    graph = [v - 1, v + 1, 2 * v] # 3가지 이동 방법을 나타내는 리스트

    if v == k: # 동생이 있는 위치를 찾은 경우
        print(data[v])
        break
    else: # 동생이 있는 위치를 찾지 못한 경우
        for next in graph: # 3가지 이동 방법을 모두 queue에 삽입
            if 0 <= next and next <= 100000 and not data[next]:
                data[next] = data[v] + 1
                queue.append(next)