n = int(input()) # n : 진짜 약수의 개수
data = list(map(int, input().split())) # data : 진짜 약수의 리스트

print(max(data) * min(data)) # 가장 작은 수 x 가장 큰 수