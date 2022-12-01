def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1: # 종료조건
        break
    d = [[0, 0, 0] for _ in range(max(x, y, z))] # dp 테이블 생성
    
    print("w(", x, ", ", y, ", ", z, ") = ", w(x, y, z), sep='')