graph = []
row_idx = -1 # 행 번호
column_idx = -1 # 열 번호
maxValue = 0 # 최댓값

for _ in range(9):
    graph.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if maxValue <= graph[i][j]:
            maxValue = graph[i][j]
            column_idx = j + 1
            row_idx = i + 1

print(maxValue)
print(row_idx, column_idx)