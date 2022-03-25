import sys
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break

    # 접근 방법 : a, b, c 중 가장 큰 값을 찾고, 나머지를 제곱하여 더했을 때 피타고라스의 정리를 만족하는지 체크한다.
    if a > b:
        if a > c: # a가 가장 큰 경우
            if (a ** 2) == (b ** 2) + (c ** 2):
                print("right")
            else:
                print("wrong")
        else: # c가 가장 큰 경우
            if (c ** 2) == (a ** 2) + (b ** 2):
                print("right")
            else:
                print("wrong")
    else:
        if b > c: # b가 가장 큰 경우
            if (b ** 2) == (a ** 2) + (c ** 2):
                print("right")
            else:
                print("wrong")
        else: # c가 가장 큰 경우
            if (c ** 2) == (a ** 2) + (b ** 2):
                print("right")
            else:
                print("wrong")
