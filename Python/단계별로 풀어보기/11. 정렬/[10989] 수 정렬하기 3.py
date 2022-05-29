import sys

n = int(sys.stdin.readline()) # n : 수의 개수
n_count = [0] * 10001 # 주어진 수의 범위가 10000보다 작거나 같은 자연수

for _ in range(n):
    n_count[int(sys.stdin.readline())] += 1 # 입력하는 수에 해당하는 인덱스 값에 1을 더함

for i in range(1, 10001):
    if n_count[i] > 0: # 해당 인덱스의 값이 존재하는 경우
        for j in range(n_count[i]):
            print(i)