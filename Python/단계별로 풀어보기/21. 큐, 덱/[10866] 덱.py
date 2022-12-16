import sys
from collections import deque

queue = deque()

n = int(input()) # n : 명령의 수

for _ in range(n):
    data = list(sys.stdin.readline().split()) # 명령어 입력
    if len(data) == 2: # 명령어의 길이가 2인 경우(원소 삽입)
        if data[0] == "push_back":
            queue.append(data[1])
        elif data[0] == "push_front":
            queue.appendleft(data[1])
    
    else: # 명령어의 길이가 1인 경우
        if data[0] == "pop_front":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif data[0] == "pop_back":
            if queue:
                print(queue.pop())
            else:
                print(-1)
        elif data[0] == "size":
            print(len(queue))
        elif data[0] == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif data[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif data[0] == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)
