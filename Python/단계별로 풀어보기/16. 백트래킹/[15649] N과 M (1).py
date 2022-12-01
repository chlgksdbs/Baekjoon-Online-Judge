from itertools import permutations # permutations(iterable, r = None) : iterable에서 원소 개수가 r개인 순열 뽑기

n, m = map(int, input().split())
I = [] # 1부터 N까지의 수를 담을 배열

for i in range(n):
    I.append(i + 1) # 1부터 N까지의 수 입력

for i in permutations(I, m): # r을 지정하지 않거나 r = None으로 하면 최대 길이의 순열 리턴
    for j in range(m):
        print(i[j], end=' ', sep=' ') # 리스트 원소 별로 띄어쓰기 출력
    print() # 줄 바꿈
