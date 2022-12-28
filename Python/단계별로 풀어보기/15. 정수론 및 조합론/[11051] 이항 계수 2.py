def factorial(x):
    result = 1
    for i in range(x, 0, -1):
        result *= i
    return result

# n : 자연수, k : 정수
n, k = map(int, input().split())

a = factorial(n)
b = factorial(k)
c = factorial(n - k)

answer = a // (b * c)
print(answer % 10007)
