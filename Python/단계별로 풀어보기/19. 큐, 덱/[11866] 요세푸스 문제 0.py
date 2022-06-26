import copy
from collections import deque

# n : 사람의 수, k : k번째 사람 제거
n, k = map(int, input().split())
data = [i for i in range(1, n + 1)] # 1 ~ n까지의 사람을 담는 리스트
cnt = 0 # 반복 횟수를 저장하는 변수
result = [] # 요세푸스 문제의 정답을 저장하는 리스트

while data:
    data = deque(data)
    temp = [] # 임시적인 공간 리스트
    for _ in range(len(data)):
        cnt += 1 # 반복 횟수 증가
        x = data.popleft()
        if cnt % k == 0: # 현재 반복 횟수가 k의 배수인 경우 result 리스트에 추가
            result.append(x)
        else: # 현재 반복 횟수가 k의 배수가 아닌 경우 temp 리스트에 추가
            temp.append(x)
    
    data = copy.deepcopy(temp) # 새로 생성된 temp 리스트를 data 리스트에 깊은 복사

print("<", result[0], end='', sep='')
for i in range(1, len(result)):
    print(", ", result[i], end='', sep='')
print(">")
