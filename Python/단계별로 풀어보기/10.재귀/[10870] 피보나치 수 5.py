def Fibonacci(n, a, b): # n은 count 변수, a는 전전 숫자, b는 전 숫자
    if n == 0:
        return a
    else:
        c = a + b
        return Fibonacci(n - 1, b, c)

x = int(input()) # 입력
print(Fibonacci(x, 0, 1))
