from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n): # n개의 줄에 미로 입력
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque() 
    q.append((x, y)) # 시작 지점을 queue에 삽입
    
    while q: # queue가 빌 떄까지 수행
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 주어진 범위를 벗어나는 경우 무시
                continue

            if graph[nx][ny] == 0: # 이동할 수 없는 칸인 경우 무시
                continue

            if graph[nx][ny] == 1: # 해당 노드를 처음 방문하는 경우 최단거리 기록
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    
    return graph[n - 1][m - 1]

print(bfs(0, 0))
