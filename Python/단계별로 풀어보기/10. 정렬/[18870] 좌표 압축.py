import sys

n = int(sys.stdin.readline()) # n : 좌표의 개수
data = list(map(int, sys.stdin.readline().split()))
new_data = set(sorted(data)) # 중복 제거를 위해 set으로 변환
new_data = list(new_data) # 중복 제거 후, index 함수 사용을 위해 list로 변환

for x in data:
    print(new_data.index(x), end = ' ') # 정렬한 리스트에서 x 원소의 인덱스 찾기
