n = int(input()) # 사람의 수 n 입력
data = list(map(int, input().split())) # 각 사람이 걸리는 인출시간 입입력
data.sort() # 오름차순 정렬
result = 0 # 결과 값을 담을 변수
sum = 0 # 차례대로 인출시간을 담을 변수

for x in data:
    sum += x # 각 사람이 인출하는데 걸리는 시간
    result += sum # 합

print(result)
