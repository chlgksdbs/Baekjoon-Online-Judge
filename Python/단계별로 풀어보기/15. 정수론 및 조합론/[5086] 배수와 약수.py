while True:
    x, y = map(int, input().split()) # 입력
    if x == 0 and y == 0: # 종료조건
        break

    if y % x == 0: # (1) 첫 번째 숫자가 두 번째 숫자의 약수인 경우
        print("factor")
    elif x % y == 0: # (2) 첫 번째 숫자가 두 번째 숫자의 배수인 경우
        print("multiple")
    else: # (3) 둘 다 아닌 경우
        print("neither")
