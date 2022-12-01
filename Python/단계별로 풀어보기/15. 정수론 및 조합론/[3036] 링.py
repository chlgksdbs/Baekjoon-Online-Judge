def gcd(x, y): # 최대 공약수를 구하는 함수 (x > y)
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input()) # n : 링의 개수
data = list(map(int, input().split()))
a = data[0] # 첫 번째 링의 반지름

for i in range(1, n):
    b = data[i]
    c = gcd(a, b)
    print(a//c, "/", b//c, sep='')