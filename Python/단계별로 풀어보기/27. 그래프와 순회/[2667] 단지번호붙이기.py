from collections import deque

n = int(input()) # n : 총 단지수
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * n for _ in range(n)] # 해당 노드를 방문했는지 체크하는 리스트

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
num = 0 # 단지 별 번호를 붙일 변수

def bfs(x, y):
    global num
    num += 1 # 단지의 수를 증가시킴
    q = deque()
    q.append([x, y])
    visited[x][y] = True # 해당 노드를 방문처리
    graph[x][y] = num # 해당 노드값을 단지 번호로 변경
    count = 1 # 각 단지내 집의 수를 count 하는 변수, 현재 위치인 [x, y]를 포함하여 1로 초기화

    while q: # 큐가 빌 때까지 수행
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 주어진 범위를 벗어날 경우 무시
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == False: # [nx, ny] 노드의 값이 1이면서 방문 처리가 되지 않았을 때 수행
                graph[nx][ny] = num
                visited[nx][ny] = True
                count += 1
                q.append([nx, ny]) # queue에 현재 위치를 삽입하여 작업 반복
    
    return count

data = [] # bfs 수행의 결과 값을 담을 리스트

for i in range(n): # 해당 노드 값이 1이면서 방문 처리가 되지 않은 노드에 대해 bfs 수행
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            data.append(bfs(i, j))

print(num) # 총 단지의 수를 출력
data.sort()
for i in range(len(data)): # 각 단지내 집의 수를 오름차순으로 정렬하여 출력
    print(data[i])
