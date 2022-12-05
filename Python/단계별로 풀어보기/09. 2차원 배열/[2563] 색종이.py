n = int(input()) # n : 색종이의 수
result = 0 # result : 색종이가 붙은 검은 영역의 넓이

graph = [[0] * 100 for _ in range(100)] # graph : n개의 색종이로 덮힌 100 x 100의 흰색 도화지
for _ in range(n):
    # x : 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리, y : 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리
    x, y = map(int, input().split())
    
    x -= 1
    y -= 1

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if graph[i][j] == 0:
                graph[i][j] = 1

for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            result += 1

print(result)
