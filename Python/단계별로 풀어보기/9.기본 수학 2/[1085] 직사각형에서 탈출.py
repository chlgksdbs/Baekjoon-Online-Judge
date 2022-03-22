import sys
x, y, w, h = map(int, sys.stdin.readline().split()) # 입력
min_arr = [x, y, (w - x), (h - y)] # 최솟값이 나오는 4가지 경우의 수
print(min(min_arr)) # 경우의 수 중 최솟값
