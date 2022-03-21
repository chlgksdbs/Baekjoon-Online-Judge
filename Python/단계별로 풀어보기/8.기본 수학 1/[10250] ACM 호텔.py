import sys
t = int(input()) # T개의 테스트 데이터
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    # h : 호텔의 층 수, w : 각 층의 방 수, n : n번째 손님
    if n % h == 0: # 경우의 수 (1)
        a = (h * 100) # YY
        b = (n // h) # XX
        print(a + b)
    else: # 경우의 수 (2)
        a = (n % h) * 100 # YY
        b = (n // h) + 1 # XX
        print(a + b)
