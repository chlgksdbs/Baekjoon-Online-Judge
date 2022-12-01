from collections import deque

t = int(input()) # t : 테스트 케이스의 수

for _ in range(t):
    # n : 문서의 개수, m : 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수
    n, m = map(int, input().split())
    data = list(map(int, input().split())) # n개 문서의 중요도를 담는 리스트
    queue = deque(data)
    
    