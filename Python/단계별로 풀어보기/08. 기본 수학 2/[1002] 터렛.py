import math # 제곱근 연산을 수행하기 위한 라이브러리

t = int(input()) # test case의 수

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) # 각 변수 입력
    d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)) # 점과 점 사이의 거리
    dr1 = r1 + r2 # 원의 반지름 더하기 연산 (외접상태)
    dr2 = math.fabs(r1 - r2) # 원의 반지름 빼기 연산 (내접상태)

    if d == 0: # 두 원의 중심이 같을 때,
        if dr2 == 0: # 원의 반지름이 같다면
            print("-1") # 류재명이 있을 수 있는 좌표의 수는 무한대
        else: # 원의 반지름이 다르다면
            print("0") # 류재명이 있을 수 있는 좌표의 수는 0개

    else: # 두 원의 중심이 다를 때,
        if dr2 > d: # (1) 원이 원을 포함할 때,
            print("0")
        elif dr2 == d: # (1) 원이 원을 포함할 때,
            print("1")
        elif d < dr1: # (2) 원이 서로 밖에 있을 때,
            print("2")
        elif d == dr1: # (2) 원이 서로 밖에 있을 때,
            print("1")
        elif d > dr1: # (2) 원이 서로 밖에 있을 때,
            print("0")
