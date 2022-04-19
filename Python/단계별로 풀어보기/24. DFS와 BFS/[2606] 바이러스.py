n = int(input()) # 컴퓨터의 수
m = int(input()) # 컴퓨터가 연결된 쌍의 수
graph = [[] for _ in range(n + 1)] # 각 노드 별, 연결되어 있는 컴퓨터 번호를 담을 리스트

for i in range(m):
    a, b = map(int, input().split()) # 연결된 컴퓨터 정보
    # 쌍방향 연결이므로, 양쪽 노드에 연결된 정보를 추가
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)): # 입력된 노드들을 오름차순으로 정렬
    graph[i].sort()

visited = [False] * (n + 1) # 각 노드 별 방문 정보를 담은 리스트

def dfs(graph, v, visited):
    visited[v] = True # 방문처리
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited) # dfs 수행

count = -1 # 1번 컴퓨터의 수를 제외하기 때문에, 1번은 항상 감염
for i in range(len(visited)):
    if visited[i] == True:
        count += 1

print(count)
