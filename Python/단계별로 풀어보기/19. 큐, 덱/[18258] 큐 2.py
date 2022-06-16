import sys
from collections import deque

n = int(input()) # n : 명령의 수
queue_list = deque() # 큐

for _ in range(n):
    data = list(sys.stdin.readline().split()) # 명령어 입력
    if len(data) == 2: # push 명령어
        queue_list.append(data[1])
    else:
        if data[0] == "pop":
            if queue_list:
                print(queue_list.popleft())
            else:
                print(-1)
        elif data[0] == "size":
            print(len(queue_list))
        elif data[0] == "empty":
            if queue_list:
                print(0)
            else:
                print(1)
        elif data[0] == "front":
            if queue_list:
                print(queue_list[0])
            else:
                print(-1)
        elif data[0] == "back":
            if queue_list:
                print(queue_list[-1])
            else:
                print(-1)