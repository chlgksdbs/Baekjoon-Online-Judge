n = int(input()) # n : 점의 개수
graph = []
for _ in range(n): # 입력
    x, y = map(int, input().split())
    graph.append([x, y])

graph.sort(key = lambda x : (x[1], x[0])) # (1) y좌표 오름차순, (2) x좌표 오름차순

for i in range(n): # 출력
    print(graph[i][0], graph[i][1])