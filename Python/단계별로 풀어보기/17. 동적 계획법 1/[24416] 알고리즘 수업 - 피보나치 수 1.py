def fib(n, cnt):
    if n == 1 or n == 2:
        cnt += 1
        return 1 # 코드 1
    else:
        cnt += 1
        return fib(n - 1, cnt + 1) + fib(n - 2, cnt + 1)

def fibonacci(n, cnt):
    d = [0] * (n + 1) # dp 테이블 생성
    d[1] = 1
    d[2] = 1
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2] # 코드 2
        cnt += 1
    return cnt

n = int(input())
print(fib(n, 0), fibonacci(n, 0)) # 코드1, 코드2 실행 횟수

# 백준 : Python3 제출 시 시간 초과 발생. 따라서 PyPy3로 제출