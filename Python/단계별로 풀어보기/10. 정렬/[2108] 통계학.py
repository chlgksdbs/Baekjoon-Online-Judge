import sys

n = int(sys.stdin.readline()) # n : 수의 개수
data = []
for _ in range(n): # 입력
    data.append(int(sys.stdin.readline()))
data.sort() # 오름차순 정렬
data_cnt = [0] * 8001 # 계수 정렬을 위한 리스트
for x in data: # 계수 정렬
    data_cnt[x + 4000] += 1

max_cnt = [] # 최빈값을 저장하는 리스트
result = max(data_cnt)
for i in range(len(data_cnt)):
    if data_cnt[i] == result:
        max_cnt.append(i)

print(int(round(sum(data) / n, 0))) # (1) 산술평균
print(data[n // 2]) # (2) 중앙값
# (3) 최빈값
if len(max_cnt) > 1:
    print(max_cnt[1] - 4000)
else:
    print(max_cnt[0] - 4000)
print(data[-1] - data[0]) # (4) 범위