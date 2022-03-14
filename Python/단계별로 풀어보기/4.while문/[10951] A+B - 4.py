import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break
# Python 입력이 끝날 때 까지 출력(EOF)
