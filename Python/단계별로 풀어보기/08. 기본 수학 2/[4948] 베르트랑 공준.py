import math

# 소수인지 체크하는 함수
def isPrimeNumber(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

primeList = [] # primeList : 입력 값의 최소 크기인 2부터 123456 * 2 + 1 까지의 소수를 담은 리스트
for x in range(2, 123456 * 2 + 1):
    if isPrimeNumber(x):
        primeList.append(x)

while True:
    n = int(input())

    if n == 0:
        break

    nCount = 0 # nCount : n보다 크고, 2n보다 작거나 같은 소수의 개수를 저장하는 변수

    for x in primeList:
        if x > 2 * n:
            break
        elif n < x and x <= 2 * n:
            nCount += 1
    
    print(nCount)
