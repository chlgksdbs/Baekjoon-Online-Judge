import sys
a1, b1 = map(int, sys.stdin.readline().split()) # 첫 번째 점의 좌표
a2, b2 = map(int, sys.stdin.readline().split()) # 두 번째 점의 좌표
a3, b3 = map(int, sys.stdin.readline().split()) # 세 번째 점의 좌표

# 접근방법 : 각 x, y좌표 별로 비교하여 3가지 점 중 다른 한가지 점을 찾음

if a1 == a2:
    x = a3
elif a1 == a3:
    x = a2
else:
    x = a1

if b1 == b2:
    y = b3
elif b1 == b3:
    y = b2
else:
    y = b1
    
print(x, y)
