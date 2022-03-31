n = int(input()) # 전체 사람의 수 N 입력
data_x = [] # 몸무게를 담을 리스트
data_y = [] # 키를 담을 리스트
rank = [] # 등수를 담을 리스트

for i in range(n): # 데이터 입력
    x, y = map(int, input().split()) # 한 사람의 키와 몸무게 입력
    data_x.append(x)
    data_y.append(y)

for i in range(n): # 데이터 비교 (기준)
    count = 1 # 등수를 나타내는 변수
    for j in range(n):
        if data_x[i] < data_x[j] and data_y[i] < data_y[j]:
            count += 1
    rank.append(count)

for i in range(n): # 출력
    print(rank[i], end=' ')
