# n : 학생의 수, k : 점수가 높은 사람의 커트라인
n, k = map(int, input().split())
numList = list(map(int, input().split()))

numList.sort() # 오름차순 정렬

print(numList[-k])
