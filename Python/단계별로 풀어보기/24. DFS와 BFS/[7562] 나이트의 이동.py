from collections import deque

n = int(input()) # n : 테스트 케이스의 개수
lrr = [] # lrr : 체스판의 한변의 길이를 담는 리스트
arr = [] # arr : 나이트가 현재 있는 칸의 위치 정보를 담는 리스트
brr = [] # brr : 나이트가 이동하려고 하는 칸의 위치 정보를 담는 리스트

for i in range(n): # 입력
    l = int(input()) # 체스판의 한변의 길이
    a_x, a_y = map(int, input().split()) # 나이트가 현재 있는 칸
    b_x, b_y = map(int, input().split()) # 나이트가 이동하려고 하는 칸
    
    lrr.append(l)
    arr.append([a_x, a_y])
    brr.append([b_x, b_y])

d_xy = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]] # 나이트의 8가지 이동 방향

for i in range(n): # 출력
    queue = deque()
    queue.append((arr[i][0], arr[i][1])) # queue에 나이트가 현재 있는 칸의 x, y좌표를 추가
    
    graph = [[0] * lrr[i] for _ in range(lrr[i])] # 방문 처리와 이동 횟수를 위한 리스트

    while queue:
        x, y = queue.popleft()

        if x == brr[i][0] and y == brr[i][1]: # 나이트가 이동하려고 하는 칸과 현재 칸의 위치가 같은 경우
            print(graph[x][y])
            break

        for dx, dy in d_xy:
            # 이동하는 x, y 좌표가 체스판 안에 위치하는 경우만 queue에 삽입
            if 0 <= (x + dx) and (x + dx) < lrr[i]:
                if 0 <= (y + dy) and (y + dy) < lrr[i]:
                    if not graph[x + dx][y + dy]: # 방문한 적 없는 경우에만 처리
                        graph[x + dx][y + dy] = graph[x][y] + 1 # 현재 칸의 이동 횟수를 증가
                        queue.append((x + dx, y + dy))
