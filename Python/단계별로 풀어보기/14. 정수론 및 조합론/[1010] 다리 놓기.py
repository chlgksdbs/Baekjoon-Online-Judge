t = int(input()) # t : 테스트 케이스의 개수

for _ in range(t):
    # n : 서쪽에 있는 사이트의 개수, m : 동쪽에 있는 사이트의 개수
    n, m = map(int, input().split())

    i = n # 반복문 횟수
    a = 1 # 분모
    b = 1 # 분자

    while i > 0: # 콤비네이션 수행
        a *= n
        b *= m

        n -= 1
        m -= 1
        i -= 1
    
    print(b // a)