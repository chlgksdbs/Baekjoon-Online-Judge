import heapq
import sys

n = int(input()) # n : 연산의 개수
arr = [] # arr : 배열

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if not arr: # 배열이 비어 있는 경우
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -x)
