import sys

n = int(input()) # n : 수의 개수
data = []
for _ in range(n):
    temp = int(sys.stdin.readline())
    data.append(temp)
data.sort() # 입력받은 원소를 오름차순으로 정렬

for i in range(n): # 차례대로 출력
    print(data[i])