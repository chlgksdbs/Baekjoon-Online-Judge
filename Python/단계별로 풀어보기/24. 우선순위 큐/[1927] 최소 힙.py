import heapq # heapq (priority queue) 알고리즘
import sys

n = int(input()) # 연산의 개수인 n 입력
heap = [] # 최소 힙을 구현하는 heap 리스트 생성
result = [] # 출력될 값을 저장하는 result 리스트 생성

for _ in range(n):
    x = int(sys.stdin.readline()) # 연산에 대한 정보를 나타내는 정수인 x 입력
    if x == 0:
        if heap: # heap 리스트에 원소가 존재하는 경우
            result.append(heapq.heappop(heap)) # 가장 작은 원소를 heap에서 제거함과 동시에 결과값을 result 리스트에 삽입
        else: # heap 리스트에 원소가 존재하지 않는 경우
            result.append(0)
    
    else:
        heapq.heappush(heap, x) # x가 자연수라면 heap 리스트에 x라는 값을 추가

for y in result: # 저장된 출력 값들을 출력
    print(y)

# 입력 라인이 1,000,000인 경우, input() 대신 sys.stdin.readline() 사용
