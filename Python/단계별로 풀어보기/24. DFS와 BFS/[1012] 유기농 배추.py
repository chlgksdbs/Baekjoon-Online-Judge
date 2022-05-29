from collections import deque

def bfs(graph, x, y):
    queue = deque()
    queue.append([x, y]) # 큐에 현재 x, y 좌표를 삽입

    dx = [-1, 1, 0, 0] # x좌표 이동방향
    dy = [0, 0, -1, 1] # y좌표 이동방향

    graph[y][x] = 2 # 현재 좌표를 방문처리

    while queue:
        x, y = queue.popleft() # 현재 큐에 저장되어있는 x, y좌표를 pop

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a and a < m and 0 <= b and b < n and graph[b][a] == 1: # 이동한 좌표가 배추밭 범위안에 존재하는 경우
                graph[b][a] = 2 # 방문처리
                queue.append([a, b])
    
    return 1
    

t = int(input()) # t : 테스트 케이스의 개수

for i in range(t):
    # m : 가로길이, n : 세로길이, k : 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)] # 배추밭 ( m x n )

    for j in range(k):
        # x : 배추가 심어져 있는 세로 좌표, y : 배추가 심어져 있는 가로 좌표
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    result = 0 # 필요한 배추흰지렁이의 최소 마리 수를 저장하는 변수

    for j in range(m):
        for k in range(n):
            if graph[k][j] == 1:
                result += bfs(graph, j, k)
    
    print(result)
    