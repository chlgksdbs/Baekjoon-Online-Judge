from collections import deque

m, n = map(int, input().split()) # m : 상자의 가로 칸의 수, n : 상자의 세로 칸의 수

'''
# 문제점 : 해당 코드 사용 시, index of list out 오류가 발생, 이유는 graph 리스트를 초기할 때 2중 리스트로 선언했는데, 반복문에서 value 입력 시에 또다시 list로 선언하여 3중 리스트가 되는 것으로 보임.
# 해결방안 : 1) graph 리스트를 초기화 할 때, graph = []로만 초기화 후에 반복문에서 list로 입력받기
            2) graph 리스트는 해당 코드와 같이 초기화 하고, 반복문에서 입력 시 list를 제거하고 map(int, input().split()) 형식으로만 입력받기
            
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i].append(list(map(int, input().split()))) # 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어있지 않은 칸
'''

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split()))) # 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어있지 않은 칸

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(data):
    max_value = 1 # 토마토가 모두 익을 때까지의 최소 날짜를 구하기 위한 변수
    q = deque()
    for i in range(len(data)):
        q.append([data[i][0], data[i][1]])

    while q: # 큐가 빌 때까지 수행
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == -1: # 주어진 범위를 벗어나거나, 해당 노드의 값이 -1인 경우 무시
                continue

            if graph[nx][ny] == 0: # 해당 노드의 값이 0이라면 1로 변환
                graph[nx][ny] = graph[x][y] + 1
                max_value = graph[nx][ny]
                q.append([nx, ny])
            
    return max_value - 1

error_value = 0 # graph에서 값이 0인 노드의 개수를 세는 변수
count = 0 # bfs함수의 반복 수행의 횟수를 세는 변수
data = [] # 그래프에서 노드의 값이 1인 x, y좌표의 위치를 담는 리스트

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            data.append([i, j]) # data리스트에 그 값을 추가

count = bfs(data) # bfs 함수 수행

for i in range(n): # 익지 않은 토마토의 개수 세기
    error_value += graph[i].count(0)

if error_value == 0: # 익지 않은 토마토가 없다면,
    print(count)
else: # 익지 않은 토마토가 1개라도 있다면
    print(-1)

# 토마토가 모두 익을 때까지의 최소 날짜를 구하기 위한 idea로, bfs를 수행할 때마다 다음 노드의 값을 1씩 증가시키고, 그 중 가장 큰 값에 -1을 해줌으로써 익은 날짜를 계산할 수 있다.
# max_value 값을 초기화할 때, 이미 수행할 수 없는 상태(백준 문제 예제 (5))와 같이 날짜가 0인 경우를 생각해야 하므로 max_value 값을 1로 초기화 함.
