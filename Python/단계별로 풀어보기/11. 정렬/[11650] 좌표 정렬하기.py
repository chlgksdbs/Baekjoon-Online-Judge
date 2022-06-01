n = int(input()) # n : 점의 개수
graph = []

for _ in range(n): # 입력
    x, y = map(int, input().split())
    graph.append([x, y])

graph.sort(key = lambda x : (x[0], x[1])) # x를 기준으로 오름차순 정렬, x값이 같으면 y를 기준으로 오름차순 정렬

for i in range(n): # 출력
    print(graph[i][0], graph[i][1])