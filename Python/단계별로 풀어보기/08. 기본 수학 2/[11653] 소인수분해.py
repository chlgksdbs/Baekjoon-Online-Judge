n = int(input()) # 정수 N (1 <= N <= 10,000,000)

if n > 1:
    i = 2
    while True: # 소수로 나누기
        if n == 1:
            break
        elif n % i == 0:
            n = n // i
            print(i)
        else:
            i += 1
            
# 처음 이 문제를 풀이할 때 알고리즘 설계를 (1) 소수 판별 -> (2) 소수로 나누기의 영역으로 접근했다.
# 위와 같이 풀이를 했을 때 시간초과가 발생했고, 질문게시판을 통해 검색한 결과 소수 판별 부분이 필요 없다는 걸 알았다.
