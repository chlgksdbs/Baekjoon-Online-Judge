def gcd(a, b): # 유클리드 알고리즘 : 최대 공약수 구하기 (a > b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
t = int(input()) # t : 테스트 케이스의 개수

for _ in range(t):
    a, b = map(int, input().split()) # a, b : 자연수

    if a < b: # b가 a보다 큰 경우 두 수를 교체
        temp = b
        b = a
        a = temp

    n = gcd(a, b) # 최대 공약수를 계산
    print((a // n) * (b // n) * n) # 최소 공배수를 출력