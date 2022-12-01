from collections import deque

n = int(input())

queue = []
for i in range(n): # 1 ~ n까지의 수를 리스트에 삽입
    queue.append(i + 1)
queue = deque(queue)

while len(queue) > 1:
    # 1) 제일 위에 있는 카드를 바닥에 버림
    queue.popleft()
    
    # 2) 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김
    temp = queue.popleft()
    queue.append(temp)

print(queue[0]) # 마지막 남은 카드 한장을 출력
