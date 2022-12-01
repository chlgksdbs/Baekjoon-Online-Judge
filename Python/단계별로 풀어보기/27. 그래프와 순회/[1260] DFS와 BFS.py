from collections import deque

# n : 정점의 개수, m : 간선의 개수, v : 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 0 ~ n까지의 2차원 리스트(빈 리스트) 생성, index 0은 사용 X

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 단방향이 아니므로 양쪽 인덱스에 모두 대입

for i in range(n + 1):
    graph[i].sort() # 정점 번호가 작은 것을 먼저 방문하기 위한 오름차순 정렬

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True # 현재 노드를 방문처리
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

def bfs(graph, v, visited_bfs):
    q = deque([v])
    visited_bfs[v] = True # 현재 노드를 방문처리
    
    while q: # queue가 빌 때까지 수행
        # queue에서 하나의 원소를 뽑아 출력
        x = q.popleft()
        print(x, end=' ')
        
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[x]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True

dfs(graph, v, visited_dfs)
print() # 줄바꿈
bfs(graph, v, visited_bfs)
