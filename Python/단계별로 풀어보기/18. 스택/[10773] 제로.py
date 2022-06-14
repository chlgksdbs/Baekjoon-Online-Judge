k = int(input()) # k : 정수
data = [] # 스택 자료구조

for _ in range(k):
    n = int(input())
    if n == 0: # 입력된 정수가 "0"인 경우, 가장 최근에 쓴 수를 제거
        data.pop()
    else: # 입력된 정수가 "0"이 아닌 경우, 해당 수를 스택에 push
        data.append(n)

print(sum(data)) # 남아있는 원소의 합을 출력
