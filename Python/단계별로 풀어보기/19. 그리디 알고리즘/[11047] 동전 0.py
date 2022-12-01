n, k = map(int, input().split()) # n : 동전 종류의 개수, k : 동전의 합
data = [] # 동전의 가치
result = 0 # 동전 개수를 count할 변수

for i in range(n):
    x = int(input()) # 동전의 가치 입력(문제 조건에 따라)
    data.append(x)

for i in range(n - 1, -1, -1): # (n - 1) ~ 0으로 배열을 접근(오름차순 정렬이기 때문에)
    result += k // data[i] # data[i]의 원소와 나누어지는 몫만큼 count를 셈
    k %= data[i] # k값을 data[i]와 나누어진 나머지로 변경

print(result)
