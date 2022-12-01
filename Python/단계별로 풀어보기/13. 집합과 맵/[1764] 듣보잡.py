# n : 듣도 못한 사람의 수, m : 보도 못한 사람의 수
n, m = map(int, input().split())
n_name = []
m_name = []
result = [] # 정답 값을 담는 리스트

for _ in range(n): # 입력
    n_name.append(input())
for _ in range(m): # 입력
    m_name.append(input())

# list -> set 변경
n_name = set(n_name)
m_name = set(m_name)

result = n_name & m_name # 교집합을 result에 저장
result = list(result) # set -> list 변경

result.sort() # 사전 순으로 오름차순 정렬

print(len(result)) # 길이를 출력
for i in range(len(result)): # 리스트 원소를 출력
    if i == len(result) - 1:
        print(result[i], end='')
    else:
        print(result[i])
