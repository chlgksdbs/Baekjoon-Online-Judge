from collections import deque

m, n = map(int, input().split()) # m : 상자의 가로 칸의 수, n : 상자의 세로 칸의 수

'''
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i].append(list(map(int, input().split()))) # 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어있지 않은 칸
'''

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split()))) # 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어있지 않은 칸

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    count = 0 # 반복 횟수를 count할 변수
    
    q = deque()
    q.append([x, y])

    while q: # 큐가 빌 때까지 수행
        x, y = q.popleft()
        count += 1 # 반복 횟수 1 증가

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == -1: # 주어진 범위를 벗어나거나, 해당 노드의 값이 -1인 경우 무시
                continue

            if graph[nx][ny] == 0: # 해당 노드의 값이 0이라면 1로 변환
                graph[nx][ny] = 1
                q.append([nx, ny])
            
    return count

count_0 = 0 # graph에서 값이 0인 노드의 개수를 세는 변수
count = 0 # bfs함수의 반복 수행의 횟수를 세는 변수

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count += bfs(i, j) # bfs 함수 수행

for i in range(n):
    print(graph[i])

for i in range(n): # 익지 않은 토마토의 개수 세기
    count_0 += graph[i].count(0)

if count_0 == 0: # 익지 않은 토마토가 없다면,
    print(count)
else: # 익지 않은 토마토가 1개라도 있다면
    print(-1)

# 현재 코드는 미완성, bfs는 구현했으나 토마토가 익을 때까지의 최소 날짜를 구하지 못함.
