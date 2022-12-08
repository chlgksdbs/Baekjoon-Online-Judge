import sys
from collections import deque

n = int(sys.stdin.readline()) # n : 라우터 내부에 존재하는 버퍼의 크기
queue = deque()

while True:
    x = int(sys.stdin.readline())

    if x == -1: # 입력의 끝
        break

    if x == 0:
        if queue: # 입력 값이 0이면서 버퍼가 비어있지 않은 경우
            queue.popleft()
    else:
        if len(queue) < n:
            queue.append(x)

if queue:
    while queue:
        print(queue.popleft(), end = ' ')
else:
    print("empty")
