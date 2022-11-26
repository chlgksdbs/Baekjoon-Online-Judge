t = int(input()) # t : 테스트 케이스의 개수
for i in range(t):
    n = int(input()) # n 입력
    
    d = [0] * 101 # dp 테이블 초기화
    # 1 ~ 5까지 초기화
    d[1] = 1
    d[2] = 1
    d[3] = 1
    d[4] = 2
    d[5] = 2

    for i in range(6, n + 1):
        d[i] = d[i - 1] + d[i - 5]
    
    print(d[n])
