from itertools import product
# product(중복 순열)는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다. 다만 원소를 중복하여 뽑는다.

n, m = map(int, input().split())
data = [] # 1 ~ n까지의 수를 담을 리스트
for i in range(1, n + 1):
    data.append(i)

result = list(product(data, repeat=m)) # m개를 뽑는 모든 순열 구하기(중복 허용)

for i in range(len(result)):
    for j in range(m):
        print(result[i][j], end=' ') # 리스트의 각 원소를 한줄에 띄어쓰기 형태로 출력
    print() # 줄 바꿈
