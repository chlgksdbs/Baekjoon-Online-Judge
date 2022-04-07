import itertools # itertools 라이브러리 사용

n, m = map(int, input().split())
it = itertools.combinations(range(1, n+1), m) # 1 ~ n까지의 수를 m개 만큼의 조합으로 리스트저장
for i in it:
    for j in range(len(i)):
        print(i[j], end=" ")
    print()
